package mypack;

public class Student2 {
	int id;
	String name;
	
	// phương thức insertRecord
	public void insertRecord(int id, String name) {
		this.id = id;
		this.name = name;
	}
	
	// phương thức displayInformation
	 public void displayInformation() {
		System.out.println(id + " " + name);
	}
	
	 public static void main(String args[]) {
		 Student2 s = new Student2();
         
         s.insertRecord(111, "Phero");
         s.displayInformation();
	 }
}