*** JAVA BASIC *** 

1. *** Cách đặt tên *** 
- Bắt đầu bằng chữ cái, _ , $
- Có phân biệt chữ hoa và chữ thường

 *** Cú pháp *** 
DataType varName [ = value] [, varName2] [ = value2]...;
VD: String a = "java";

2. *** Biến trong java ***
- Local  (biến cục bộ)
- Instance (biến toàn cục) => biến Instance không gọi lại được trong hàm static
- Static
Xem thêm ví dụ ở KhaiNiem.java sẽ hiểu

3. *** Kiểu dữ liệu ***

- KDL nguyên thuỷ (string, int, float, boolean ,..)
- KDL đối tượng (array, class, interface)

4. *** Toán tử ***
5. *** If else ***

    if (condition) {
        // khối lệnh này được thực thi
        // nếu condition = true
    } else {
        // khối lệnh này được thực thi
        // nếu condition = false
    }

hoặc

    if (condition1) {  
        // khối lệnh này được thực thi 
        // nếu condition1 là true  
    } else if (condition2) {  
        // khối lệnh này được thực thi 
        // nếu condition2 là true  
    }  else if (condition3) {  
        // khối lệnh này được thực thi 
        // nếu condition3 là true  
    }  
    ...  
    else {  
        // khối lệnh này được thực thi 
        // nếu tất cả những điều kiện trên là false                 
    }

6. *** Switch Case ***

    switch (bieu_thuc) {    
        case gia_tri_1:
            // Khối lệnh 1
            break;  //tùy chọn
        case gia_tri_2:    
            // Khối lệnh 2
            break;  //tùy chọn
        ......    
        case gia_tri_n:    
            // Khối lệnh n
            break;  //tùy chọn    
        default:     
            // Khối lệnh này được thực thi 
            // nếu tất cả các điều kiện trên không thỏa mãn 
    }

=> không có break nó sẽ in ra tất cả các điều kiện

7. *** Vòng lặp for ***
- Vòng lặp for đơn giản (VD: for(int i=0 ; i <=10; i++))
- Vòng lặp for cải tiến (sử dụng để lặp mảng array)
    for (Type var : array) {  
        // Khối lệnh được thực thi
    } 
- Vòng lặp for gắn nhãn 
    ten_nhan:
    for (khoi_tao_bien ; check_dieu_kien ; tang/giam_bien) {  
        // Khối lệnh được thực thi
    }  


8. *** Mảng Array ***

- Mảng 1 chiều ví dụ a[0] = 1;
- Mảng nặc danh a[] = {1,2,3};
- Truyền mảng vào phương thức

*** Java OOP hướng đối tượng *** 

1. *** Đối tượng *** 
- Một thực thể có trạng thái và hành vi được gọi là đối tượng. VD: máy pha cà phê, xe đạp, bút chì,...
- Một đối tượng có 3 đặc điểm: 
    + Trạng thái
    + Hành vi
    + Danh tính (được cài đặt thông qua một ID nhất định)
VD: Bút chì là 1 đối tượng. Tên là A, có màu cam là trạng thái. Dùng để viết là hành vi

2. *** Class *** 
- Là một nhóm các đối tượng có thuộc tính chung, nó là 1 mẫu hoặc thiết kế từ đó các đối tượng được tạo ra.

3. *** Phạm vi truy cập *** 
Có 4 loại phạm vi truy cập:
- Private: chỉ được truy cập trong phạm vi lớp.
- (Default): chỉ được phép truy cập trong cùng package.
- Protected: được truy cập bên trong package và bên ngoài package nhưng phải kế thừa.
- Public: được truy cập ở mọi nơi.

4. *** Tính kế thừa (extends) *** 
    class <tên lớp con> extends <tên lớp cha> {

    }

- Từ khóa super để cho lớp con truy cập các những thứ liên quan đến lớp cha
*** NOTE ***  “Cha có thì con có, con có chưa chắc cha đã có”
=> Xem file Person.java , StudentKeThua.java, Ke_thua.java
Person(cha) -> StudentKeThua(con) kế thừa từ cha -> Ke_thua đem ra xài
5. *** Tính đóng gói (encapsulation) *** 
-  Là kỹ thuật ẩn giấu thông tin không liên quan và hiện thị ra thông liên quan.
=> Xem file StudentKeThua.java, Dong_Goi.java
Dùng getName() return name, setName() gọi this.name = name
Thằng Dong_Goi tạo đối tượng StudentKeThua xài

6. *** Tính đa hình (Polymorphism) *** 
- Thực hiện một hành động bằng nhiều cách khác nhau
=> Xem VD: Da_hinh.java 

*** Q & A ***

*** Câu hỏi 1 ***: Tại sao không thể nạp chồng phương thức bằng cách chỉ thay đổi kiểu trả về của phương thức?
Trong java, không thể nạp chồng phương thức bằng cách chỉ thay đổi kiểu trả về của phương thức bởi vì không biết phương thức nào sẽ được gọi.

*** Câu hỏi 2 *** Có ghi đè được phương thức static không?
Không, phương thức static không thể ghi đè được, bằng chứng là đa hình runtime, vấn đề này sẽ được học trong bài sau.

*** Câu hỏi 3 *** Tại sao không ghi đè được phương thức static?
Vì phương thức static được ràng buộc với class còn phương thức instance được ràng buộc với đối tượng. Static thuộc về vùng nhớ class còn instance thuộc về vùng nhớ heap.

*** Câu hỏi 4 *** Có ghi đè phương thức main được không?
Không, vì main là phương thức static.