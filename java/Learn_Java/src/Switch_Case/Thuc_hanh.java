package Switch_Case;

public class Thuc_hanh {
	public static void main (String[] args) {
		int number = 80;
		switch (number) {
			case 10: 
				System.out.println("Number = " + number);
				break; // không có break nó sẽ in ra hết tất cả
			case 20:
				System.out.println("Number = " + number);
				break;
			case 30:
				System.out.println("Number = " + number);
				break;
			default: 
				System.out.println("Number is not 10, 20 or 30");
		}
	}
}
