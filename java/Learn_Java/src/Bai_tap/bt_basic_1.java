package Bai_tap;
import java.util.Scanner;

public class bt_basic_1 {
	public static void main (String[] args) {
		//Bài 1: Cộng hai số 
		int a,b, total;
		Scanner sc = new Scanner(System.in);
		System.out.print("Nhập a: ");
		a = sc.nextInt();
		System.out.print("Nhập b: ");
		b = sc.nextInt();
		total = a+b;
		System.out.println("a + b = "+total);

		//Bài 2: Kiểm tra số chẵn hay số lẻ
		if (a%2==0) {
			System.out.print("a là số chẵn");
		}
		else {
			System.out.print("a là số lẻ");
		}
	}

}
