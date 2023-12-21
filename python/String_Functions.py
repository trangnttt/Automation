name = "I am Admin"

# len(s) số lượng ký tự trong chuỗi bao gồm dấu câu, khoảng cách và tất cả kiểu ký tự đặc biệt
print("len():",len(name))
# str() trả về một chuỗi được coi là đại diện không chính thức hoặc có thể in được của một đối tượng
print("str():",str(name))
# upper() viết hoa chuỗi
print("upper():",name.upper())
# count: Cú pháp: str.count(sub, start= 0, end=len(string)) => sub: Đây là chuỗi con để được tìm kiếm.
sub = "Admin"
print("count():",name.count(sub, 0, len(name)))
# isupper trả về true nếu tất cả ký tự trong chuỗi là chữ hoa
print("isupper():",name.isupper())
# islower trả về true nếu tất cả ký tự trong chuỗi là ở dạng chữ thường, nếu không là false.
print("islower():",name.islower())
# slipt Cú pháp: str.split(str="", num=string.count(str))
print("split():",name.split())
# lstrip trả về một bản sao của chuỗi ban đầu sau khi đã cắt tất cả các ký tự chars đã cung cấp từ phần đầu của chuỗi (các ký tự mặc định là khoảng trắng)
a = "--------Python--------"
print("lstrip():",a.lstrip("-"))
# rstrip  trả về một bản sao của chuỗi trong đó tất cả các chars đã được xóa từ phần cuối chuỗi
print("rstrip():",a.rstrip("-"))
# replace
print("replace():",name.replace(" ", "-"))
# find Cú pháp: str.find(str, beg=0 end=len(string))
print("find():",name.find("Admin"))
# index
print("index():",name.index("I"))

# Xem thêm: https://www.w3schools.com/python/python_ref_string.asp