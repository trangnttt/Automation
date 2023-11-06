package Bai_tap;
import java.util.*;
public class bt_basic_5 {
//	Tìm phần nguyên và phần dư
	public static void main(String[] args) {
		int num1, num2;
		Scanner sc = new Scanner(System.in);
		System.out.print("Nhập số thứ nhất: ");
		num1 =  sc.nextInt();
		System.out.print("Nhập số thứ hai: ");
		num2 =  sc.nextInt();
		int phan_nguyen = num1 / num2;
		int phan_du = num1 % num2;

		System.out.println("Phần nguyên = " + phan_nguyen);
		System.out.println("Phần dư = " + phan_du);
		
	}
	
	
}
