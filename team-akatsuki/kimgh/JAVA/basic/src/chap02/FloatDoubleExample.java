package chap02;

public class FloatDoubleExample {
	public static void main(String[] args) {
		double var1 = 3.141592;
		
		// float var2 = 3.14; //������ ����(type mismatch)
		// �ڹٿ����� �Ҽ����� ������ �⺻������ double�� �ν��ϱ� ������
		// Type mismatch �߻�
		
		float var3 = 3.14f;
		
		// �Ǽ� �ڿ� f�� ������ double�� �ƴ϶� float���� �ν�
		
		double var4 = 0.1234567890123456789;
		float var5 = 0.1234567890123456789f;
		
		System.out.println("var1 : " + var1);
		System.out.println("var3 : " + var3);
		System.out.println("var4 : " + var4);
		System.out.println("var5 : " + var5);
		
						
	}
}
