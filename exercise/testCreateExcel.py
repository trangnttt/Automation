# ********** Viết file excel tạo data test cho Login **********

from openpyxl import Workbook
wb = Workbook()

ws = wb.active
datas = (
    ['No', 'Username', 'Password', 'Desired Result', 'Message'],
    [1, '', 'SuperSecretPassword!', 'Pass', 'Your username is invalid!'],
    [2, 'tomsmith', '', 'Pass', 'Your password is invalid!'],
    [3, 'tomsmith', 'SuperSecretPassword', 'Fail', 'You username and password is invalid!'],
    [4,	'tomsmith',	'SuperSecretPassword!',	'Pass',	'You logged into a secure area!'],
)
for data in datas:
    ws.append(data)

wb.save("demo-excel.xlsx")

# # ********** Đọc file excel **********
# # cài pip install xlrd==1.2.0
# from xlrd import open_workbook

# class readDataTest:
#     def dataTestLogin(self):
#         data_test = open_workbook("./demo-excel.xlsx")
#         values = []
#         for s in data_test.sheets():
#             # print(s.name)
#             for r in range(1, s.nrows):
#                 col_name = s.row(0)
#                 col_value = []
#                 for name, col in zip(col_name, range(s.ncols)):
#                     value = s.cell(r,col).value
#                     try:
#                         value = str(int(value))
#                     except:
#                         pass
#                     col_value.append(value)
#                 values.append(col_value)
#         return values

