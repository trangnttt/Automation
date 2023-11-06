package Array;

public class Mang_Array {
	public static void main (String[] args) {
		int a[] = new int[3]; // khai báo & khởi tạo mảng
		a[0] = 10; // gán giá trị
		a[1] = 20;
		a[2] = 50;
		
		System.out.println("mảng i: ");
		for (int i=0; i< a.length; i++) {
			System.out.println(a[i]);
		}

		// gán mảng nặc danh cho mảng b
		int b[] = {10, 20, 30};
		System.out.println("gán mảng nặc danh cho mảng b: ");
		for (int j=0; j< b.length; j++) {
			System.out.println(a[j]);
		}
		
	}
}
