package chap02;

public class CharExample {
	public static void main(String [] arg) {
		char c1 = 'A';
		char c2 = 65;
		
		// 65�� ASCII �ڵ��� 65
		// 0~127���� �Ҵ�Ǿ� �ִ� ǥ�� �ڵ�
		// American Standard Code for Information Interchange
		// �̱� ���� ��ȯ ǥ�� ��ȣ
		
		// �����ڵ� - ������ ��� ��� ����
		// Ű���忡�� �ѱ��� ������ ��� ���� ASCII�� ����
		
		char c3 = '\u0041';
		char c4 = '��';
		char c5 = 44032;
		char c6 = '\uac00';
		
		int uniCode = c1; //�����ڵ� ���
		
		//Ÿ�� �ڵ���ȯ
		
		System.out.println(c1);
		System.out.println(c2);
		System.out.println(c3);
		System.out.println(c4);
		System.out.println(c5);
		System.out.println(uniCode);
		
	}

}
