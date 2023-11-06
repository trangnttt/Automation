package Bai_tap;

public class bt_for_4 {
	//	Tính trung bình cộng các số trong mảng
	public static void main (String[] args) {
		double[] arr = {19, 12.89, 16.5, 200, 13.7};
        double total = 0;
        for (int i=0; i < arr.length; i++) {
        	total += arr[i];
        }
        double average = total / arr.length;
        System.out.format("Kết quả là: %.3f", average);
       
	}
}
