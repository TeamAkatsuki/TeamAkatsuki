package chap02;

public class CheckValueBeforeCasting {
	public static void main(String[] args) {
		int i = 128;
		
		if((i<Byte.MIN_VALUE) || (i>Byte.MAX_VALUE)) {
			System.out.println("byte Ÿ������ ��ȯ�� �� �����ϴ�.");
			System.out.println("���� �ٽ� �� �ּ���.");
			// || = or , && = and
		}else {
			byte b = (byte) i;
			System.out.println("���� Ÿ�� ��ȯ ��: " + b);
		}
	}

}
