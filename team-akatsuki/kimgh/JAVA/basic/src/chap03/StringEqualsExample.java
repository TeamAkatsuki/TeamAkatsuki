package chap03;

public class StringEqualsExample {
	public static void main(String[] args) {
		String strVal1 = "������";
		String strVal2 = "������";
		
		// Val1�� Val2�� �ּҰ� ���� ������ Val1�� ����ǰ� ���� Val2�� ���� ������ ����Ǿ� �ִ�
		// �ּҿ��� �����ϱ� ����... ���ű�
		
		String strVal3 = new String("������");
		
		// ���� ���ϴ� ���� �ƴ϶� ���� ����Ǿ� �ִ� �ּҸ� ���ϴ� ���̹Ƿ� �ٸ���.
		
		System.out.println(strVal1);
		System.out.println(strVal2);
		System.out.println(strVal3);
		
		System.out.println(strVal1 == strVal2);
		System.out.println(strVal1 == strVal3);
	}

}
