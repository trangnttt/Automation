list = ['A', 'B', 'C']

# append: thêm 1 phần tử vào cuối của một list.
list.append('D')
print("append D:",list)

# insert: thêm phần tử vào vị trí index của list, và các phần tử sau index đó sẽ được đẩy về phía sau
list.insert(1, "D")
print("insert D vị trí 1:",list)

# extend: kế thừa lại các phần tử của list2 và thêm vào trong list1.
list.extend('E')
print("extend E:",list)

# remove: xóa phần tử đầu tiên khỏi list
list.remove("D")
print("remove D:",list)

# pop: xóa bỏ phần tử trong list dựa trên index của nó
list.pop(3)
print("pop 3:",list)

# index: trả về index xuất hiện đầu tiên của phần tử mà bạn muốn tìm và nếu như không tìm thấy thì nó sẽ gọi exception
print("index B:",list.index('B'))

# count: đếm số lần xuất hiện của một thành phần trong list
print("count B:",list.count('B'))

# sort: sắp xếp lại các phần tử trong list theo một thứ tự xác định.
print("sort:",list.sort())

# reverse:  đảo ngược vị trí của các phần tử trong list
list.reverse()
print("reverse:",list)

# copy
list.copy()
print("copy:",list)

# clear: xóa bỏ hết tất cả các phần tử trong list.
list.clear()
print("clear:",list)

# Xem thêm: https://www.w3schools.com/python/python_lists_methods.asp