package Bai_tap;

public class bt_basic_4 {
//	Tính lãi xuất kép:	P (1 + R/n)^(nt) - P
//	Tính lãi xuất: Lãi xuất = (P × R × T)/100
	public void TinhLaiKep(int p, int t, double r, int n) {
		 double amount = p * Math.pow(1 + (r / n), n * t);
	     double LaiKep = amount - p;
		System.out.println("Lãi xuất kép = " + LaiKep + "$");
	}
	public void TinhLaiXuat(int p, double r, int t) {
		double LaiXuat = (p * r * t)/100;
		System.out.print("Lãi xuất = " + LaiXuat + "$");
		
	}
	public static void main (String[] args) {
		bt_basic_4 result = new bt_basic_4();
		bt_basic_4 result1 = new bt_basic_4();
		result.TinhLaiKep(2000, 5, 0.08, 12);
		result1.TinhLaiXuat(2000, 6, 3);
		
	}

}
