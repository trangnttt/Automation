from selenium import webdriver
from selenium.webdriver.common.by import By
import XLUtils

file = "./demo-excel.xlsx"
rows = XLUtils.getRowCount(file,"Sheet")

for r in range(2, rows+1):
    read_1 =  XLUtils.readData(file, "Sheet", r, 1)
    read_2 = XLUtils.readData(file, "Sheet", r, 2)
    XLUtils.fillGreenColor(file, "Sheet", r, 1)
    XLUtils.fillRedColor(file, "Sheet", r, 2)
    print(read_1)