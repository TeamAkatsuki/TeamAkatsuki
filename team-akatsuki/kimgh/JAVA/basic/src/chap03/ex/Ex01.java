package chap03.ex;

public class Ex01 {
	public static void main(String[] args) {
		// ����  ! �Է��� 90�� �̻��̸� A, 80�� �̻��̸� B, 70�� �̻��̸� C 60�� �̻��̸� D!
		int score = 87;
		
		char grade = (score >= 90 ? 'A' : (score >= 80 ? 'B' : (score >= 70 ? 'C' : 'D')));
		System.out.println("����� " + grade + "�Ӵϴ�");
		
	}

}
