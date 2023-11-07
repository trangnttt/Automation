from xlrd import open_workbook

class readDataTest:
    def dataTestLogin(self):
        data_test = open_workbook("./demo-excel.xlsx")
        values = []
        for s in data_test.sheets():
            # print(s.name)
            for r in range(1, s.nrows):
                col_name = s.row(0)
                col_value = []
                for name, col in zip(col_name, range(s.ncols)):
                    value = s.cell(r,col).value
                    try:
                        value = str(int(value))
                    except:
                        pass
                    col_value.append(value)
                values.append(col_value)
        return values