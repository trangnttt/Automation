# ****** Toán tử trong Python ******

# Toán tử số học (arithmetic operator)
x = 15
y = 4
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y) # chia trả về phần dư
print(x // y) # chia trả về phần nguyên
print(x ** y) # luỹ thừa



# Toán tử so sánh (comparison operator)
print('x > y is', x>y)
print('x < y is', x<y)
print('x == y is', x==y)
print('x != y is', x!=y)
print('x >= y is', x>=y)
print('x <= y is', x<=y)

# Toán tử logic (logical operator)
a = True
b = False

print('x(True) and y(False) is', a and b)
print('x(True) or y(False) is', a or b)
print('not x(True) is', not a)

# Toán tử trên bit (bitwise operator)
bit_1 = 10
bit_2 = 4

print("x & y = ", bit_1 & bit_2) # Output 0 (0000 0000)
print("x | y = ", bit_1 | bit_2) # Output 14 (0000 1110)
print("~x = ", ~bit_1) # Output -11 (1111 0101)
print("x ^ y = ", bit_1 ^ bit_2) # Output 14 (0000 1110)
print("x >> y = ", bit_1 >> 2) # Output 2 (0000 0010)
print("x >> y = ", bit_1 << 2) # Output 40 (0010 1000)

# Toán tử gán (assignment operator)
num_1 = 10
print("num_1 = ", num_1)
num_2 = num_1
print("num_2 = ", num_2)

# cộng
num_2 += num_1
print("num_2 +=num_1 then num_2 = ", num_2)

# trừ
num_2 -= num_1
print("num_2 -=num_1 then num_2 = ", num_2)
 
# nhân
num_2 *= num_1
print("num_2 *=num_1 then num_2 = ", num_2)
 
# bitwise lishift operator
num_2 <<= num_1
print("num_2 <<=num_1 then num_2 = ", num_2)



# Một số toán tử khác
# identity operator
list1 = ["abc", "def"]
list2 = ["abc", "def"]

print(list1 is list2)
print(list1 == list2)

# membership operator
print("abc" in list2)
print("abc" not in list2)