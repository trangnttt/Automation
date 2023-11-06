package Bai_tap;
import java.util.*;

public class bt_basic_3 {
	public static void main (String[] agrs) {
//		Kiểm tra nguyên âm và phụ âm  sử dụng Switch Case
		Scanner sc = new Scanner(System.in);
		boolean check = true;
		System.out.println("Nhập vào kí tự cần kiểm tra : "); 
		char ch = sc.next().charAt(0);
		switch (ch) {
			case 'u' :
				check = true;
				break;
			case 'e' :
				check = true;
				break;
			case 'o' :
				check = true;
				break;
			case 'a' :
				check = true;
				break;
			case 'i' :
				check = true;
				break;
			default: 
				check = false;
		}
		if (check == true) {
			System.out.println("Nguyên âm"); 
		}
		else {
			if((ch>='a'&&ch<='z')||(ch>='A'&&ch<='Z')) {
				System.out.println("Phụ âm"); 
			}
			else {
				System.out.println("Không phải chữ cái hợp lệ"); 
			}
		}
		
	}
}
