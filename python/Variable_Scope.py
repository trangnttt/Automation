# Local
def myfunc():
    x = 100  # biến local
    print(x)
myfunc()

# Global
mess = "Hello"
def Greet():
    print("Local", mess)
Greet()
print("Global", mess)

# global keyword
x = 15
def change():
    global x
    x = 20
    print(x)
change()
print("x = ", x)

# Nonlocal
# function bên ngoài
def outer():
    mess = "Local"
    # Function lồng nhau
    def inner():
        # declare nonlocal variable
        nonlocal mess
        mess = "nonlocal"
        print("inner:", mess)
    inner()
    print("outer:", mess)
outer()
