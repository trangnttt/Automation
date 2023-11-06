# tạo class tính diện tích hình chữ nhật
class AreaRect:
    # khởi tạo
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def calculate_area(self):
        return self.l * self.b

area1 = AreaRect(2,5)

print(area1.calculate_area())


class Cat:
    def __init__(self, cat_name, cat_color):
        self.cat_name = cat_name
        self.cat_color = cat_color
    
    def Info_Cat(self):
        print(self.cat_name, "cat has", self.cat_color,"color")

cat1 = Cat("Tom", "grey and white")
cat1.Info_Cat()

# Hàm __init__() là hàm khởi tạo (constructor) của class trong Python
# Cú pháp
# def __init__(self, [parameter1, parameter2,...]):
#     # Body of __init__()
# Trong đó,

# def là từ khóa khai báo một hàm trong Python
# __init__() là tên của hàm khởi tạo (constructor)
# self là tham số đầu tiên của hàm __init__(). Đây là một tham chiếu đến đối tượng hiện tại của lớp và được sử dụng để truy cập các biến thuộc về lớp đó.
# [parameter1, parameter2,…] là các tham số tùy chọn, thường là các giá trị để gán cho các thuộc tính của đối tượng được tạo ra.