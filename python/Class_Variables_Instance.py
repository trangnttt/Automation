# *************Class Variables: là 1 biến được định nghĩa trong 1 lớp, và bên ngoài bất kỳ 1 phương thức nào của lớp.*************
class Employee:
    text = "XYZ Private Limited"  # This is a class variable

    # Để truy cập nó trong hàm khởi tạo init có 2 cách
    def __init__(self, name):
        self.name = name
        print(Employee.text)  # cách 1
        print(self.text)  # cách 2

emp1 = Employee("Ram")

# Chỉnh sửa Class Variables
class Employee_1:
    # Class variable
    office_name = "ABC"

    # Constructor
    def __init__(self, employee_ID, employee_name):
        self.employee_ID = employee_ID
        self.employee_name = employee_name

    # hàm show giá trị đó ra 
    def show(self):
        print("ID:", self.employee_ID)
        print("Name:", self.employee_name)
        print("Office name:", Employee_1.office_name)

# create Object
e1 = Employee_1("T1111", "Phero")
print('----Before----')
e1.show()

# Modify class variable
Employee_1.office_name = "BCD"
print('----After----')
e1.show()

# *************Instance Variables: Các biến thể hiện được định nghĩa trong các phương thức lớp, điển hình là hàm khởi tạo*************
class Employee_2:
    def __init__(self, name, id):
        self.name = name # This is Instance Variables
        self.id = id  # This is Instance Variables

# Truy cập nó
e2 = Employee_2("John Doe", 123)
print(e2.name)

# modify instance variable
e2.name = "Tom"
print("modify: ",e2.name)
# xoá instance variable
del e2.name
print("Name delected!")

# Xem thêm: https://www.atatus.com/blog/class-variables-vs-instance-variables-in-java/