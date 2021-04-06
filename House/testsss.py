import xlsxwriter

wb = xlsxwriter.Workbook("filename.xlsx")
ws = wb.add_worksheet("案例")

# 数据
data = [
    ('描述', '属性', '方法名称'),
    ('字体类型', 'font_name', 'set_font_name()'),
    ('字体大小', 'font_size', 'set_font_size()'),
    ('字体颜色', 'font_color', 'set_font_color()'),
    ('粗体', 'bold', 'set_bold()')
]

# 字段格式
header = {
    'bold': True,  # 粗体
    'font_name': '仿宋',
    'font_size': 14,
    'border': True,  # 边框线
    'align': 'center',  # 水平居中
    'valign': 'vcenter',  # 垂直居中
    'bg_color': '#66DD00'  # 背景颜色
}

text = {
    'font_name': '微软雅黑',
    'font_size': 10,
    'border': True,
    'align': 'left',  # 左对齐
    'valign': 'vcenter'
}

headerpm = wb.add_format(header)
textpm = wb.add_format(text)
ws.set_column('C:C', 13)  # C列宽度

for row, rowdata in enumerate(data):
    for col, coldata in enumerate(rowdata):
        if row == 0:
            ws.write(row, col, coldata, headerpm)
        else:
            ws.write(row, col, coldata, textpm)

wb.close()
