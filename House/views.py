import xlsxwriter
from django.http import FileResponse
from django.shortcuts import render

# Create your views here.
from .models import TbWtfwHccg, TbHcqy
from django.db import connection


def house_short(request):
    # 从models获取数据传给template(house对象就是queryset)
    sql1 = '''
        SELECT
        tb_hcqy.sdm,
        tb_hcqy.smc 省名称,
        SUM(CASE WHEN fwlx = '1' AND zzlb = '1' OR NULL THEN 1 ELSE 0 END) 单户住宅类,
        SUM(CASE WHEN fwlx = '1' AND zzlb = '2' OR NULL THEN 1 ELSE 0 END) 多户住宅类,
        SUM(CASE WHEN fwlx = '3' OR NULL THEN 1 ELSE 0 END) 产业类,
        SUM(CASE WHEN fwlx = '2' OR NULL THEN 1 ELSE 0 END) 公共服务类,
        SUM(
        CASE WHEN fwlx = '1' AND zzlb = '1' OR NULL
        OR fwlx = '1' AND zzlb = '2' OR NULL
        OR fwlx = '3' OR NULL
        OR fwlx = '2' OR NULL THEN 1 ELSE 0 END
        ) 合计
        FROM tb_hcqy
        RIGHT JOIN tb_wtfw_hccg
        ON tb_wtfw_hccg.xzqdm = tb_hcqy.xdm
        GROUP BY tb_hcqy.sdm,tb_hcqy.smc
        ORDER BY tb_hcqy.sdm;
        '''
    houses = TbHcqy.objects.raw(
        sql1
    )
    # 住宅类数量
    Residential = TbWtfwHccg.objects.filter(fwlx='1').count()  # 住宅类
    Public_service = TbWtfwHccg.objects.filter(fwlx='2').count()  # 公共服务类
    Industry = TbWtfwHccg.objects.filter(fwlx='3').count()  # 产业类
    Others = TbWtfwHccg.objects.filter(fwlx='').count()  # 其他

    return render(request, 'result.html', locals())


