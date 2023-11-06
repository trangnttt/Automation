package Vong_lap_for;

public class Thuc_hanh {
	public static void main (String[] args) {
		System.out.println("Vòng lặp for đơn giản: ");
		for (int i = 0; i <=5; i++) {
			// in ra từ 1 -> 5
			System.out.println(i);
		}
		// Vòng lặp for cải tiến 
		int arr[] = {12, 24, 32, 48};
		System.out.println("Vòng lặp for cải tiến: ");
		for (int i : arr) {
			System.out.println(i);
		}
		// Vòng lặp for gắn nhãn
		System.out.println("Vòng lặp for gắn nhãn: ");
		aa: for (int i = 1; i <= 3; i++) {
            bb: for (int j = 1; j <= 3; j++) {
                if (i == 2 && j == 2) {
                    break aa;
                }
            	System.out.println(i + " " + j);
            }
        }
		
	}
}
