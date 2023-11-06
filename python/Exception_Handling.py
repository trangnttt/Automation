# VD: tránh tình trạng user nhập số 0 và báo lỗi

# ---------- try với khối lệnh except ----------
try:
    print("a: ")
    a = int(input())
    print("b: ")
    b = int(input())
    print(a/b)
except Exception as e:
    print(e)

# ---------- try với khối lệnh else ----------
# để định nghĩa một khối lệnh (block of code) sẽ được thực thi nếu không có exception nào xảy ra.
try:
    x = 1/1
    print(x)
except ZeroDivisionError:
    print("Cannot divide by 0!")
else:
    print("Nothing wrong.")

# ---------- try với khối lệnh finally ----------
# luôn luôn được thực thi bất kể khối lệnh try có xảy ra exception hay không.

try:
    x = 1/0
    print(x)
except ZeroDivisionError:
    print("Cannot divide by 0!")
finally:
    print("The 'try except' is finished!")

# ---------- try với khối lệnh raise ----------
# Python cho phép chúng ta có thể ném ra một exception nếu thỏa một điều kiện nào đó. 
# Từ khóa raise giúp chúng ta làm việc này.

try:
    print("y: ")
    y = int(input())
    print("z: ")
    z = int(input())
    if z == 0 :
        raise Exception("z = 0")
    print(y/z)
except Exception as e:
    print(e)