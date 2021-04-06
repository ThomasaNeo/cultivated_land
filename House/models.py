# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TbUserpower(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    stime = models.DateTimeField(blank=True, null=True)
    suser = models.CharField(max_length=50, blank=True, null=True)
    type = models.BigIntegerField(blank=True, null=True)
    powercode = models.CharField(max_length=2000, blank=True, null=True)
    cfgtype = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_userpower'


class TbUserrole(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True)
    rcode = models.CharField(max_length=50, blank=True, null=True)
    stime = models.DateTimeField(blank=True, null=True)
    suser = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_userrole'


class TbUsers(models.Model):
    bsm = models.BigIntegerField()
    username = models.CharField(max_length=50, blank=True, null=True)
    userpass = models.CharField(max_length=50, blank=True, null=True)
    userphone = models.CharField(max_length=20, blank=True, null=True)
    usertime = models.DateTimeField(blank=True, null=True)
    useremail = models.CharField(max_length=50, blank=True, null=True)
    userenabled = models.BigIntegerField(blank=True, null=True)
    isadmin = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    ssbm = models.CharField(max_length=50, blank=True, null=True)
    zw = models.CharField(max_length=50, blank=True, null=True)
    sf = models.CharField(max_length=50, blank=True, null=True)
    cancheck = models.BigIntegerField(blank=True, null=True)
    loginstate = models.CharField(max_length=10, blank=True, null=True)
    reporttime = models.DateTimeField(blank=True, null=True)
    loginmac = models.CharField(max_length=50, blank=True, null=True)
    loginip = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_users'


class TbWebApp(models.Model):
    bsm = models.BigIntegerField(primary_key=True)
    webuserbsm = models.BigIntegerField()
    appuserbsm = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tb_web_app'


class TbWeblog(models.Model):
    bsm = models.BigIntegerField()
    xzqdm = models.BigIntegerField()
    xzqmc = models.CharField(max_length=150, blank=True, null=True)
    modulename = models.CharField(max_length=150, blank=True, null=True)
    functionname = models.CharField(max_length=150, blank=True, null=True)
    operating = models.CharField(max_length=150, blank=True, null=True)
    createtime = models.DateTimeField()
    remark = models.CharField(max_length=2000, blank=True, null=True)
    ip = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_weblog'


