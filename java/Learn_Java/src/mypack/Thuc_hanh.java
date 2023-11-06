package mypack;
//Bạn hãy viết chương trình khai báo lớp Student3 với thông tin giống như sau:
//name, age, phương thức display, getInformation
//class Student thay bằng Thuc_hanh trong bài này
class Student3 {
	String name;
	int age;
	void getInformation(String name, int age) {
		this.name = name;
		this.age = age;
	}
	void display() {
		System.out.println("Name: " + name + "; " + "Age: " + age);
	}
}
public class Thuc_hanh {
	public static void main (String[] args) {
		Student3 bt = new Student3(); //khởi tạo đối tượng
		bt.getInformation("Phero", 30);
		bt.display();
	}
}
