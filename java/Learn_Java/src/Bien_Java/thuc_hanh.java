package Bien_Java;

public class thuc_hanh {
	public String name = "Phero"; // biến instance (biến toàn cục)
	
	public static String job = "QC"; // biến staic
	
	public void getInfo() {
		int age = 30;  // biến cục bộ
		float weight = 76.5f; // biến cục bộ
		boolean gender = true;
		System.out.println("Name: " + name);
		System.out.println("Age: " + age);
		System.out.println("Weight: " + weight);
		System.out.println("Gender: " + gender);
		System.out.print("Job: " + job);
	}
	
//	biến instance không để vào hàm main để gọi ra được => nên mình dùng hàm getInfo() để gọi qua
	
	public static void main (String[] args) {
		thuc_hanh info = new thuc_hanh();
		info.getInfo();
	}
}
