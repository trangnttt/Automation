package Bai_tap;
import java.lang.reflect.Array;
import java.util.*;


public class bt_for_3 {
	// tìm số nhỏ thứ 2 của mảng 
	public static int getSecondSmallest(int[] a, int total) {
        Arrays.sort(a); // dùng để sắp xếp thứ tự mảng lại là giải được
        return a[1];
    }
	public static void main(String args[]) {
        int a[] = {1, 2, 5, 6, 3, 2};
        int b[] = {44, 66, 99, 77, 33, 22, 55};
        System.out.println("Số nhỏ thứ 2 của Mảng a: " + getSecondSmallest(a, a.length));
        System.out.println("Số nhỏ thứ 2 của Mảng b: " + getSecondSmallest(b, b.length));
    }
	
}
