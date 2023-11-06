# Một SET gồm các yếu tố
# Được giới hạn bởi cặp ngoặc {}, tất cả những gì nằm trong đó là những phần tử của Set.
# Các phần tử của Set được phân cách nhau ra bởi dấu phẩy (,).
# Set không chứa nhiều hơn 1 phần tử trùng lặp

# add
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

# clear
fruits.clear()
print(fruits)

# copy
fruits.copy()
print(fruits)

# difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)
print(z)

# difference_update: xoá những cái khác
x.difference_update(y)
print(x)

# discard: Xóa mục được chỉ định
fruits1 = {"apple", "banana", "cherry"}
fruits1.discard("banana")
print(fruits1)

# intersection: tìm các tập hợp giống nhau
# intersection_update: xoá các tập hợp khác nhau
x1 = {"apple", "banana", "cherry"}
y1 = {"google", "microsoft", "apple"}
z1 = x1.intersection(y1)
print(z1)

# isdisjoint: check 2 tập hợp có gì giống nhau không
z1 = x1.isdisjoint(y1) 
print(z1)

# issubset: tập hợp x1 có chứa tất cả các phần tử của y1 không
z1 = x1.issubset(y1) 
print(z1)

# https://www.w3schools.com/python/python_ref_set.asp