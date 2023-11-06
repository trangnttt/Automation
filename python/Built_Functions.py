
demo_tuple = (5,7,8,9,2)

# max
print("max is: ",max(demo_tuple))

# min
print("min is: ",min(demo_tuple))

# iter & next
x = iter(demo_tuple)
print("iter is: ",next(x))

# reversed
ralph = reversed(demo_tuple)
for i in ralph:
    print(i)

# slice
s = slice(2)
print("slice is: ",demo_tuple[s])

# sorted
print("sorted is: ",sorted(demo_tuple))

# sum
print("sum is: ",sum(demo_tuple))

# input
greet = input("What is your name?")
print(greet)