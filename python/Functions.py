# Calling a Function

def myFunc():
    print("Hello")
myFunc()

# Arguments
def myFunc1(name):
    print("Hi " + name)
myFunc1("Phero")


# Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")
