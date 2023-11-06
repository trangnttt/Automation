# 1. mở file và tạo file
f = open("/Users/trangntt/Documents/Martha/Learns/python/FileIODemo/write_demo.txt", "w")
# 2. Viết trong file 
List = [1, 2, 3 , 4, 10]
for i in List:
    f.write(str(i) + "\n")
# 3. Đóng file 
f.close()


