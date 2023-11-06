package mypack;

//VD Da_hinh là con của Bike
//class Bike {
//	void run() {
//		System.out.println("Chạy");
//	}
//}
//
//public class Da_hinh extends Bike {
//	void run() {
//		System.out.println("Chạy thật nhanh");
//	}
//	public static void main(String[] args) {
//		
//		Bike bk = new Bike();
//		Bike bk1 = new Da_hinh(); // Upcasting
//		bk.run();
//		bk1.run(); // tính đa hình nè thực hiện một hành động bằng nhiều cách khác nhau
//	}
//}

//-- Bài tập: Bank là một lớp cung cấp chức năng xem thông tin tỷ lệ lãi suất. 
//Nhưng mỗi ngân hàng có một lãi xuất khác nhau, 
//ví dụ các ngân hàng SBI, ICICI và AXIS có tỷ lệ lãi suất lần lượt là 8%, 7% và 9%

class Bank {
	int getRateOfInterest() {
		return 0;
	}
}
class SBI extends Bank {
	int getRateOfInterest() {
		return 8;
	}
}
class ICICI extends Bank {
	int getRateOfInterest() {
		return 9;
	}
}
class AXIS extends Bank {
	int getRateOfInterest() {
		return 10;
	}
}

public class Da_hinh {
	public static void main(String[] args) {
		Bank b1 = new SBI();
		Bank b2 = new ICICI();
		Bank b3 = new AXIS();
		System.out.println("VCB lai suat la: " + b1.getRateOfInterest());
        System.out.println("ICICI lai suat la: " + b2.getRateOfInterest());
        System.out.println("AXIS lai suat la: " + b3.getRateOfInterest());
	}
}