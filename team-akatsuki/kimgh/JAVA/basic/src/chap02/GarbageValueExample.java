package chap02;

public class GarbageValueExample {
	public static void main(String[] args) {
		byte var1 = 125;
		int var2 = 125;
		
		for (int i = 0; i < 5; i++) {
			var1++;
			var2++;
			System.out.println("byte var1: " + var1 + "\t" + "int var2: " + var2);
			
			/* �ŷ��� �� ����, �� �� ���� �� = GarbageValue
			 * �����÷ο��� �����, �ִ밪�� �پ� �Ѵ� ���� ���Ͽ� ������ ���� �Ǵ� ��
			 *  */
			
		}
	}
}
