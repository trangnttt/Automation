import datetime

ngay_gio = datetime.datetime.now()
gio = datetime.datetime.today().time()
ngay = datetime.datetime.today().date()
print("Ngày giờ hiện tại là", ngay_gio)
print("Giờ hiện tại là", gio)
print("Ngày tháng hiện tại là", ngay)

nam= ngay_gio.year
ngay = ngay_gio.day
thang = ngay_gio.month

print("Năm hiện tại là", nam)
print("Ngày hiện tại là", ngay)
print("Tháng hiện tại là", thang)

file_date = ngay_gio.strftime('%Y-%m%d %H:%M:%S')
print(file_date)

# Đọc thêm strftime: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes