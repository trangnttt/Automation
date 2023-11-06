package Bai_tap;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class bt_for_6 {
	// Đảo ngược các phần tử trong mảng
	public static void main(String args[]) {
		int[] src = {0, 1, 2, 3, 4, 5};
        System.out.println(Arrays.toString(src)); 
        /*Đảo ngược mảng trong Java bằng vòng lặp*/
        for (int i = 0, j = src.length - 1; i < j; i++, j--){
            /*Tạo biến temp và tiến hành hoán đổi phần tử*/
            int temp = src[i];
            src[i]  = src[j];
            src[j] = temp;
        }
        System.out.println(Arrays.toString(src)); 
        
     // Đảo ngược  chuỗi các phần tử trong mảng
     // Tạo và in mảng ban đầu
        String[] name = {"Ha Noi", "Nam Dinh", "Thanh Hoa", "Ninh Binh"};
        System.out.println(Arrays.toString(name)); 
        
        // Chuyển mảng ban đầu sang dạng list
        List list = Arrays.asList(name);
        // Đảo ngược list 
        Collections.reverse(list);

        // Chuyển list thành mảng kết quả
        String[] name2 = (String[])list.toArray(new String[3]);
        System.out.println(Arrays.toString(name2)); 
	}
}
