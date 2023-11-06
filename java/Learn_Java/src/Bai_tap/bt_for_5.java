package Bai_tap;
import java.util.Scanner;

public class bt_for_5 {
//	Tính tổng các số trong mảng trong Java
	public static void main (String[] args) {
		
		double[] arr1 = {2,3,1};
        double total1 = 0;
        for (int i=0; i < arr1.length; i++) {
        	total1 += arr1[i];
        }
        System.out.println("Kết quả 1 là: " + total1);
		
        // dùng Scanner
		
		Scanner sc = new Scanner(System.in);
		System.out.println("Nhập vào số phần tử trong mảng: ");
		int n = sc.nextInt();
        double[] arr = new double[n];
        double total = 0;
        for(int i=0; i<arr.length; i++){
            System.out.print("Nhập vào giá trị cho phần tử thứ "+(i+1)+": ");
            arr[i] = sc.nextDouble();
        }
        for(int i=0; i<arr.length; i++){
            total = total + arr[i];
        }
        System.out.format("Kết quả là: %.3f", total);
		
		
	}
}
