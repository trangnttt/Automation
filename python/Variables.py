# ****** Biến ******
username = "admin"
age = 30
height = 175

print(username)
print(type(age)) # in ra KDL

# ép KDL
print(type(height))
print(type(float(height)))


# ****** Chuỗi ******
x =  "I am Phero"
y = 'I am 30'
print(type(x))
print(type(y))
print(x[5])


# ****** Cắt chuỗi ****** 
# Giữ đầu bỏ đuôi. Tức là phần tử đầu tiên thì bao hàm trong danh sách con lấy ra, 
# nhưng phần tử có chỉ số sau thì không lấy
s = "welcome to VSCode"
print(s[0:8])
print(s[3:])
print(s[::-1]) #đảo chuỗi

# Nhảy cóc: Chuỗi [ index bắt đầu : index kết thúc : bước nhảy]
print(s[0:8:2])


# ****** Format chuỗi ****** 
x = "Python Class"
y = "Learn now"
print("Welcom to {classname} from {address}".format(classname="Phero", address = "VietNam"))

