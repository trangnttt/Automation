package Bai_tap;
import java.util.Arrays;

public class bt_chuoi_2 {
//	Đảo chuỗi
	public void DaoChuoi(String str) {
		String[] words = str.split(" "); // split tách chuỗi return mảng
		String reversedString = "";
		for (int i = 0; i < words.length; i++)
        {
            String word = words[i];
            String reverseWord = "";
            for (int j = word.length()-1; j >= 0; j--)
            {
                reverseWord = reverseWord + word.charAt(j);
            }
            reversedString = reversedString + reverseWord + " ";
        }
		 System.out.println(str);
        System.out.println(reversedString);

	}
	
	
	
	 public static void main(String args[])
	    {
		 bt_chuoi_2 bt = new bt_chuoi_2();
		 bt.DaoChuoi("Hello nha");
	    }
	

}
