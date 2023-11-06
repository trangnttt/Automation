package Bai_tap;
import java.lang.reflect.Array;
import java.util.Arrays;

//sắp xếp các phần tử trong mảng tăng dần
public class bt_for_7 {
	public static void main (String[] args) {
		 int a[] = {1, 2, 5, 6, 3, 2};
		 for (int i=0; i<a.length; i++) {
			 Arrays.sort(a);
			 System.out.print(a[i] + " ");
		 }
	}
}
