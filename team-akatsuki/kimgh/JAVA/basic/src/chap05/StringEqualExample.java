package chap05;

public class StringEqualExample {
	public static void main(String [] args) {
		String strVar1 = "���ȣ";
		String strVar2 = "���ȣ";
		
		if(strVar1 == strVar2) { // ������ ���Ѵ�
			System.out.println("strVar1�� strVar2�� ������ ����");
		}else {
			System.out.println("������ �ٸ���");
		}
		if(strVar1.equals(strVar2)) { // ���� ���Ѵ�
			System.out.println("strVar1�� strVar2�� ���ڿ��� ����");
		}
		
		String strVar3 = new String("���ȣ");
		String strVar4 = new String("���ȣ"); // new�� ������ ������ ���ο� ��ü�� �����Ѵ�
		
		if(strVar3 == strVar4) {
			System.out.println("strVar3�� strVar4�� ������ ����");
		}else {
			System.out.println("strVar3�� strVar4�� ������ �ٸ���");
		}
		if(strVar3.equals(strVar4)) {
			System.out.println("strVar3�� strVar4�� ���ڿ��� ����");
		}
		
		strVar3 = null;
		
	}

}