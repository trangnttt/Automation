package Bai_tap;
import java.util.Scanner;

//Chương trình ATM 
public class bt_number_1 {
	
	public static void main (String[] args) {
		int so_du = 100;
		int tien_gui, tien_rut, choice;
		Scanner sc = new Scanner(System.in);
		while(true) {
			System.out.println("------ ATM ------");
			System.out.println("Nhập phím 1 để rút tiền");
			System.out.println("Nhập phím 2 để gửi tiền");
			System.out.println("Nhập phím 3 để kiểm tra số dư");
			System.out.println("Chọn 4 để Kết thúc");
			System.out.println("------------");
			System.out.print("Mời bạn chọn: ");
			choice = sc.nextInt();
			switch (choice) {
			case 1:
				System.out.print("Nhập số tiền:");
                //Nhập số tiền từ user
                tien_rut = sc.nextInt();
                if (so_du >= tien_rut) {
                	//Sau khi rút, số dư trong tài khoản bị trừ đi số tiền vừa rút
                    so_du = so_du - tien_rut;
                    System.out.println("Hãy nhận tiền từ ATM! Cảm ơn bạn đã sử dụng ATM!");
                    break;
                }
                else
                {
                    //Hiển thị lỗi không đủ tiền để thanh toán
                    System.out.println("Số dư không đủ, vui lòng nạp tiền để có thể thực hiện dịch vụ.");
                }
			case 2:
				 
                System.out.print("Nhập số tiền:");
                //Lấy số tiền gửi từ user
                tien_gui = sc.nextInt();

                //Số dư tăng sau khi cập nhật số tiền gửi vào
                so_du = so_du + tien_gui;
                System.out.println("Bạn đã gửi tiền thành công! Cảm ơn bạn đã sử dụng ATM!");
                System.out.println("");
                break;

            case 3:
                //Hiển thị toàn bộ số dư của user
                System.out.println("Số dư hiện tại của bạn : "+so_du + "VNĐ");
                System.out.println("Cảm ơn bạn đã sử dụng ATM !");
                break;

            case 4:
                System.exit(0);
		}
		}
	}

}
