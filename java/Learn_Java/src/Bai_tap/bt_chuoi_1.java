package Bai_tap;
import java.util.*;

public class bt_chuoi_1 {
	public static void main (String[] args) {
		String txt = "a b";
		// xóa khoảng trắng của chuỗi	
		txt = txt.replace(" ", "");
		System.out.println("Xóa khoảng trắng của chuỗi:	" + txt);
		
		// viết hoa ký tự đầu tiên
		String first_txt = txt.substring(0, 1); // kí tự đầu
		first_txt = first_txt.toUpperCase(); // viết hoa
		String second = txt.substring(1, txt.length()); // phần còn lại 

		System.out.println("Viết hoa ký tự đầu tiên: " + first_txt + second);
		
		// chuyển chữ thường thành chữ hoa
		System.out.println("Chuyển chữ thường thành chữ hoa:	 " + txt.toUpperCase());
		
		// chuyển chữ hoa thành chữ thường bằng Scanner
		Scanner sc = new Scanner(System.in);
		String text;
		System.out.println("Nhập chuỗi chữ hoa: ");
		text = sc.nextLine();
		System.out.println(text + " chuyển thành " + text.toLowerCase());
		
	}
}
