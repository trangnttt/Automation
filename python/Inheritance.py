# Kế thừa (Inheritance) là việc một lớp được khai báo kế thừa toàn bộ thuộc tính và phương thức của một lớp khác
# Lớp con có thể sử dụng toàn bộ dữ liệu khai báo ở mức độ protected và public ở lớp cha. 
# Riêng với private thì không được, vì đó là mức độ bảo mật cao nhất, chỉ sử dụng bên trong nội bộ của lớp cha.

# --------- Đơn kế thừa ---------

class Animal:
    def __init__(self, name):
        self.name = name
    def Info(self):
        print("Animal: " + self.name)

# lớp con Dog kế thừa lớp Animal
class Dog(Animal):
    def Speak(self):
        print("Gou gou!")

d = Dog("Dog")
d.Info()
d.Speak()

