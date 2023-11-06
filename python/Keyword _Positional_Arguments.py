def nameAge(name, age):
	print("Hi, I am", name)
	print("My age is ", age)
	
print("--------Ví dụ 1--------")
nameAge(name="Prince", age=20)
nameAge(age=20, name="Prince")

print("--------Ví dụ 2--------")
# You will get correct output because argument is given in order
print("Case-1:")
nameAge("Prince", 20)
# You will get incorrect output because argument is not in order
print("\nCase-2:")
nameAge(20, "Prince")

def minus(a, b):
	return a - b
a, b = 20, 10

print("--------Ví dụ 3--------")
result1 = minus(a, b)
print("Used Positional arguments:", result1)

result2 = minus(b, a)
print("Used Positional arguments:", result2)
