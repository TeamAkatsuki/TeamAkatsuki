package chap03;

public class LogicalOperatorExample {
	public static void main(String[] args) {
		int charCode = 'A';
		
		if((charCode >= 65) & (charCode<=90)) {
			System.out.println("���ĺ� �빮���Ӵϴ�");
		}
		
		if((charCode >= 97) & (charCode <= 122)) {
			System.out.println("���ĺ� �ҹ����Ӵϴ�");
		}
		
		if(!(charCode < 48) && !(charCode > 57)) {
			System.out.println("�����Ӵϴ�");
		}
		
		int value = 6;
		if ((value % 2 == 0) | (value % 3 == 0 )) {
			System.out.println("2 �Ǵ� 3�� ����Ӵϴ�.");
			
		}
		if ((value % 2 == 0) || (value % 3 == 0)) {
			System.out.println("2 �Ǵ� 3�� ����Ӵϴ�.");
		}
	}

}
