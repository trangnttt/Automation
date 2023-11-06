package mypack;

public class Annonymous {
	  void fact(int n) {
	        int giaithua = 1;
	        for (int i = 1; i <= n; i++) {
	            giaithua = giaithua * i;
	        }
	        System.out.println("Giai thừa của " + n + "  là: " + giaithua);
	    }
	 
	    public static void main(String args[]) {
	        // gọi phương thức của đối tượng annonymous
	        new Annonymous().fact(5);
	    }
}
