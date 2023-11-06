# ****** Cắt chuỗi ****** 
# Giữ đầu bỏ đuôi. Tức là phần tử đầu tiên thì bao hàm trong danh sách con lấy ra, 
# nhưng phần tử có chỉ số sau thì không lấy

s = "welcome to VSCode"
print(s[0:8])
print(s[3:])
print(s[::-1]) #đảo chuỗi

# Nhảy cóc: Chuỗi [ index bắt đầu : index kết thúc : bước nhảy]
print(s[0:8:2])