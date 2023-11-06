import my_custom_module

# Gọi class từ module
p = my_custom_module.Person("Phong",30)
print("Name:",p.name)

# Gọi hàm từ module
total = my_custom_module.phep_cong(5,5)
print("a + b =", total)

# Gọi biến từ module
v = my_custom_module.list_fruists
print("List_fruists : ",v)