def exporttoexcel(request):
    path = request.path_info
    code = path[path.rindex("/") + 1:]

    sql1 = """
                SELECT
                SUM(CASE WHEN fwlx = '1' AND zzlb = '1' OR NULL THEN 1 ELSE 0 END) 单户住宅类,
                SUM(CASE WHEN fwlx = '1' AND zzlb = '2' OR NULL THEN 1 ELSE 0 END) 多户住宅类,
                SUM(CASE WHEN fwlx = '2' OR NULL THEN 1 ELSE 0 END) 公共服务类,
                SUM(CASE WHEN fwlx = '3' OR NULL THEN 1 ELSE 0 END) 产业类,
                SUM(CASE WHEN fwlx = '1' AND zzlb = '1' OR NULL
                    OR fwlx = '1' AND zzlb = '2' OR NULL
                    OR fwlx = '3' OR NULL
                    OR fwlx = '2' OR NULL THEN 1 ELSE 0 END
                ) 合计,
                SUM(CASE WHEN fwlx = '1' AND zzlb = '1' OR NULL THEN zymj END)/666.667 单户住宅占用土地面积,
                SUM(CASE WHEN fwlx = '1' AND zzlb = '2' OR NULL THEN zymj END)/666.667 多户住宅占用土地面积,
                SUM(CASE WHEN fwlx = '2' OR NULL THEN zymj END)/666.667 公共服务类占用土地面积,
                SUM(CASE WHEN fwlx = '3' OR NULL THEN zymj END)/666.667 产业类占用土地面积,
                (
                    SUM(CASE WHEN fwlx = '1' AND zzlb = '1' OR NULL THEN zymj END) +
                    SUM(CASE WHEN fwlx = '1' AND zzlb = '2' OR NULL THEN zymj END) +
                    SUM(CASE WHEN fwlx = '2' OR NULL THEN zymj END) +
                    SUM(CASE WHEN fwlx = '3' OR NULL THEN zymj END)

                )/666.667 占用土地面积,
                SUM(CASE WHEN fwlx = '1' AND zzlb = '1' OR NULL THEN zygdmj END)/666.667 单户住宅占用耕地面积,
                SUM(CASE WHEN fwlx = '1' AND zzlb = '2' OR NULL THEN zygdmj END)/666.667 多户住宅占用耕地面积,
                SUM(CASE WHEN fwlx = '2' OR NULL THEN zygdmj END)/666.667 公共服务类占用耕地面积,
                SUM(CASE WHEN fwlx = '3' OR NULL THEN zygdmj END)/666.667 产业类占用耕地面积,
                (
                    SUM(CASE WHEN fwlx = '1' AND zzlb = '1' OR NULL THEN zygdmj END) +
                    SUM(CASE WHEN fwlx = '1' AND zzlb = '2' OR NULL THEN zygdmj END) +
                    SUM(CASE WHEN fwlx = '2' OR NULL THEN zygdmj END) +
                    SUM(CASE WHEN fwlx = '3' OR NULL THEN zygdmj END)
                )/666.667 占用耕地面积,
                SUM(CASE WHEN fwlx = '1' AND zzlb = '1' OR NULL THEN zyjbntmj END)/666.667 单户住宅占用永久基本农田面积,
                SUM(CASE WHEN fwlx = '1' AND zzlb = '2' OR NULL THEN zyjbntmj END)/666.667 多户住宅占用永久基本农田面积,
                SUM(CASE WHEN fwlx = '2' OR NULL THEN zyjbntmj END)/666.667 公共服务类占用永久基本农田面积,
                SUM(CASE WHEN fwlx = '3' OR NULL THEN zyjbntmj END)/666.667 产业类占用永久基本农田面积,
                (
                    SUM(CASE WHEN fwlx = '1' AND zzlb = '1' OR NULL THEN zyjbntmj END) +
                    SUM(CASE WHEN fwlx = '1' AND zzlb = '2' OR NULL THEN zyjbntmj END) +
                    SUM(CASE WHEN fwlx = '2' OR NULL THEN zyjbntmj END) +
                    SUM(CASE WHEN fwlx = '3' OR NULL THEN zyjbntmj END)
                )/666.667 占用永久基本农田面积
                FROM tb_wtfw_hccg
                WHERE xzqdm LIKE '%s%%';
                """ % code
    sql2 = """
                SELECT
                tb_hcqy.sdm 省代码,
                tb_hcqy.smc 省名称,
                tb_hcqy.cmc 市名称,
                SUM(CASE WHEN fwlx = '1' AND zzlb = '1' OR NULL THEN 1 ELSE 0 END) 单户住宅类,
                SUM(CASE WHEN fwlx = '1' AND zzlb = '2' OR NULL THEN 1 ELSE 0 END) 多户住宅类,
                SUM(CASE WHEN fwlx = '2' OR NULL THEN 1 ELSE 0 END) 公共服务类,
                SUM(CASE WHEN fwlx = '3' OR NULL THEN 1 ELSE 0 END) 产业类,
                SUM(
                CASE WHEN fwlx = '1' AND zzlb = '1' OR NULL
                OR fwlx = '1' AND zzlb = '2' OR NULL
                OR fwlx = '2' OR NULL
                OR fwlx = '3' OR NULL THEN 1 ELSE 0 END
                ) 合计
                FROM tb_wtfw_hccg
                LEFT JOIN tb_hcqy ON tb_wtfw_hccg.xzqdm = tb_hcqy.xdm
                WHERE sdm = '%s' GROUP BY tb_hcqy.sdm,tb_hcqy.smc,tb_hcqy.cmc;
    """ % code
    sql3 = """
                SELECT
                tb_hcqy.sdm 省代码,
                tb_hcqy.smc 省名称,
                tb_hcqy.cmc 市名称,
                tb_hcqy.xmc 县名称,
                tb_hcqy.xdm 县代码,
                SUM(CASE WHEN fwlx = '1' AND zzlb = '1' OR NULL THEN 1 ELSE 0 END) 单户住宅类,
                SUM(CASE WHEN fwlx = '1' AND zzlb = '2' OR NULL THEN 1 ELSE 0 END) 多户住宅类,
                SUM(CASE WHEN fwlx = '2' OR NULL THEN 1 ELSE 0 END) 公共服务类,
                SUM(CASE WHEN fwlx = '3' OR NULL THEN 1 ELSE 0 END) 产业类,
                SUM(
                CASE WHEN fwlx = '1' AND zzlb = '1' OR NULL
                OR fwlx = '1' AND zzlb = '2' OR NULL
                OR fwlx = '2' OR NULL
                OR fwlx = '3' OR NULL THEN 1 ELSE 0 END
                ) 合计
                FROM tb_wtfw_hccg
                LEFT JOIN tb_hcqy ON tb_wtfw_hccg.xzqdm = tb_hcqy.xdm
                WHERE tb_hcqy.sdm = '%s' GROUP BY tb_hcqy.sdm,tb_hcqy.smc,tb_hcqy.cmc,tb_hcqy.xmc,tb_hcqy.xdm;
    """ % code
    sql4 = """
            SELECT b.市名称,a.总图斑,a.属于摸排范围,a.已外业,a.已审核,b.总图斑,b.已外业,b.已审核
            FROM
            (SELECT
                tb_hcqy.cmc 市名称,
                COUNT(*) 总图斑,
                COUNT(sfzqczzfw = 'Y' OR NULL) 属于摸排范围,
                COUNT(wyzt = 'Y' OR NULL) 已外业,
                COUNT(shzt = 'P' OR NULL) 已审核
            FROM tb_wttb_qlist
            LEFT JOIN tb_hcqy ON tb_wttb_qlist.xzqdm = tb_hcqy.xdm
            WHERE tb_wttb_qlist.xzqdm LIKE '%s%%'
            GROUP BY tb_hcqy.cmc) a FULL JOIN (
            SELECT
                tb_hcqy.cmc 市名称,
                COUNT(*) 总图斑,
                COUNT(wyzt = 'Y' OR NULL) 已外业,
                COUNT(shzt = 'P' OR NULL) 已审核
            FROM tb_wtfw_qlist
            LEFT JOIN tb_hcqy ON tb_wtfw_qlist.xzqdm = tb_hcqy.xdm
            WHERE tb_wtfw_qlist.xzqdm LIKE '%s%%'
            GROUP BY tb_hcqy.cmc
            )b ON a.市名称 = b.市名称
    """ % (code, code)
    sql5 = """
           select a.xdm,a.xmc,a.zs,a.tbmj,a.zygdmj
            ,b.zs as ywy_zs,b.tbmj ywy_tbmj,b.zygdmj ywy_zygdmj,round(cast(b.zs as numeric)/cast(a.zs as numeric),2)*100||'%%' as bfb
            ,c.zs as ywt_zs,c.tbmj ywt_tbmj,c.zygdmj ywt_zygdmj,c.zyjbntmj ywt_zyjbntmj
            ,d.zs as ywt_z_zs,d.tbmj ywt_z_tbmj,d.zygdmj ywt_z_zygdmj,d.zyjbntmj ywt_z_zyjbntmj
            ,d1.zs as ywt_z_zs1,d1.tbmj ywt_z_tbmj1,d1.zygdmj ywt_z_zygdmj1,d1.zyjbntmj ywt_z_zyjbntmj1
            ,d2.zs as ywt_z_zs2,d2.tbmj ywt_z_tbmj2,d2.zygdmj ywt_z_zygdmj2,d2.zyjbntmj ywt_z_zyjbntmj2
            ,e.zs as ywt_g_zs,e.tbmj ywt_g_tbmj,e.zygdmj ywt_g_zygdmj,e.zyjbntmj ywt_g_zyjbntmj
            ,f.zs as ywt_c_zs,f.tbmj ywt_c_tbmj,f.zygdmj ywt_c_zygdmj,f.zyjbntmj ywt_c_zyjbntmj
            ,g.zs as yswt_zs,g.tbmj yswt_tbmj,g.zygdmj yswt_zygdmj
            ,h.zs as wwt_zs,h.tbmj wwt_tbmj,h.zygdmj wwt_zygdmj
            ,i.zs as wrd_zs,i.tbmj wrd_tbmj,i.zygdmj wrd_zygdmj
            from
            (select b1.xdm,b1.xmc,count(*) zs,sum(a1.tbmj)*0.0001 tbmj,sum(c1.ZYGDMJ)*0.0001 zygdmj from tb_wtfw_qlist a1
            left join tb_hcqy b1 on a1.xzqdm=b1.xdm
            left join tb_wtfw_hccg c1 on a1.tbbsm=c1.tbbsm
            where a1.xzqdm like '%s%%' 
            group by xdm,xmc order by xdm asc) a
            left join (
            select b2.xdm,b2.xmc,count(*) zs,sum(a2.tbmj)*0.0001 tbmj,sum(c2.ZYGDMJ)*0.0001 zygdmj from tb_wtfw_qlist a2
            left join tb_hcqy b2 on a2.xzqdm=b2.xdm
            left join tb_wtfw_hccg c2 on a2.tbbsm=c2.tbbsm
            where a2.xzqdm like '%s%%' and a2.wyzt='Y'
            group by xdm,xmc order by xdm asc) b on a.xdm =b.xdm
            left join (
            select b2.xdm,b2.xmc,sum(
            case when a2.fwlx='1' or null
                or a2.fwlx='2' or null
                or a2.fwlx='3' or null
            then 1 else 0 end
            ) zs,sum(a2.tbmj)*0.0001 tbmj,sum(c2.ZYGDMJ)*0.0001 zygdmj,sum(c2.zyjbntmj)*0.0001 zyjbntmj from tb_wtfw_qlist a2
            left join tb_hcqy b2 on a2.xzqdm=b2.xdm
            left join tb_wtfw_hccg c2 on a2.tbbsm=c2.tbbsm
            where a2.xzqdm like '%s%%' and a2.xjshjg='YWT' and a2.wyzt='Y'
            group by xdm,xmc order by xdm asc) c on a.xdm =c.xdm
            left join (
            select b2.xdm,b2.xmc,count(*) zs,sum(a2.tbmj)*0.0001 tbmj,sum(c2.ZYGDMJ)*0.0001 zygdmj,sum(c2.zyjbntmj)*0.0001 zyjbntmj from tb_wtfw_qlist a2
            left join tb_hcqy b2 on a2.xzqdm=b2.xdm
            left join tb_wtfw_hccg c2 on a2.tbbsm=c2.tbbsm
            where a2.xzqdm like '%s%%' and a2.xjshjg='YWT' and a2.fwlx='1' and a2.wyzt = 'Y'
            group by xdm,xmc order by xdm asc) d on a.xdm =d.xdm
            left join (
            select b2.xdm,b2.xmc,count(*) zs,sum(a2.tbmj)*0.0001 tbmj,sum(c2.ZYGDMJ)*0.0001 zygdmj,sum(c2.zyjbntmj)*0.0001 zyjbntmj from tb_wtfw_qlist a2
            left join tb_hcqy b2 on a2.xzqdm=b2.xdm
            left join tb_wtfw_hccg c2 on a2.tbbsm=c2.tbbsm
            where a2.xzqdm like '%s%%' and a2.xjshjg='YWT' and a2.fwlx='1' and c2.zzlb='1' and a2.wyzt = 'Y'
            group by xdm,xmc order by xdm asc) d1 on a.xdm =d1.xdm
            left join (
            select b2.xdm,b2.xmc,count(*) zs,sum(a2.tbmj)*0.0001 tbmj,sum(c2.ZYGDMJ)*0.0001 zygdmj,sum(c2.zyjbntmj)*0.0001 zyjbntmj from tb_wtfw_qlist a2
            left join tb_hcqy b2 on a2.xzqdm=b2.xdm
            left join tb_wtfw_hccg c2 on a2.tbbsm=c2.tbbsm
            where a2.xzqdm like '%s%%' and a2.xjshjg='YWT' and a2.fwlx='1' and c2.zzlb='2' and a2.wyzt = 'Y'
            group by xdm,xmc order by xdm asc) d2 on a.xdm =d2.xdm
            left join (
            select b2.xdm,b2.xmc,count(*) zs,sum(a2.tbmj)*0.0001 tbmj,sum(c2.ZYGDMJ)*0.0001 zygdmj,sum(c2.zyjbntmj)*0.0001 zyjbntmj from tb_wtfw_qlist a2
            left join tb_hcqy b2 on a2.xzqdm=b2.xdm
            left join tb_wtfw_hccg c2 on a2.tbbsm=c2.tbbsm
            where a2.xzqdm like '%s%%' and a2.xjshjg='YWT' and a2.fwlx='2' and a2.wyzt = 'Y'
            group by xdm,xmc order by xdm asc) e on a.xdm =e.xdm
            left join (
            select b2.xdm,b2.xmc,count(*) zs,sum(a2.tbmj)*0.0001 tbmj,sum(c2.ZYGDMJ)*0.0001 zygdmj,sum(c2.zyjbntmj)*0.0001 zyjbntmj from tb_wtfw_qlist a2
            left join tb_hcqy b2 on a2.xzqdm=b2.xdm
            left join tb_wtfw_hccg c2 on a2.tbbsm=c2.tbbsm
            where a2.xzqdm like '%s%%' and a2.xjshjg='YWT' and a2.fwlx='3' and a2.wyzt = 'Y'
            group by xdm,xmc order by xdm asc) f on a.xdm =f.xdm
            left join (
            select b2.xdm,b2.xmc,count(*) zs,sum(a2.tbmj)*0.0001 tbmj,sum(c2.ZYGDMJ)*0.0001 zygdmj from tb_wtfw_qlist a2
            left join tb_hcqy b2 on a2.xzqdm=b2.xdm
            left join tb_wtfw_hccg c2 on a2.tbbsm=c2.tbbsm
            where a2.xzqdm like '%s%%' and a2.xjshjg='YSWT' and a2.wyzt = 'Y'
            group by xdm,xmc order by xdm asc) g on a.xdm =g.xdm
            left join (
            select b2.xdm,b2.xmc,count(*) zs,sum(a2.tbmj)*0.0001 tbmj,sum(c2.ZYGDMJ)*0.0001 zygdmj from tb_wtfw_qlist a2
            left join tb_hcqy b2 on a2.xzqdm=b2.xdm
            left join tb_wtfw_hccg c2 on a2.tbbsm=c2.tbbsm
            where a2.xzqdm like '%s%%' and a2.xjshjg='WWT' and a2.wyzt = 'Y'
            group by xdm,xmc order by xdm asc
            ) h on a.xdm =h.xdm
            left join (
            select b2.xdm,b2.xmc,count(*) zs,sum(a2.tbmj)*0.0001 tbmj,sum(c2.ZYGDMJ)*0.0001 zygdmj from tb_wtfw_qlist a2
            left join tb_hcqy b2 on a2.xzqdm=b2.xdm
            left join tb_wtfw_hccg c2 on a2.tbbsm=c2.tbbsm
            where a2.xzqdm like '%s%%' and a2.xjshjg is null and a2.wyzt = 'Y'
            and a2.wyzt='Y'
            group by xdm,xmc order by xdm asc
            ) i on a.xdm =i.xdm
    """ % (code, code, code, code, code, code, code, code, code, code, code)
    sql6 = """
            SELECT 
            a.xdm,a.xmc,a.zs,b.zs as ywy_zs,c.zs wpfw_zs,d.zs wpfw_ywy,l.zs as nytb,
            f.zs as xjysh_zs,g.zs as xjwsh_zs,round(cast(f.zs as numeric)/cast(a.zs as numeric),2)*100||'%%' as bfb ,
            h.zs as cjwsh_zs,i.zs as cjysh_zs,j.zs as sjysh_zs,k.zs as sjwsh_zs
            FROM
            (SELECT xdm,xmc,COUNT(*) zs FROM tb_wttb_qlist a1 
            LEFT JOIN tb_hcqy b1 ON a1.xzqdm = b1.xdm
            LEFT JOIN tb_wttb_hccg c1 ON a1.tbbsm = c1.tbbsm
            WHERE a1.xzqdm LIKE '%s%%'
            GROUP BY xdm,xmc ORDER BY xdm DESC) a
            LEFT JOIN (
            SELECT xdm,xmc,COUNT(*) zs FROM tb_wttb_qlist a1 
            LEFT JOIN tb_hcqy b1 ON a1.xzqdm = b1.xdm
            LEFT JOIN tb_wttb_hccg c1 ON a1.tbbsm = c1.tbbsm
            WHERE a1.xzqdm LIKE '%s%%' AND a1.wyzt = 'Y'
            GROUP BY xdm,xmc ORDER BY xdm DESC) b ON a.xdm = b.xdm
            LEFT JOIN (
            SELECT xdm,xmc,COUNT(*) zs FROM tb_wttb_qlist a1 
            LEFT JOIN tb_hcqy b1 ON a1.xzqdm = b1.xdm
            LEFT JOIN tb_wttb_hccg c1 ON c1.tbbsm = a1.tbbsm
            WHERE a1.xzqdm LIKE '%s%%' AND a1.shzt = 'P' AND a1.nodeid = '1'
            GROUP BY xdm,xmc ORDER BY xdm DESC) f ON a.xdm = f.xdm
            LEFT JOIN (
            SELECT xdm,xmc,COUNT(*) zs FROM tb_wttb_qlist a1 
            LEFT JOIN tb_hcqy b1 ON a1.xzqdm = b1.xdm
            LEFT JOIN tb_wttb_hccg c1 ON c1.tbbsm = a1.tbbsm
            WHERE a1.xzqdm LIKE '%s%%' AND a1.shzt = 'T' AND a1.nodeid = '1'
            GROUP BY xdm,xmc ORDER BY xdm DESC) g ON a.xdm = g.xdm
            LEFT JOIN (
            SELECT xdm,xmc,COUNT(*) zs FROM tb_wttb_qlist a1 
            LEFT JOIN tb_hcqy b1 ON a1.xzqdm = b1.xdm
            LEFT JOIN tb_wttb_hccg c1 ON a1.tbbsm = c1.tbbsm
            WHERE a1.xzqdm LIKE '%s%%' AND a1.shzt = 'P' AND a1.nodeid = '2'
            GROUP BY xdm,xmc ORDER BY xdm DESC) h ON a.xdm = h.xdm
            LEFT JOIN (
            SELECT xdm,xmc,COUNT(*) zs FROM tb_wttb_qlist a1 
            LEFT JOIN tb_hcqy b1 ON a1.xzqdm = b1.xdm
            LEFT JOIN tb_wttb_hccg c1 ON c1.tbbsm = a1.tbbsm
            WHERE a1.xzqdm LIKE '%s%%' AND a1.shzt = 'T' AND a1.nodeid = '2'
            GROUP BY xdm,xmc ORDER BY xdm DESC) i ON a.xdm = i.xdm
            LEFT JOIN (
            SELECT xdm,xmc,COUNT(*) zs FROM tb_wttb_qlist a1 
            LEFT JOIN tb_hcqy b1 ON a1.xzqdm = b1.xdm
            LEFT JOIN tb_wttb_hccg c1 ON c1.tbbsm = a1.tbbsm
            WHERE a1.xzqdm LIKE '%s%%' AND a1.shzt = 'P' AND a1.nodeid = '3'
            GROUP BY xdm,xmc ORDER BY xdm DESC) j ON a.xdm = j.xdm
            LEFT JOIN (
            SELECT xdm,xmc,COUNT(*) zs FROM tb_wttb_qlist a1 
            LEFT JOIN tb_hcqy b1 ON a1.xzqdm = b1.xdm
            LEFT JOIN tb_wttb_hccg c1 ON c1.tbbsm = a1.tbbsm
            WHERE a1.xzqdm LIKE '%s%%' AND a1.shzt = 'T' AND a1.nodeid = '3'
            GROUP BY xdm,xmc ORDER BY xdm DESC) k ON a.xdm = k.xdm
            LEFT JOIN (
            SELECT xdm,xmc,COUNT(*) zs FROM tb_wtfw_qlist d1 
            LEFT JOIN tb_hcqy b1 ON d1.xzqdm = b1.xdm
            LEFT JOIN tb_wtfw_hccg e1 ON d1.tbbsm = e1.tbbsm
            WHERE d1.xzqdm LIKE '%s%%'
            GROUP BY xdm,xmc ORDER BY xdm DESC) c ON a.xdm = c.xdm
            LEFT JOIN (
            SELECT xdm,xmc,COUNT(*) zs FROM tb_wtfw_qlist d1 
            LEFT JOIN tb_hcqy b1 ON d1.xzqdm = b1.xdm
            LEFT JOIN tb_wtfw_hccg e1 ON d1.tbbsm = e1.tbbsm
            WHERE d1.xzqdm LIKE '%s%%' AND d1.wyzt = 'Y'
            GROUP BY xdm,xmc ORDER BY xdm DESC) d ON a.xdm = d.xdm
            LEFT JOIN (
            SELECT xdm,xmc,COUNT(*) zs FROM tb_wtfw_qlist d1 
            LEFT JOIN tb_hcqy b1 ON d1.xzqdm = b1.xdm
            LEFT JOIN tb_wtfw_hccg e1 ON d1.tbbsm = e1.tbbsm
            WHERE d1.xzqdm LIKE '%s%%' AND e1.kgsj IS NOT NULL
            AND e1.tdly IS NOT NULL AND e1.zymj IS NOT NULL 
            AND e1.zygdmj IS NOT NULL AND e1.sffhcxgh IS NOT NULL 
            GROUP BY xdm,xmc ORDER BY xdm DESC) l ON a.xdm = l.xdm
    """ % (code, code, code, code, code, code, code, code, code, code, code)

    cur1 = connection.cursor()
    cur2 = connection.cursor()
    cur3 = connection.cursor()
    cur4 = connection.cursor()
    cur5 = connection.cursor()
    cur6 = connection.cursor()

    cur1.execute(sql1)
    cur2.execute(sql2)
    cur3.execute(sql3)
    cur4.execute(sql4)
    cur5.execute(sql5)
    cur6.execute(sql6)

    # 获取结果集的每一行,sql查询的值
    rows1 = cur1.fetchall()
    rows2 = cur2.fetchall()
    rows3 = cur3.fetchall()
    rows4 = cur4.fetchall()
    rows5 = cur5.fetchall()
    rows6 = cur6.fetchall()

    # 获取所有字段名
    all_fields1 = cur1.description
    all_fields2 = cur2.description
    all_fields3 = cur3.description
    all_fields4 = cur4.description
    all_fields5 = cur5.description
    all_fields6 = cur6.description

    # 存储字段名的列表
    field_messages1 = []
    field_messages2 = []
    field_messages3 = []
    field_messages4 = []
    field_messages5 = []
    field_messages6 = []

    # 遍历sql1执行的数据
    rows1 = rows1[0]

    for i in range(len(all_fields1)):
        # 格式化输出结果，len参数是各列的显示宽度，可以指定常量，也可自定义函数进行获取。
        field_messages1.append("{str:<{len}}".format(str=str(all_fields1[i][0]), len=0))

    for i in range(len(all_fields2)):
        # 格式化输出结果，len参数是各列的显示宽度，可以指定常量，也可自定义函数进行获取。
        field_messages2.append("{str:<{len}}".format(str=str(all_fields2[i][0]), len=0))

    for i in range(len(all_fields3)):
        # 格式化输出结果，len参数是各列的显示宽度，可以指定常量，也可自定义函数进行获取。
        field_messages3.append("{str:<{len}}".format(str=str(all_fields3[i][0]), len=0))

    for i in range(len(all_fields4)):
        # 格式化输出结果，len参数是各列的显示宽度，可以指定常量，也可自定义函数进行获取。
        field_messages4.append("{str:<{len}}".format(str=str(all_fields4[i][0]), len=0))

    for i in range(len(all_fields5)):
        # 格式化输出结果，len参数是各列的显示宽度，可以指定常量，也可自定义函数进行获取。
        field_messages5.append("{str:<{len}}".format(str=str(all_fields5[i][0]), len=0))

    for i in range(len(all_fields6)):
        # 格式化输出结果，len参数是各列的显示宽度，可以指定常量，也可自定义函数进行获取。
        field_messages6.append("{str:<{len}}".format(str=str(all_fields6[i][0]), len=0))

    # 定义模板样式
    data1 = [
        ['序号', '类型', '个数', '占用土地面积（亩）', '占用耕地面积（亩）', '占用永久基本农田面积（亩）'],
        [1, field_messages1[0], rows1[0], rows1[5], rows1[10], rows1[15]],
        [2, field_messages1[1], rows1[1], rows1[6], rows1[11], rows1[16]],
        [3, field_messages1[2], rows1[2], rows1[7], rows1[12], rows1[17]],
        [4, field_messages1[3], rows1[3], rows1[8], rows1[13], rows1[18]],
        ['小计', '', rows1[4], rows1[9], rows1[14], rows1[19]]
    ]

    data2 = [
        ['排序', '行政区', '采集分类', '摸排房屋数量（个）'],
    ]

    data3 = [
        ['排序', '行政区', '采集分类', '摸排房屋数量（个）'],
    ]

    data4 = [
        ['市名称', '下发图斑', '下发图斑', '下发图斑', '下发图斑', '摸排房屋', '摸排房屋', '摸排房屋'],
        ['市名称', '总图斑', '属于摸排范围', '已外业', '已审核', '总图斑', '已外业', '已审核'],
    ]

    data5 = [
        ['全省农村乱占耕地建房问题摸排情况统计表'],
        ['面积单位：公顷'],
        ['序号', '区县代码', '行政名称',
         '县级工作底图（上传摸排系统图斑）', '县级工作底图（上传摸排系统图斑）', '县级工作底图（上传摸排系统图斑）',
         '已完成外业摸排', '已完成外业摸排', '已完成外业摸排',
         '县级核查意见为有问题即认定为违法', '县级核查意见为有问题即认定为违法', '县级核查意见为有问题即认定为违法', '县级核查意见为有问题即认定为违法',
         '', '', '', '',
         '县级核查意见为有问题即认定为违法', '县级核查意见为有问题即认定为违法', '县级核查意见为有问题即认定为违法', '县级核查意见为有问题即认定为违法',
         '县级核查意见为有问题即认定为违法', '县级核查意见为有问题即认定为违法', '县级核查意见为有问题即认定为违法', '县级核查意见为有问题即认定为违法',
         '县级核查意见为有问题即认定为违法', '县级核查意见为有问题即认定为违法', '县级核查意见为有问题即认定为违法', '县级核查意见为有问题即认定为违法',
         '县级核查意见为有问题即认定为违法', '县级核查意见为有问题即认定为违法', '县级核查意见为有问题即认定为违法', '县级核查意见为有问题即认定为违法',
         '县级核查意见为存疑即已摸排未明确意见', '县级核查意见为存疑即已摸排未明确意见', '县级核查意见为存疑即已摸排未明确意见',
         '县级核查意见为无问题即认定为合法', '县级核查意见为无问题即认定为合法', '县级核查意见为无问题即认定为合法',
         '已完成外业但县级无审核意见', '已完成外业但县级无审核意见', '已完成外业但县级无审核意见',
         ],
        ['序号', '区县代码', '行政区代码',
         '县级工作底图（上传摸排系统图斑）', '县级工作底图（上传摸排系统图斑）', '县级工作底图（上传摸排系统图斑）',
         '已完成外业摸排', '已完成外业摸排', '已完成外业摸排',
         '合计', '合计', '合计', '合计',
         '住宅类', '住宅类', '住宅类', '住宅类',
         '其中单户住宅', '其中单户住宅', '其中单户住宅', '其中单户住宅',
         '其中多户住宅', '其中多户住宅', '其中多户住宅', '其中多户住宅',
         '管理类', '管理类', '管理类', '管理类',
         '产业类', '产业类', '产业类', '产业类',
         '县级核查意见为存疑即已摸排未明确意见', '县级核查意见为存疑即已摸排未明确意见', '县级核查意见为存疑即已摸排未明确意见',
         '县级核查意见为无问题即认定为合法', '县级核查意见为无问题即认定为合法', '县级核查意见为无问题即认定为合法',
         '已完成外业但县级无审核意见', '已完成外业但县级无审核意见', '已完成外业但县级无审核意见',
         ],
        ['序号', '区县代码', '行政名称',
         '图斑个数', '图斑面积', '占耕地面积',
         '图斑个数', '图斑面积', '占耕地面积', '个数占工作地图比例',
         '个数', '图斑面积', '占耕地面积', '占基本农田面积',
         '个数', '图斑面积', '占耕地面积', '占基本农田面积',
         '个数', '图斑面积', '占耕地面积', '占基本农田面积',
         '图斑个数', '图斑面积', '占耕地面积', '占基本农田面积',
         '图斑个数', '图斑面积', '占耕地面积', '占基本农田面积',
         '图斑个数', '图斑面积', '占耕地面积', '占基本农田面积',
         '图斑个数', '图斑面积', '占耕地面积',
         '图斑个数', '图斑面积', '占耕地面积',
         '图斑个数', '图斑面积', '占耕地面积',
         ],
    ]

    data6 = [
        ['县代码', '县名称', '下发图斑数量', '下发图斑已外业', '摸排房屋数量', '摸排房屋已外业', '内业填报数',
         '县级已审核', '县级未审核', '县级审核占比', '市级已审核', '市级未审核', '省级已审核', '省级未审核']
    ]

    # 将数据库表字段插入表格
    for j in range(len(rows2)):
        list1 = [
            j + 1, rows2[j][2], field_messages2[3], rows2[j][3],
        ]
        list2 = [
            j + 2, rows2[j][2], field_messages2[4], rows2[j][4],
        ]
        list3 = [
            j + 3, rows2[j][2], field_messages2[5], rows2[j][5],
        ]
        list4 = [
            j + 4, rows2[j][2], field_messages2[6], rows2[j][6],
        ]
        list5 = [
            j + 5, rows2[j][2], field_messages2[7], rows2[j][7],
        ]
        data2.append(list1)
        data2.append(list2)
        data2.append(list3)
        data2.append(list4)
        data2.append(list5)

    for j in range(len(rows3)):
        list1 = [
            j + 1, rows3[j][3], field_messages3[5], rows3[j][5],
        ]
        list2 = [
            j + 2, rows3[j][3], field_messages3[6], rows3[j][6],
        ]
        list3 = [
            j + 3, rows3[j][3], field_messages3[7], rows3[j][7],
        ]
        list4 = [
            j + 4, rows3[j][3], field_messages3[8], rows3[j][8],
        ]
        list5 = [
            j + 5, rows3[j][3], field_messages3[9], rows3[j][9],
        ]
        data3.append(list1)
        data3.append(list2)
        data3.append(list3)
        data3.append(list4)
        data3.append(list5)

    for j in range(len(rows4)):
        list1 = [
            rows4[j][0], rows4[j][1], rows4[j][2], rows4[j][3],
            rows4[j][4], rows4[j][5], rows4[j][6], rows4[j][7]
        ]
        data4.append(list1)

    for j in range(len(rows5)):
        list1 = [
            j + 1, rows5[j][0], rows5[j][1], rows5[j][2], rows5[j][3], rows5[j][4], rows5[j][5], rows5[j][6],
            rows5[j][7], rows5[j][8], rows5[j][9], rows5[j][10], rows5[j][11], rows5[j][12], rows5[j][13],
            rows5[j][14], rows5[j][15], rows5[j][16], rows5[j][17], rows5[j][18], rows5[j][19], rows5[j][20],
            rows5[j][21], rows5[j][22], rows5[j][23], rows5[j][24], rows5[j][25], rows5[j][26], rows5[j][27],
            rows5[j][28], rows5[j][29], rows5[j][30], rows5[j][31], rows5[j][32], rows5[j][33], rows5[j][34],
            rows5[j][35], rows5[j][36], rows5[j][37], rows5[j][38], rows5[j][39], rows5[j][40], rows5[j][41],
        ]
        data5.append(list1)

    for j in range(len(rows6)):
        list1 = [
            rows6[j][0], rows6[j][1], rows6[j][2], rows6[j][3], rows6[j][4], rows6[j][5], rows6[j][6],
            rows6[j][7], rows6[j][8], rows6[j][9], rows6[j][10], rows6[j][11], rows6[j][12], rows6[j][13],
        ]
        data6.append(list1)

    header = {
        'bold': True,  # 粗体
        'font_name': '仿宋',
        'font_size': 10,
        'border': True,  # 边框线
        'align': 'center',  # 水平居中
        'valign': 'vcenter',  # 垂直居中
        # 'bg_color': '#66DD00'  # 背景颜色
    }

    text = {
        'align': 'center',
        'valign': 'vcenter',
        'font_name': '仿宋',
        'font_size': 11,
        'border': 1,
    }

    with xlsxwriter.Workbook('测试乱占耕地.xlsx') as workbook1:
        worksheet1 = workbook1.add_worksheet('汇总')
        worksheet2 = workbook1.add_worksheet('分市')
        worksheet3 = workbook1.add_worksheet('分县')
        worksheet4 = workbook1.add_worksheet('外业')
        worksheet5 = workbook1.add_worksheet('四川')
        worksheet6 = workbook1.add_worksheet('福建')

        headerpm = workbook1.add_format(header)
        textpm = workbook1.add_format(text)

        # 工作薄一样式设置
        worksheet1.set_column('A:C', 17)  # 列宽17
        worksheet1.set_column('D:F', 36)  # 列宽35
        worksheet1.merge_range(5, 0, 5, 1, '小计')

        for row1, rowdata1 in enumerate(data1):
            for col1, coldata1 in enumerate(rowdata1):
                if row1 == 0:
                    worksheet1.write(row1, col1, coldata1, headerpm)
                else:
                    worksheet1.write(row1, col1, coldata1, textpm)

        # 工作薄二样式设置
        worksheet2.set_column('A:C', 17)  # 列宽17
        worksheet2.set_column('D:D', 25)  # 列宽25

        for i in range(0, len(rows2) * 5, 5):
            worksheet2.merge_range(i + 1, 0, i + 5, 0, +1)
            worksheet2.merge_range(i + 1, 1, i + 5, 1, None)

        for row2, rowdata2 in enumerate(data2):
            for col2, coldata2 in enumerate(rowdata2):
                if row2 == 0:
                    worksheet2.write(row2, col2, coldata2, headerpm)
                else:
                    worksheet2.write(row2, col2, coldata2, textpm)

        # 工作薄三样式设置
        worksheet3.set_column('A:C', 17)  # 列宽17
        worksheet3.set_column('D:D', 25)  # 列宽25

        for i in range(0, len(rows3) * 5, 5):
            worksheet3.merge_range(i + 1, 0, i + 5, 0, +1)
            worksheet3.merge_range(i + 1, 1, i + 5, 1, None)

        for row3, rowdata3 in enumerate(data3):
            for col3, coldata3 in enumerate(rowdata3):
                if row3 == 0:
                    worksheet3.write(row3, col3, coldata3, headerpm)
                else:
                    worksheet3.write(row3, col3, coldata3, textpm)

        # 工作薄四样式设置
        worksheet4.set_column('A:H', 18)  # 列宽17

        worksheet4.merge_range(0, 0, 1, 0, None)
        worksheet4.merge_range(0, 1, 0, 4, None)
        worksheet4.merge_range(0, 5, 0, 7, None)

        for row4, rowdata4 in enumerate(data4):
            for col4, coldata4 in enumerate(rowdata4):
                if row4 == 0:
                    worksheet4.write(row4, col4, coldata4, headerpm)
                else:
                    worksheet4.write(row4, col4, coldata4, textpm)

        # 工作薄五样式设置
        worksheet5.set_row(4, 36)  # 设置第5行行高36
        # 前面是行，后面是列
        worksheet5.merge_range(0, 0, 0, 42, None)
        worksheet5.merge_range(1, 0, 1, 42, None)

        # 序号，区县代码，行政代码
        worksheet5.merge_range(2, 0, 4, 0, None)
        worksheet5.merge_range(2, 1, 4, 1, None)
        worksheet5.merge_range(2, 2, 4, 2, None)

        # 县级工作底图（上传摸排系统图斑）
        worksheet5.merge_range(2, 3, 3, 5, None)
        # 已完成外业摸排
        worksheet5.merge_range(2, 6, 3, 9, None)
        # 县级核查意见为有问题即认定为违法
        worksheet5.merge_range(2, 10, 2, 33, None)
        # 县级核查意见为存疑即已摸排未明确意见
        worksheet5.merge_range(2, 34, 3, 36, None)
        # 县级核查意见为无问题即认定为合法
        worksheet5.merge_range(2, 37, 3, 39, None)
        # 已完成外业但县级无审核意见
        worksheet5.merge_range(2, 40, 3, 42, None)
        # 合计
        worksheet5.merge_range(3, 10, 3, 13, None)
        # 住宅类
        worksheet5.merge_range(3, 14, 3, 17, None)
        # 其中单户住宅
        worksheet5.merge_range(3, 18, 3, 21, None)
        # 其中多户住宅
        worksheet5.merge_range(3, 22, 3, 25, None)
        # 管理类
        worksheet5.merge_range(3, 26, 3, 29, None)
        # 产业类
        worksheet5.merge_range(3, 30, 3, 33, None)

        for row5, rowdata5 in enumerate(data5):
            for col5, coldata5 in enumerate(rowdata5):
                if row5 == 0:
                    worksheet5.write(row5, col5, coldata5, headerpm)
                else:
                    worksheet5.write(row5, col5, coldata5, textpm)

        for row6, rowdata6 in enumerate(data6):
            for col6, coldata6 in enumerate(rowdata6):
                if row6 == 0:
                    worksheet6.write(row6, col6, coldata6, headerpm)
                else:
                    worksheet6.write(row6, col6, coldata6, textpm)

    response = FileResponse(open('测试乱占耕地.xlsx', 'rb'))
    response['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    response['Content-Disposition'] = 'attachment;filename="测试乱占耕地.xlsx"'
    return response
