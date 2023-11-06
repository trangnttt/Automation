package Bai_tap;

public class bt_for_1 {
	public static void main (String [] agrs) {
		// các phần tử trùng nhau
		int arr[] = {10,20,20,30,30,40,50,50};
		System.out.println("các phần tử trùng nhau:");  
		for (int i=0; i<arr.length; i++) {
			for(int j= i+1; j < arr.length; j++) {
				if(arr[i] == arr[j])  {
					System.out.print(arr[j]);  
				}
			}
		}
		
	}
}
