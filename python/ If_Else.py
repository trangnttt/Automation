# ****** IF ELSE ******
age = 20
if (age > 18):
    print ("Tuổi lớn hơn 18")

# Lệnh if elif else 
score =  85

if score > 90:
    print("I get motobike")
elif score > 80 and score < 90:
    print("I will get bycycle")
elif score > 70 and score < 80:
    print("I will still get something")
else:
    print("you don't get anything")


# ****** FOR ******
fruits = ["apple", "orange", "kiwi"]
for fruit in fruits:
	print(fruit)
	
# In từ 1-> 10
for i in range(1,11):
	print(i)



# ****** WHILE ******
# In lần lượt các số nhỏ hơn 8
count = 1
n=0
while (n < 8):
    print ('Số thứ', count,' là:', n)
    n = n + 1
    count = count + 1
print ("Hết rồi!")



# ****** Break_and_Continue ******
for val in "Phero":
    if val == "r":
        break
    print(val)

print("Kết thúc break!")

for a in "Hello":
    if a == "l":
        continue
    print(a)
print("Kết thúc continue!")