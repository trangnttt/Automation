package Bai_tap;

public class bt_basic_2 {
	//Bài 1: Kiểm tra năm nhuận không?
	//	Năm nhuận là năm chia hết cho 400.
	//	Năm nhuận là năm chia hết cho 4 nhưng không chia hết cho 100.
	
	 public static void main(String[] args) {
		 int year = 2023;
		 boolean isLeap = false;
		 
		 if(year % 4 ==0) {	// chia hết cho 4 => nhuận
			 if(year % 100 == 0) { // chia hết cho 4 và 100 => không nhận
				 if(year % 400 ==0) {	// chia hết cho 400 => nhuận
					 isLeap = true;
				 }
				 else {
					 isLeap = false;
				 }
			 }
			 else {
				 isLeap = true;
			 }
			 
		 }
		 else { 
			 isLeap = false;
		 }
		 if(isLeap == false) {
			 System.out.println("Không phải năm nhuận");
		 }
		 else {
			 System.out.println("Năm nhuận");
		 }
	 }
}
