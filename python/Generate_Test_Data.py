# pip3 install Faker

from faker import Faker
from openpyxl import Workbook

fake_data = Faker()
wb = Workbook()
ws = wb.active

for i in range (1,10):
    ws.cell(row=i, column = 1).value = fake_data.name()

wb.save("demo-excel.xlsx")