class TbWebuser(models.Model):
    xzqdm = models.CharField(max_length=50, blank=True, null=True)
    xzqmc = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    changedpwd = models.BigIntegerField(blank=True, null=True)
    bsm = models.BigIntegerField(primary_key=True)
    userid = models.CharField(unique=True, max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    ssgxq = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(unique=True, max_length=18, blank=True, null=True)
    datapowertype = models.BigIntegerField(blank=True, null=True)
    state = models.BigIntegerField(blank=True, null=True)
    isadmin = models.BigIntegerField(blank=True, null=True)
    unittypecode = models.CharField(max_length=50, blank=True, null=True)
    unitname = models.CharField(max_length=200, blank=True, null=True)
    usertitle = models.CharField(max_length=100, blank=True, null=True)
    bz = models.CharField(max_length=1000, blank=True, null=True)
    syncstatus = models.BigIntegerField(blank=True, null=True)
    synctime = models.DateTimeField(blank=True, null=True)
    gtdcy_open = models.BigIntegerField(blank=True, null=True)
    gtdcy_erorr = models.CharField(max_length=500, blank=True, null=True)
    jwusertype = models.BigIntegerField(blank=True, null=True)
    menu = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_webuser'


class TbWebuserXzqdm(models.Model):
    bsm = models.BigIntegerField(primary_key=True)
    webuserbsm = models.BigIntegerField()
    xzqdmlevel = models.BigIntegerField()
    xzqdm = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_webuser_xzqdm'


class TbWtfw(models.Model):
    bsm = models.IntegerField(primary_key=True)
    xzqmc = models.CharField(max_length=200, blank=True, null=True)
    xzqdm = models.CharField(max_length=200, blank=True, null=True)
    xzmc = models.CharField(max_length=200, blank=True, null=True)
    xzdm = models.CharField(max_length=200, blank=True, null=True)
    xzjbdm = models.CharField(max_length=20)
    tbbsm = models.CharField(unique=True, max_length=200)
    reltbbsm = models.CharField(max_length=200, blank=True, null=True)
    zdsxh = models.CharField(max_length=200, blank=True, null=True)
    relzdsxh = models.CharField(max_length=200, blank=True, null=True)
    tbmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shapearea = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    jzzmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    zlwz = models.CharField(max_length=200, blank=True, null=True)
    ztlx = models.CharField(max_length=10, blank=True, null=True)
    fzzt = models.CharField(max_length=10, blank=True, null=True)
    zdlx = models.CharField(max_length=10, blank=True, null=True)
    ydspqk = models.CharField(max_length=50, blank=True, null=True)
    ghqk = models.CharField(max_length=50, blank=True, null=True)
    ztxq = models.CharField(max_length=100, blank=True, null=True)
    ztmc = models.CharField(max_length=100, blank=True, null=True)
    jslx = models.CharField(max_length=50, blank=True, null=True)
    jssj = models.DateTimeField(blank=True, null=True)
    zydl = models.CharField(max_length=10, blank=True, null=True)
    sjpc = models.CharField(max_length=64, blank=True, null=True)
    bz = models.CharField(max_length=500, blank=True, null=True)
    x = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    y = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    minx = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    miny = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    maxx = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    maxy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    xmzt = models.IntegerField(blank=True, null=True)
    sjly = models.CharField(max_length=10, blank=True, null=True)
    shape = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=10, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    createname = models.CharField(max_length=100, blank=True, null=True)
    modifytime = models.DateTimeField()
    modifyname = models.CharField(max_length=100, blank=True, null=True)
    cloudid = models.CharField(max_length=200, blank=True, null=True)
    sjtgf = models.CharField(max_length=100, blank=True, null=True)
    cloudresultid = models.CharField(max_length=200, blank=True, null=True)
    cloudquerytime = models.CharField(max_length=200, blank=True, null=True)
    cloudresultdb = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wtfw'


class TbWtfwChildXmbhs(models.Model):
    bsm = models.IntegerField(primary_key=True)
    xzqdm = models.CharField(max_length=16, blank=True, null=True)
    symbol = models.CharField(max_length=200, blank=True, null=True)
    serial = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    xmbh = models.CharField(max_length=64, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wtfw_child_xmbhs'


class TbWtfwCqat(models.Model):
    bsm = models.IntegerField(primary_key=True)
    analyzetype = models.CharField(max_length=50, blank=True, null=True)
    analyzetypename = models.CharField(max_length=50, blank=True, null=True)
    analyzeshowname = models.CharField(max_length=50, blank=True, null=True)
    tag = models.CharField(max_length=200, blank=True, null=True)
    ordernumber = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tb_wtfw_cqat'


class TbWtfwDellog(models.Model):
    bsm = models.IntegerField(primary_key=True)
    xzqdm = models.CharField(max_length=10)
    tbbsm = models.CharField(max_length=50)
    xzjbdm = models.CharField(max_length=10)
    userid = models.CharField(max_length=10)
    ywlx = models.CharField(max_length=50)
    deletetime = models.DateTimeField(blank=True, null=True)
    xmbh = models.CharField(max_length=100, blank=True, null=True)
    xmmc = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wtfw_dellog'


class TbWtfwDownloadlog(models.Model):
    bsm = models.IntegerField(primary_key=True)
    xzqdm = models.CharField(max_length=20)
    logbsm = models.CharField(max_length=100)
    cjry = models.CharField(max_length=200)
    cjlx = models.IntegerField()
    cjnr = models.CharField(max_length=2000, blank=True, null=True)
    cjsj = models.DateTimeField()
    cjrymc = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wtfw_downloadlog'


class TbWtfwHccg(models.Model):
    bsm = models.IntegerField(primary_key=True)
    xzqdm = models.CharField(max_length=10)
    tbbsm = models.CharField(unique=True, max_length=50)
    fwbh = models.CharField(max_length=50, blank=True, null=True)
    fwzl = models.CharField(max_length=200, blank=True, null=True)
    sfzqczzfw = models.CharField(max_length=200, blank=True, null=True)
    fwlx = models.CharField(max_length=50, blank=True, null=True)
    zzfwwfwlx = models.CharField(max_length=50, blank=True, null=True)
    zzlsfsj = models.CharField(max_length=10, blank=True, null=True)
    cylsfsj = models.CharField(max_length=10, blank=True, null=True)
    gglsfsj = models.CharField(max_length=10, blank=True, null=True)
    fwlb = models.CharField(max_length=10, blank=True, null=True)
    tdly = models.CharField(max_length=10, blank=True, null=True)
    jfyy = models.CharField(max_length=10, blank=True, null=True)
    fwjsyj = models.CharField(max_length=200, blank=True, null=True)
    xmzgbm = models.CharField(max_length=200, blank=True, null=True)
    jszt = models.CharField(max_length=50, blank=True, null=True)
    jsztxz = models.CharField(max_length=50, blank=True, null=True)
    tyshxydm = models.CharField(max_length=200, blank=True, null=True)
    jszjly = models.CharField(max_length=50, blank=True, null=True)
    frdb = models.CharField(max_length=20, blank=True, null=True)
    sfzh = models.CharField(max_length=50, blank=True, null=True)
    fwjzmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cs = models.CharField(max_length=10, blank=True, null=True)
    jsqk = models.CharField(max_length=10, blank=True, null=True)
    kgsj = models.DateTimeField(blank=True, null=True)
    jgsj = models.DateTimeField(blank=True, null=True)
    fwsyqk = models.CharField(max_length=50, blank=True, null=True)
    fwjtyt = models.CharField(max_length=100, blank=True, null=True)
    mz = models.CharField(max_length=20, blank=True, null=True)
    zy = models.CharField(max_length=20, blank=True, null=True)
    sjh = models.CharField(max_length=50, blank=True, null=True)
    zzmm = models.CharField(max_length=10, blank=True, null=True)
    sfbcm = models.CharField(max_length=10, blank=True, null=True)
    sfyhyz = models.CharField(max_length=10, blank=True, null=True)
    bfhyy = models.CharField(max_length=10, blank=True, null=True)
    sffhfhtj = models.CharField(max_length=10, blank=True, null=True)
    syzt = models.CharField(max_length=50, blank=True, null=True)
    syrsfzh = models.CharField(max_length=50, blank=True, null=True)
    syrmz = models.CharField(max_length=20, blank=True, null=True)
    syrzy = models.CharField(max_length=20, blank=True, null=True)
    syrsjh = models.CharField(max_length=50, blank=True, null=True)
    syrzzmm = models.CharField(max_length=10, blank=True, null=True)
    syrsfbcm = models.CharField(max_length=10, blank=True, null=True)
    ztqdfs = models.CharField(max_length=10, blank=True, null=True)
    yjsztgx = models.CharField(max_length=20, blank=True, null=True)
    zymj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    zygdmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    zyjgmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qztdmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qzgdmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qzjgmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    zyjbntmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bdynghsj = models.DateTimeField(blank=True, null=True)
    sfhdynhjf = models.CharField(max_length=10, blank=True, null=True)
    zybhqmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bhqhdsj = models.DateTimeField(blank=True, null=True)
    sfhdbhqhjf = models.CharField(max_length=10, blank=True, null=True)
    zysthxmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sthxsj = models.DateTimeField(blank=True, null=True)
    sfsthxhjf = models.CharField(max_length=10, blank=True, null=True)
    zdsfgh = models.CharField(max_length=10, blank=True, null=True)
    cxghyt = models.CharField(max_length=50, blank=True, null=True)
    sfjsfw = models.CharField(max_length=10, blank=True, null=True)
    sffhtg = models.CharField(max_length=10, blank=True, null=True)
    tgyt = models.CharField(max_length=100, blank=True, null=True)
    sfpdsq = models.CharField(max_length=10, blank=True, null=True)
    sflx = models.CharField(max_length=10, blank=True, null=True)
    sflx_pzjg = models.CharField(max_length=50, blank=True, null=True)
    sflx_pzsj = models.DateTimeField(blank=True, null=True)
    sflx_lxmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sfzjdsp = models.CharField(max_length=10, blank=True, null=True)
    sfzjdsp_pzjg = models.CharField(max_length=50, blank=True, null=True)
    sfzjdsp_pzsj = models.DateTimeField(blank=True, null=True)
    sfzjdsp_pzmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sfbyd = models.CharField(max_length=10, blank=True, null=True)
    sfbyd_pzjg = models.CharField(max_length=50, blank=True, null=True)
    sfbyd_pzsj = models.DateTimeField(blank=True, null=True)
    sfbyd_pzmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sfghxk = models.CharField(max_length=10, blank=True, null=True)
    sfghxk_pzjg = models.CharField(max_length=50, blank=True, null=True)
    sfghxk_pzsj = models.DateTimeField(blank=True, null=True)
    sfghxk_pzmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sfbdcdj = models.CharField(max_length=10, blank=True, null=True)
    zsbh = models.CharField(max_length=50, blank=True, null=True)
    fzsj = models.DateTimeField(blank=True, null=True)
    djmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sfxzcf = models.CharField(max_length=10, blank=True, null=True)
    cfyj = models.CharField(max_length=100, blank=True, null=True)
    sfsqfyqzzx = models.CharField(max_length=10, blank=True, null=True)
    fkje = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sfcdzx = models.CharField(max_length=10, blank=True, null=True)
    fysfsl = models.CharField(max_length=10, blank=True, null=True)
    cfzxqk = models.CharField(max_length=50, blank=True, null=True)
    cdzxzt = models.CharField(max_length=10, blank=True, null=True)
    sfss = models.CharField(max_length=10, blank=True, null=True)
    ssyy = models.CharField(max_length=50, blank=True, null=True)
    bcsm = models.CharField(max_length=500, blank=True, null=True)
    cmqkms = models.CharField(max_length=10, blank=True, null=True)
    wflx = models.CharField(max_length=10, blank=True, null=True)
    tdqdfs = models.CharField(max_length=10, blank=True, null=True)
    cgghzjdmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bzgdjsqzt = models.CharField(max_length=10, blank=True, null=True)
    sfyjjbnt = models.CharField(max_length=10, blank=True, null=True)
    sfwyzrbhq = models.CharField(max_length=10, blank=True, null=True)
    sffhcxgh = models.CharField(max_length=10, blank=True, null=True)
    sffhctdlyqk = models.CharField(max_length=10, blank=True, null=True)
    sfczcs = models.CharField(max_length=10, blank=True, null=True)
    sffp = models.CharField(max_length=10, blank=True, null=True)
    sfczspdz = models.CharField(max_length=10, blank=True, null=True)
    czmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    zzlb = models.CharField(max_length=10, blank=True, null=True)
    sm = models.CharField(max_length=500, blank=True, null=True)
    hcry = models.CharField(max_length=50, blank=True, null=True)
    sign = models.TextField(blank=True, null=True)
    hcsj = models.DateTimeField(blank=True, null=True)
    xzjd = models.CharField(max_length=200, blank=True, null=True)
    csq = models.CharField(max_length=200, blank=True, null=True)
    zu = models.CharField(max_length=200, blank=True, null=True)
    mph = models.CharField(max_length=200, blank=True, null=True)
    xmmc = models.CharField(max_length=200, blank=True, null=True)
    zygdlx = models.CharField(max_length=10, blank=True, null=True)
    ydsxqk = models.CharField(max_length=10, blank=True, null=True)
    myhfhgyy = models.CharField(max_length=10, blank=True, null=True)
    sfsjbmyq = models.CharField(max_length=10, blank=True, null=True)
    lyqk = models.CharField(max_length=10, blank=True, null=True)
    sfhbcyg = models.CharField(max_length=10, blank=True, null=True)
    grxm = models.CharField(max_length=200, blank=True, null=True)
    dwmc = models.CharField(max_length=100, blank=True, null=True)
    jsztmc = models.CharField(max_length=500, blank=True, null=True)
    tbrqm = models.CharField(max_length=500, blank=True, null=True)
    fhrqm = models.CharField(max_length=500, blank=True, null=True)
    shrqm = models.CharField(max_length=500, blank=True, null=True)
    bccmhs = models.IntegerField(blank=True, null=True)
    wccmhs = models.IntegerField(blank=True, null=True)
    czjmhs = models.IntegerField(blank=True, null=True)
    qtcmhs = models.IntegerField(blank=True, null=True)
    hjrs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wtfw_hccg'


class TbWtfwHccgsh(models.Model):
    bsm = models.IntegerField(primary_key=True)
    xzqdm = models.CharField(max_length=10, blank=True, null=True)
    tbbsm = models.CharField(unique=True, max_length=50, blank=True, null=True)
    xjshjg = models.CharField(max_length=10, blank=True, null=True)
    xjshsj = models.DateTimeField(blank=True, null=True)
    xjshry = models.CharField(max_length=50, blank=True, null=True)
    xjshsm = models.CharField(max_length=500, blank=True, null=True)
    cjshjg = models.CharField(max_length=10, blank=True, null=True)
    cjshsj = models.DateTimeField(blank=True, null=True)
    cjshry = models.CharField(max_length=50, blank=True, null=True)
    cjshsm = models.CharField(max_length=500, blank=True, null=True)
    sjshjg = models.CharField(max_length=10, blank=True, null=True)
    sjshsj = models.DateTimeField(blank=True, null=True)
    sjshry = models.CharField(max_length=50, blank=True, null=True)
    sjshsm = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wtfw_hccgsh'


class TbWtfwHccgshjl(models.Model):
    bsm = models.IntegerField(primary_key=True)
    xzqdm = models.CharField(max_length=10)
    tbbsm = models.CharField(max_length=50)
    shsm = models.CharField(max_length=1000, blank=True, null=True)
    shry = models.CharField(max_length=100, blank=True, null=True)
    shsj = models.CharField(max_length=100, blank=True, null=True)
    auditbsm = models.CharField(max_length=100, blank=True, null=True)
    xjshjg = models.CharField(max_length=10, blank=True, null=True)
    xjshsm = models.CharField(max_length=1000, blank=True, null=True)
    xjshry = models.CharField(max_length=100, blank=True, null=True)
    xjshsj = models.CharField(max_length=100, blank=True, null=True)
    cjshjg = models.CharField(max_length=10, blank=True, null=True)
    cjshsm = models.CharField(max_length=1000, blank=True, null=True)
    cjshry = models.CharField(max_length=100, blank=True, null=True)
    cjshsj = models.CharField(max_length=100, blank=True, null=True)
    sjshjg = models.CharField(max_length=50, blank=True, null=True)
    sjshsm = models.CharField(max_length=1000, blank=True, null=True)
    sjshry = models.CharField(max_length=100, blank=True, null=True)
    sjshsj = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wtfw_hccgshjl'


class TbWtfwHcfj(models.Model):
    bsm = models.IntegerField(primary_key=True)
    xzqdm = models.CharField(max_length=10, blank=True, null=True)
    tbbsm = models.CharField(max_length=50, blank=True, null=True)
    fjmc = models.CharField(max_length=500, blank=True, null=True)
    fjmc2 = models.CharField(max_length=500, blank=True, null=True)
    fjmc3 = models.CharField(max_length=500, blank=True, null=True)
    fjlx = models.CharField(max_length=50, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    points_json = models.TextField(blank=True, null=True)
    fjly = models.CharField(max_length=50, blank=True, null=True)
    createtime1 = models.DateTimeField(blank=True, null=True)
    fjmode = models.CharField(max_length=50, blank=True, null=True)
    arg = models.CharField(max_length=500, blank=True, null=True)
    arg1 = models.CharField(max_length=500, blank=True, null=True)
    fjtype = models.CharField(max_length=5, blank=True, null=True)
    psry = models.CharField(max_length=100, blank=True, null=True)
    angle = models.IntegerField(blank=True, null=True)
    dkid = models.CharField(max_length=100, blank=True, null=True)
    jym = models.TextField(blank=True, null=True)
    x = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    y = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rwhtlysm = models.CharField(max_length=100, blank=True, null=True)
    azimuth = models.IntegerField(blank=True, null=True)
    distance = models.CharField(max_length=100, blank=True, null=True)
    yaw = models.IntegerField(blank=True, null=True)
    roll = models.IntegerField(blank=True, null=True)
    pitch = models.IntegerField(blank=True, null=True)
    height = models.CharField(max_length=100, blank=True, null=True)
    accuracy = models.IntegerField(blank=True, null=True)
    lysb = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wtfw_hcfj'


class TbWtfwLog(models.Model):
    bsm = models.IntegerField(primary_key=True)
    sjbh = models.CharField(max_length=50)
    tbbsm = models.CharField(max_length=50)
    czry = models.CharField(max_length=10)
    czrymc = models.CharField(max_length=50, blank=True, null=True)
    czlx = models.CharField(max_length=5)
    cznr = models.CharField(max_length=20, blank=True, null=True)
    czsj = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tb_wtfw_log'


class TbWtfwQlist(models.Model):
    xzqdm = models.CharField(max_length=200, blank=True, null=True)
    bsm = models.IntegerField(primary_key=True)
    tbbsm = models.CharField(max_length=200, blank=True, null=True)
    zlwz = models.CharField(max_length=200, blank=True, null=True)
    xmbh = models.CharField(max_length=200, blank=True, null=True)
    xmmc = models.CharField(max_length=200, blank=True, null=True)
    xzjbdm = models.CharField(max_length=20, blank=True, null=True)
    zdsxh = models.CharField(max_length=200, blank=True, null=True)
    tbmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sjly = models.CharField(max_length=10, blank=True, null=True)
    ydspqk = models.CharField(max_length=50, blank=True, null=True)
    ghqk = models.CharField(max_length=50, blank=True, null=True)
    ztlx = models.CharField(max_length=10, blank=True, null=True)
    ztmc = models.CharField(max_length=100, blank=True, null=True)
    ztxq = models.CharField(max_length=100, blank=True, null=True)
    jslx = models.CharField(max_length=50, blank=True, null=True)
    jssj = models.DateTimeField(blank=True, null=True)
    zydl = models.CharField(max_length=10, blank=True, null=True)
    bz = models.CharField(max_length=500, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cloudid = models.CharField(max_length=200, blank=True, null=True)
    cloudresultid = models.CharField(max_length=200, blank=True, null=True)
    reltbbsm = models.CharField(max_length=200, blank=True, null=True)
    relzdsxh = models.CharField(max_length=200, blank=True, null=True)
    wyzt = models.TextField(blank=True, null=True)
    xjshjg = models.CharField(max_length=10, blank=True, null=True)
    optype = models.TextField(blank=True, null=True)
    sjshjg = models.CharField(max_length=10, blank=True, null=True)
    cjshjg = models.CharField(max_length=10, blank=True, null=True)
    flowid = models.BigIntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    nodeid = models.BigIntegerField(blank=True, null=True)
    workstate = models.IntegerField(blank=True, null=True)
    shzt = models.TextField(blank=True, null=True)
    fzzt = models.CharField(max_length=1, blank=True, null=True)
    zdlx = models.CharField(max_length=10, blank=True, null=True)
    xzdm = models.CharField(max_length=200, blank=True, null=True)
    xzmc = models.CharField(max_length=50, blank=True, null=True)
    fwzl = models.CharField(max_length=200, blank=True, null=True)
    sfsj = models.TextField(blank=True, null=True)
    fwlb = models.CharField(max_length=10, blank=True, null=True)
    fwlx = models.CharField(max_length=50, blank=True, null=True)
    tdly = models.CharField(max_length=10, blank=True, null=True)
    jfyy = models.CharField(max_length=1, blank=True, null=True)
    jsztmc = models.CharField(max_length=1, blank=True, null=True)
    zygdlx = models.CharField(max_length=10, blank=True, null=True)
    fwjsyj = models.CharField(max_length=200, blank=True, null=True)
    jszt = models.CharField(max_length=50, blank=True, null=True)
    syzt = models.CharField(max_length=50, blank=True, null=True)
    fwsyqk = models.CharField(max_length=50, blank=True, null=True)
    fwjzmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sfzyjbnt = models.TextField(blank=True, null=True)
    sfzygd = models.TextField(blank=True, null=True)
    sfzqczzfw = models.CharField(max_length=200, blank=True, null=True)
    ffzt = models.TextField(blank=True, null=True)
    pic = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wtfw_qlist'


class TbWtfwRwfp(models.Model):
    bsm = models.IntegerField(primary_key=True)
    xzqdm = models.CharField(max_length=10, blank=True, null=True)
    tbbsm = models.CharField(max_length=100, blank=True, null=True)
    subtaskid = models.IntegerField(blank=True, null=True)
    sbbsm = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wtfw_rwfp'


class TbWtfwRwfpJw(models.Model):
    bsm = models.IntegerField(primary_key=True)
    xzqdm = models.CharField(max_length=10, blank=True, null=True)
    tbbsm = models.CharField(max_length=100, blank=True, null=True)
    subtaskid = models.IntegerField(blank=True, null=True)
    sbbsm = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wtfw_rwfp_jw'


class TbWtfwTbzt(models.Model):
    bsm = models.IntegerField(primary_key=True)
    tbbsm = models.CharField(max_length=50)
    xzqdm = models.CharField(max_length=10)
    tbzt = models.CharField(max_length=10, blank=True, null=True)
    jzsbbsm = models.CharField(max_length=20, blank=True, null=True)
    xjqr = models.IntegerField(blank=True, null=True)
    qrry = models.CharField(max_length=200, blank=True, null=True)
    qrsj = models.DateTimeField(blank=True, null=True)
    sbry = models.CharField(max_length=200, blank=True, null=True)
    sbsj = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wtfw_tbzt'


class TbWtfwXmbhs(models.Model):
    bsm = models.IntegerField(primary_key=True)
    xzqdm = models.CharField(max_length=16, blank=True, null=True)
    symbol = models.CharField(max_length=200, blank=True, null=True)
    serial = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    xmbh = models.DateTimeField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wtfw_xmbhs'


class TbWttb(models.Model):
    bsm = models.IntegerField(primary_key=True)
    xzqmc = models.CharField(max_length=200, blank=True, null=True)
    xzqdm = models.CharField(max_length=200, blank=True, null=True)
    xzmc = models.CharField(max_length=200, blank=True, null=True)
    xzdm = models.CharField(max_length=200, blank=True, null=True)
    xzjbdm = models.CharField(max_length=20)
    tbbsm = models.CharField(unique=True, max_length=200)
    reltbbsm = models.CharField(max_length=200, blank=True, null=True)
    zdsxh = models.CharField(max_length=200, blank=True, null=True)
    relzdsxh = models.CharField(max_length=200, blank=True, null=True)
    tbmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shapearea = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    jzzmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    zlwz = models.CharField(max_length=200, blank=True, null=True)
    sfzqczzfw = models.CharField(max_length=200, blank=True, null=True)
    fwlx = models.CharField(max_length=50, blank=True, null=True)
    mpqksm = models.CharField(max_length=1000, blank=True, null=True)
    ztlx = models.CharField(max_length=10, blank=True, null=True)
    fzzt = models.CharField(max_length=10, blank=True, null=True)
    zdlx = models.CharField(max_length=10, blank=True, null=True)
    ydspqk = models.CharField(max_length=50, blank=True, null=True)
    ghqk = models.CharField(max_length=50, blank=True, null=True)
    ztxq = models.CharField(max_length=100, blank=True, null=True)
    ztmc = models.CharField(max_length=100, blank=True, null=True)
    jslx = models.CharField(max_length=50, blank=True, null=True)
    jssj = models.DateTimeField(blank=True, null=True)
    zydl = models.CharField(max_length=10, blank=True, null=True)
    sjpc = models.CharField(max_length=64, blank=True, null=True)
    bz = models.CharField(max_length=500, blank=True, null=True)
    x = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    y = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    minx = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    miny = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    maxx = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    maxy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    xmzt = models.IntegerField(blank=True, null=True)
    sjly = models.CharField(max_length=10, blank=True, null=True)
    shape = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=10, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    createname = models.CharField(max_length=100, blank=True, null=True)
    modifytime = models.DateTimeField()
    modifyname = models.CharField(max_length=100, blank=True, null=True)
    cloudid = models.CharField(max_length=200, blank=True, null=True)
    sjtgf = models.CharField(max_length=100, blank=True, null=True)
    cloudresultid = models.CharField(max_length=200, blank=True, null=True)
    cloudquerytime = models.CharField(max_length=200, blank=True, null=True)
    cloudresultdb = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wttb'


class TbWttbChildXmbhs(models.Model):
    bsm = models.IntegerField(primary_key=True)
    xzqdm = models.CharField(max_length=16, blank=True, null=True)
    symbol = models.CharField(max_length=200, blank=True, null=True)
    serial = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    xmbh = models.CharField(max_length=64, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wttb_child_xmbhs'


class TbWttbCqat(models.Model):
    bsm = models.IntegerField(primary_key=True)
    analyzetype = models.CharField(max_length=50, blank=True, null=True)
    analyzetypename = models.CharField(max_length=50, blank=True, null=True)
    analyzeshowname = models.CharField(max_length=50, blank=True, null=True)
    tag = models.CharField(max_length=200, blank=True, null=True)
    ordernumber = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tb_wttb_cqat'


class TbWttbDellog(models.Model):
    bsm = models.IntegerField(primary_key=True)
    xzqdm = models.CharField(max_length=10)
    tbbsm = models.CharField(max_length=50)
    xzjbdm = models.CharField(max_length=10)
    userid = models.CharField(max_length=10)
    ywlx = models.CharField(max_length=50)
    deletetime = models.DateTimeField(blank=True, null=True)
    xmbh = models.CharField(max_length=100, blank=True, null=True)
    xmmc = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wttb_dellog'


class TbWttbDownloadlog(models.Model):
    bsm = models.IntegerField(primary_key=True)
    xzqdm = models.CharField(max_length=20)
    logbsm = models.CharField(max_length=100)
    cjry = models.CharField(max_length=200)
    cjlx = models.IntegerField()
    cjnr = models.CharField(max_length=2000, blank=True, null=True)
    cjsj = models.DateTimeField()
    cjrymc = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wttb_downloadlog'


class TbWttbHccg(models.Model):
    bsm = models.IntegerField(primary_key=True)
    xzqdm = models.CharField(max_length=10)
    tbbsm = models.CharField(unique=True, max_length=50)
    fwbh = models.CharField(max_length=50, blank=True, null=True)
    fwzl = models.CharField(max_length=200, blank=True, null=True)
    zzlsfsj = models.CharField(max_length=10, blank=True, null=True)
    cylsfsj = models.CharField(max_length=10, blank=True, null=True)
    gglsfsj = models.CharField(max_length=10, blank=True, null=True)
    fwlb = models.CharField(max_length=10, blank=True, null=True)
    tdly = models.CharField(max_length=10, blank=True, null=True)
    jfyy = models.CharField(max_length=10, blank=True, null=True)
    fwjsyj = models.CharField(max_length=200, blank=True, null=True)
    xmzgbm = models.CharField(max_length=200, blank=True, null=True)
    jszt = models.CharField(max_length=50, blank=True, null=True)
    jsztxz = models.CharField(max_length=50, blank=True, null=True)
    tyshxydm = models.CharField(max_length=200, blank=True, null=True)
    jszjly = models.CharField(max_length=50, blank=True, null=True)
    frdb = models.CharField(max_length=20, blank=True, null=True)
    sfzh = models.CharField(max_length=50, blank=True, null=True)
    fwjzmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cs = models.CharField(max_length=10, blank=True, null=True)
    jsqk = models.CharField(max_length=10, blank=True, null=True)
    kgsj = models.DateTimeField(blank=True, null=True)
    jgsj = models.DateTimeField(blank=True, null=True)
    fwsyqk = models.CharField(max_length=50, blank=True, null=True)
    fwjtyt = models.CharField(max_length=100, blank=True, null=True)
    mz = models.CharField(max_length=20, blank=True, null=True)
    zy = models.CharField(max_length=20, blank=True, null=True)
    sjh = models.CharField(max_length=50, blank=True, null=True)
    zzmm = models.CharField(max_length=10, blank=True, null=True)
    sfbcm = models.CharField(max_length=10, blank=True, null=True)
    sfyhyz = models.CharField(max_length=10, blank=True, null=True)
    bfhyy = models.CharField(max_length=10, blank=True, null=True)
    sffhfhtj = models.CharField(max_length=10, blank=True, null=True)
    syzt = models.CharField(max_length=50, blank=True, null=True)
    syrsfzh = models.CharField(max_length=50, blank=True, null=True)
    syrmz = models.CharField(max_length=20, blank=True, null=True)
    syrzy = models.CharField(max_length=20, blank=True, null=True)
    syrsjh = models.CharField(max_length=50, blank=True, null=True)
    syrzzmm = models.CharField(max_length=10, blank=True, null=True)
    syrsfbcm = models.CharField(max_length=10, blank=True, null=True)
    ztqdfs = models.CharField(max_length=10, blank=True, null=True)
    yjsztgx = models.CharField(max_length=20, blank=True, null=True)
    zymj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    zygdmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    zyjgmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qztdmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qzgdmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qzjgmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    zyjbntmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bdynghsj = models.DateTimeField(blank=True, null=True)
    sfhdynhjf = models.CharField(max_length=10, blank=True, null=True)
    zybhqmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bhqhdsj = models.DateTimeField(blank=True, null=True)
    sfhdbhqhjf = models.CharField(max_length=10, blank=True, null=True)
    zysthxmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sthxsj = models.DateTimeField(blank=True, null=True)
    sfsthxhjf = models.CharField(max_length=10, blank=True, null=True)
    zdsfgh = models.CharField(max_length=10, blank=True, null=True)
    cxghyt = models.CharField(max_length=50, blank=True, null=True)
    sfjsfw = models.CharField(max_length=10, blank=True, null=True)
    sffhtg = models.CharField(max_length=10, blank=True, null=True)
    tgyt = models.CharField(max_length=100, blank=True, null=True)
    sfpdsq = models.CharField(max_length=10, blank=True, null=True)
    sflx = models.CharField(max_length=10, blank=True, null=True)
    sflx_pzjg = models.CharField(max_length=50, blank=True, null=True)
    sflx_pzsj = models.DateTimeField(blank=True, null=True)
    sflx_lxmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sfzjdsp = models.CharField(max_length=10, blank=True, null=True)
    sfzjdsp_pzjg = models.CharField(max_length=50, blank=True, null=True)
    sfzjdsp_pzsj = models.DateTimeField(blank=True, null=True)
    sfzjdsp_pzmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sfbyd = models.CharField(max_length=10, blank=True, null=True)
    sfbyd_pzjg = models.CharField(max_length=50, blank=True, null=True)
    sfbyd_pzsj = models.DateTimeField(blank=True, null=True)
    sfbyd_pzmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sfghxk = models.CharField(max_length=10, blank=True, null=True)
    sfghxk_pzjg = models.CharField(max_length=50, blank=True, null=True)
    sfghxk_pzsj = models.DateTimeField(blank=True, null=True)
    sfghxk_pzmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sfbdcdj = models.CharField(max_length=10, blank=True, null=True)
    zsbh = models.CharField(max_length=50, blank=True, null=True)
    fzsj = models.DateTimeField(blank=True, null=True)
    djmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sfxzcf = models.CharField(max_length=10, blank=True, null=True)
    cfyj = models.CharField(max_length=100, blank=True, null=True)
    sfsqfyqzzx = models.CharField(max_length=10, blank=True, null=True)
    fkje = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sfcdzx = models.CharField(max_length=10, blank=True, null=True)
    fysfsl = models.CharField(max_length=10, blank=True, null=True)
    cfzxqk = models.CharField(max_length=50, blank=True, null=True)
    cdzxzt = models.CharField(max_length=10, blank=True, null=True)
    sfss = models.CharField(max_length=10, blank=True, null=True)
    ssyy = models.CharField(max_length=50, blank=True, null=True)
    bcsm = models.CharField(max_length=500, blank=True, null=True)
    sm = models.CharField(max_length=500, blank=True, null=True)
    hcry = models.CharField(max_length=50, blank=True, null=True)
    sign = models.TextField(blank=True, null=True)
    hcsj = models.DateTimeField(blank=True, null=True)
    fwlx = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wttb_hccg'


class TbWttbHccgsh(models.Model):
    bsm = models.IntegerField(primary_key=True)
    xzqdm = models.CharField(max_length=10, blank=True, null=True)
    tbbsm = models.CharField(unique=True, max_length=50, blank=True, null=True)
    xjshjg = models.CharField(max_length=10, blank=True, null=True)
    xjshsj = models.DateTimeField(blank=True, null=True)
    xjshry = models.CharField(max_length=50, blank=True, null=True)
    xjshsm = models.CharField(max_length=500, blank=True, null=True)
    cjshjg = models.CharField(max_length=10, blank=True, null=True)
    cjshsj = models.DateTimeField(blank=True, null=True)
    cjshry = models.CharField(max_length=50, blank=True, null=True)
    cjshsm = models.CharField(max_length=500, blank=True, null=True)
    sjshjg = models.CharField(max_length=10, blank=True, null=True)
    sjshsj = models.DateTimeField(blank=True, null=True)
    sjshry = models.CharField(max_length=50, blank=True, null=True)
    sjshsm = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wttb_hccgsh'


class TbWttbHccgshjl(models.Model):
    bsm = models.IntegerField(primary_key=True)
    xzqdm = models.CharField(max_length=10)
    tbbsm = models.CharField(max_length=50)
    shsm = models.CharField(max_length=1000, blank=True, null=True)
    shry = models.CharField(max_length=100, blank=True, null=True)
    shsj = models.CharField(max_length=100, blank=True, null=True)
    auditbsm = models.CharField(max_length=100, blank=True, null=True)
    xjshjg = models.CharField(max_length=10, blank=True, null=True)
    xjshsm = models.CharField(max_length=1000, blank=True, null=True)
    xjshry = models.CharField(max_length=100, blank=True, null=True)
    xjshsj = models.CharField(max_length=100, blank=True, null=True)
    cjshjg = models.CharField(max_length=10, blank=True, null=True)
    cjshsm = models.CharField(max_length=1000, blank=True, null=True)
    cjshry = models.CharField(max_length=100, blank=True, null=True)
    cjshsj = models.CharField(max_length=100, blank=True, null=True)
    sjshjg = models.CharField(max_length=50, blank=True, null=True)
    sjshsm = models.CharField(max_length=1000, blank=True, null=True)
    sjshry = models.CharField(max_length=100, blank=True, null=True)
    sjshsj = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wttb_hccgshjl'


class TbWttbHcfj(models.Model):
    bsm = models.IntegerField(primary_key=True)
    xzqdm = models.CharField(max_length=10, blank=True, null=True)
    tbbsm = models.CharField(max_length=50, blank=True, null=True)
    fjmc = models.CharField(max_length=500, blank=True, null=True)
    fjmc2 = models.CharField(max_length=500, blank=True, null=True)
    fjmc3 = models.CharField(max_length=500, blank=True, null=True)
    fjlx = models.CharField(max_length=50, blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    points_json = models.TextField(blank=True, null=True)
    fjly = models.CharField(max_length=50, blank=True, null=True)
    createtime1 = models.DateTimeField(blank=True, null=True)
    fjmode = models.CharField(max_length=50, blank=True, null=True)
    arg = models.CharField(max_length=500, blank=True, null=True)
    arg1 = models.CharField(max_length=500, blank=True, null=True)
    fjtype = models.CharField(max_length=5, blank=True, null=True)
    psry = models.CharField(max_length=100, blank=True, null=True)
    angle = models.IntegerField(blank=True, null=True)
    dkid = models.CharField(max_length=100, blank=True, null=True)
    jym = models.TextField(blank=True, null=True)
    x = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    y = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    rwhtlysm = models.CharField(max_length=100, blank=True, null=True)
    azimuth = models.IntegerField(blank=True, null=True)
    distance = models.CharField(max_length=100, blank=True, null=True)
    yaw = models.IntegerField(blank=True, null=True)
    roll = models.IntegerField(blank=True, null=True)
    pitch = models.IntegerField(blank=True, null=True)
    height = models.CharField(max_length=100, blank=True, null=True)
    accuracy = models.IntegerField(blank=True, null=True)
    lysb = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wttb_hcfj'


class TbWttbLog(models.Model):
    bsm = models.IntegerField(primary_key=True)
    sjbh = models.CharField(max_length=50)
    tbbsm = models.CharField(max_length=50)
    czry = models.CharField(max_length=10)
    czrymc = models.CharField(max_length=50, blank=True, null=True)
    czlx = models.CharField(max_length=5)
    cznr = models.CharField(max_length=20, blank=True, null=True)
    czsj = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tb_wttb_log'


class TbWttbQlist(models.Model):
    xzqdm = models.CharField(max_length=200, blank=True, null=True)
    bsm = models.IntegerField(primary_key=True)
    tbbsm = models.CharField(max_length=200, blank=True, null=True)
    zlwz = models.CharField(max_length=200, blank=True, null=True)
    xzjbdm = models.CharField(max_length=20, blank=True, null=True)
    zdsxh = models.CharField(max_length=200, blank=True, null=True)
    tbmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sjly = models.CharField(max_length=10, blank=True, null=True)
    ydspqk = models.CharField(max_length=50, blank=True, null=True)
    ghqk = models.CharField(max_length=50, blank=True, null=True)
    ztlx = models.CharField(max_length=10, blank=True, null=True)
    ztmc = models.CharField(max_length=100, blank=True, null=True)
    ztxq = models.CharField(max_length=100, blank=True, null=True)
    jslx = models.CharField(max_length=50, blank=True, null=True)
    jssj = models.DateTimeField(blank=True, null=True)
    zydl = models.CharField(max_length=10, blank=True, null=True)
    bz = models.CharField(max_length=500, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cloudid = models.CharField(max_length=200, blank=True, null=True)
    cloudresultid = models.CharField(max_length=200, blank=True, null=True)
    reltbbsm = models.CharField(max_length=200, blank=True, null=True)
    relzdsxh = models.CharField(max_length=200, blank=True, null=True)
    wyzt = models.TextField(blank=True, null=True)
    xjshjg = models.CharField(max_length=10, blank=True, null=True)
    optype = models.TextField(blank=True, null=True)
    sjshjg = models.CharField(max_length=10, blank=True, null=True)
    cjshjg = models.CharField(max_length=10, blank=True, null=True)
    flowid = models.BigIntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    nodeid = models.BigIntegerField(blank=True, null=True)
    workstate = models.IntegerField(blank=True, null=True)
    shzt = models.TextField(blank=True, null=True)
    fzzt = models.CharField(max_length=10, blank=True, null=True)
    zdlx = models.CharField(max_length=10, blank=True, null=True)
    xzdm = models.CharField(max_length=200, blank=True, null=True)
    xzmc = models.CharField(max_length=50, blank=True, null=True)
    fwzl = models.CharField(max_length=200, blank=True, null=True)
    sfsj = models.TextField(blank=True, null=True)
    fwlb = models.CharField(max_length=10, blank=True, null=True)
    fwlx = models.CharField(max_length=50, blank=True, null=True)
    tdly = models.CharField(max_length=10, blank=True, null=True)
    jfyy = models.CharField(max_length=10, blank=True, null=True)
    fwjsyj = models.CharField(max_length=200, blank=True, null=True)
    jszt = models.CharField(max_length=50, blank=True, null=True)
    syzt = models.CharField(max_length=50, blank=True, null=True)
    fwsyqk = models.CharField(max_length=50, blank=True, null=True)
    fwjzmj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sfzyjbnt = models.TextField(blank=True, null=True)
    sfzybhq = models.TextField(blank=True, null=True)
    sfzysthx = models.TextField(blank=True, null=True)
    sfzqczzfw = models.CharField(max_length=200, blank=True, null=True)
    ffzt = models.TextField(blank=True, null=True)
    pic = models.TextField(blank=True, null=True)
    xmbh = models.CharField(max_length=200, blank=True, null=True)
    xmmc = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wttb_qlist'


class TbWttbRelWtfw(models.Model):
    bsm = models.IntegerField(primary_key=True)
    wttbtbbsm = models.CharField(max_length=200)
    wtfwtbbsm = models.CharField(max_length=200)
    xzqdm = models.CharField(max_length=200)
    overlaparea = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    modifytime = models.DateTimeField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wttb_rel_wtfw'


class TbWttbRwfp(models.Model):
    bsm = models.IntegerField(primary_key=True)
    xzqdm = models.CharField(max_length=10, blank=True, null=True)
    tbbsm = models.CharField(max_length=100, blank=True, null=True)
    subtaskid = models.IntegerField(blank=True, null=True)
    sbbsm = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wttb_rwfp'


class TbWttbRwfpJw(models.Model):
    bsm = models.IntegerField(primary_key=True)
    xzqdm = models.CharField(max_length=10, blank=True, null=True)
    tbbsm = models.CharField(max_length=100, blank=True, null=True)
    subtaskid = models.IntegerField(blank=True, null=True)
    sbbsm = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wttb_rwfp_jw'


class TbWttbTbzt(models.Model):
    bsm = models.IntegerField(primary_key=True)
    tbbsm = models.CharField(max_length=50)
    xzqdm = models.CharField(max_length=10)
    tbzt = models.CharField(max_length=10, blank=True, null=True)
    jzsbbsm = models.CharField(max_length=20, blank=True, null=True)
    xjqr = models.IntegerField(blank=True, null=True)
    qrry = models.CharField(max_length=200, blank=True, null=True)
    qrsj = models.DateTimeField(blank=True, null=True)
    sbry = models.CharField(max_length=200, blank=True, null=True)
    sbsj = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wttb_tbzt'


class TbWttbXmbhs(models.Model):
    bsm = models.IntegerField(primary_key=True)
    xzqdm = models.CharField(max_length=16, blank=True, null=True)
    symbol = models.CharField(max_length=200, blank=True, null=True)
    serial = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    xmbh = models.DateTimeField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wttb_xmbhs'


class TbWycgjl(models.Model):
    bsm = models.BigIntegerField()
    ryname = models.CharField(max_length=100, blank=True, null=True)
    tjsj = models.DateTimeField(blank=True, null=True)
    filename = models.CharField(max_length=100, blank=True, null=True)
    jsname = models.CharField(max_length=100, blank=True, null=True)
    jssj = models.DateTimeField(blank=True, null=True)
    jsstatus = models.CharField(max_length=2, blank=True, null=True)
    xzqdm = models.CharField(max_length=10, blank=True, null=True)
    hctbgs = models.CharField(max_length=100, blank=True, null=True)
    hctbname = models.CharField(max_length=100, blank=True, null=True)
    tbzs = models.CharField(max_length=100, blank=True, null=True)
    encode = models.CharField(max_length=1000, blank=True, null=True)
    filesize = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_wycgjl'


class TbXzgdhd(models.Model):
    bsm = models.BigIntegerField(blank=True, null=True)
    xzqdm = models.SmallIntegerField(blank=True, null=True)
    xmc = models.CharField(max_length=255, blank=True, null=True)
    tbbsm = models.CharField(max_length=50)
    tbbh = models.CharField(max_length=200, blank=True, null=True)
    shapearea = models.BigIntegerField(blank=True, null=True)
    xmbh = models.CharField(max_length=200, blank=True, null=True)
    xmmc = models.CharField(max_length=255, blank=True, null=True)
    lxrq = models.DateTimeField(blank=True, null=True)
    jgrq = models.DateTimeField(blank=True, null=True)
    ztz = models.BigIntegerField(blank=True, null=True)
    ssgm = models.BigIntegerField(blank=True, null=True)
    xzgdmj = models.BigIntegerField(blank=True, null=True)
    tzgzmj = models.BigIntegerField(blank=True, null=True)
    xzstmj = models.BigIntegerField(blank=True, null=True)
    xzgdpjdb = models.BigIntegerField(blank=True, null=True)
    tzgzqdb = models.BigIntegerField(blank=True, null=True)
    tzgzhdb = models.BigIntegerField(blank=True, null=True)
    dkgs = models.CharField(max_length=100, blank=True, null=True)
    dkbh = models.CharField(max_length=100, blank=True, null=True)
    dkmj = models.CharField(max_length=100, blank=True, null=True)
    xzb = models.BigIntegerField(blank=True, null=True)
    yzb = models.BigIntegerField(blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    shapestr = models.TextField(blank=True, null=True)
    shape = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=10, blank=True, null=True)
    sjly = models.CharField(max_length=10, blank=True, null=True)
    ssgxq = models.CharField(max_length=10, blank=True, null=True)
    sjtgf = models.CharField(max_length=100, blank=True, null=True)
    sfsjcc = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_xzgdhd'


class TbXzqfw(models.Model):
    xdm = models.CharField(max_length=20, blank=True, null=True)
    fw = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_xzqfw'


class TbHcqy(models.Model):
    smc = models.CharField(max_length=50, blank=True, null=True)
    sdm = models.CharField(primary_key=True, max_length=50)
    cmc = models.CharField(max_length=50, blank=True, null=True)
    cdm = models.CharField(max_length=50, blank=True, null=True)
    xmc = models.CharField(max_length=50, blank=True, null=True)
    xdm = models.CharField(max_length=50, blank=True, null=True)
    zdw = models.BigIntegerField(blank=True, null=True)
    fdw = models.BigIntegerField(blank=True, null=True)
    dstatus = models.TextField(blank=True, null=True)
    drsj = models.DateTimeField(blank=True, null=True)
    rstatus = models.BigIntegerField(blank=True, null=True)
    rsj = models.DateTimeField(blank=True, null=True)
    tjsj = models.DateTimeField(blank=True, null=True)
    ry = models.CharField(max_length=50, blank=True, null=True)
    sfwc = models.BigIntegerField(blank=True, null=True)
    sfqq = models.BigIntegerField(blank=True, null=True)
    isgj = models.BigIntegerField(blank=True, null=True)
    wzyz = models.BigIntegerField(blank=True, null=True)
    hctp = models.BigIntegerField(blank=True, null=True)
    kfqlist = models.CharField(max_length=1000, blank=True, null=True)
    shdw = models.CharField(max_length=1000, blank=True, null=True)
    state = models.BigIntegerField(blank=True, null=True)
    ossurl = models.CharField(max_length=100, blank=True, null=True)
    process = models.CharField(max_length=50, blank=True, null=True)
    sfhcqy = models.BigIntegerField(blank=True, null=True)
    hcdw = models.CharField(max_length=500, blank=True, null=True)
    bsm = models.BigIntegerField(blank=True, null=True)
    gentrateresult = models.CharField(max_length=500, blank=True, null=True)
    dbstate = models.BigIntegerField(blank=True, null=True)
    dburl = models.CharField(max_length=100, blank=True, null=True)
    dbprocess = models.CharField(max_length=50, blank=True, null=True)
    dbgentrateresult = models.CharField(max_length=500, blank=True, null=True)
    minx = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    maxx = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    miny = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    maxy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hcqylevel = models.BigIntegerField(blank=True, null=True)
    xdmold = models.CharField(max_length=50, blank=True, null=True)
    xzdm = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_hcqy'
