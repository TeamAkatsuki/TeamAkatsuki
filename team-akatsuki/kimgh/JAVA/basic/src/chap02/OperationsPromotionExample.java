package chap02;

public class OperationsPromotionExample {
	public static void main(String[] args) {
		
		byte byteValue1 = 10;
		byte byteValue2 = 20;
		
		byte byteValue3 = (byte)(byteValue1 + byteValue2);
		System.out.println(byteValue3);
		int intValue1 = byteValue1 + byteValue2;
		System.out.println(intValue1);
		
		// ���� ������ �⺻ �ڷ����� int. casting�� ����� byte�� ����.
		// �� �����ڸ� 4byte ������ �����ϱ� ����.
		
		char charValue1 = 'A';
		char charValue2 = 1;
//		char charValue3 = charValue1 + charValue2;
		// 'A1'�� ������� �ʴ´�. char ������ ������ �ǹ̰� ����. 
		
		char charValue3 = (char)(charValue1+charValue2);
		System.out.println(charValue3);
		
		// �����ڵ�� �̿��ϰ� ���� ���� �ƴϸ� �ǹ� ����.
		
		int intValue2 = charValue1 + charValue2;
		
		System.out.println("�����ڵ� : " + intValue2);
		System.out.println("��¹��� : " + (char)intValue2);
		
		// ���� ��
		
		int intValue3 = 10;
		int intValue4 = intValue3/4;
		System.out.println(intValue4);
		
		//int�� ���� �ۿ� �������� �����Ƿ� 2.5�� �ƴ϶� 2�� �����
		
		double doubleValue1 = intValue3/4;
		double doubleValue2 = intValue3/4.0;
		System.out.println(doubleValue1);
		System.out.println(doubleValue2);
		
		//���������� �������� ��Ÿ���� �ʰ� ����������
        //double�� �ν��ϰ� ����� �ָ� 2.5�� �ȴ�
		
		int intValue5 = 10;
        //int intValue6 = intValue5 / 4.0;
		//�Ǽ������� ������ �Ǽ��� �����Ƿ� int �ȿ� ���� �� ����
		
		
		
		
	}
}
