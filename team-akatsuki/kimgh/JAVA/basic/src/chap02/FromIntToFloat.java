package chap02;

public class FromIntToFloat {
	public static void main(String[] args) {
		int num1 = 123456780;
		int num2 = 123456780;
		System.out.println("���� num2 = " + num2 + '\n');
		float num3 = num2;
		num2 = (int)num3;
		// num2�� float�� ���ٰ� int�� �ٽ� ���ƿ�
		
		int result = num1 - num2;
		
		System.out.println("float���� ���� num2 = " + num3);
		System.out.println("�ٽ� int�� ���ƿ� num2 = " + num2);
		System.out.println("��ȭ�� = " + result + "\n");
		///////////////////////////////////////////////////////////////////////
		
		
		num2 = 123456780;
		double num4 = num2;
		System.out.println("double�� ���� num2 = " + num4);
		
		num2 = (int)num4;
		System.out.println("�ٽ� int�� �� num2 = " + num2);
		
		int result2 = num1 - num2;
		System.out.println("��ȭ�� = " + result2);
		
		// float �ڷ������� double���� ��Ȯ�� ǥ���� �� �ִ� ������ �� ũ�� ������ �Ͼ�� ����
	}

}
