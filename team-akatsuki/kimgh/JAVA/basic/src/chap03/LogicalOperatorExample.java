package chap03;

public class LogicalOperatorExample {
	public static void main(String[] args) {
		int charCode = 'A';
		
		if((charCode >= 65) & (charCode<=90)) {
			System.out.println("알파벳 대문자임니다");
		}
		
		if((charCode >= 97) & (charCode <= 122)) {
			System.out.println("알파벳 소문자임니다");
		}
		
		if(!(charCode < 48) && !(charCode > 57)) {
			System.out.println("숫자임니다");
		}
		
		int value = 6;
		if ((value % 2 == 0) | (value % 3 == 0 )) {
			System.out.println("2 또는 3의 배수임니다.");
			
		}
		if ((value % 2 == 0) || (value % 3 == 0)) {
			System.out.println("2 또는 3의 배수임니다.");
		}
	}

}
