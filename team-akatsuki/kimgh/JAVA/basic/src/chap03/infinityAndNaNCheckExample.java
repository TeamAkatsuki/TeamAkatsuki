package chap03;

public class infinityAndNaNCheckExample {
	public static void main(String[] args) {
		int x =  5;
		double y = 0.0;
		
		// �Ǽ����� 0.0�� �������� 0�� �ָ��ϰ� �ٸ���.
		
		
		double z = x / y;
		double z2 = x % y;
		
		System.out.println("5 / 0.0 = z, z�� infinite�ΰ���?  " + Double.isInfinite(z));
		System.out.println("z�� NaN�ΰ���?  " + Double.isNaN(z));
		System.out.println("5 % 0.0 = z2, z2�� infinite�ΰ���?  " + Double.isInfinite(z2));
		System.out.println("z2�� NaN�ΰ���?  " + Double.isNaN(z2));
		
		System.out.println(z);
		
		// �빮�ڷ� �����ϴ� �Ķ� ǥ�ô� ��ü��, ������ ���� �޼ҵ带 ������ ����
		// �������� ������ �ٸ����� ��ȣ ȣȯ�� �ȴ�.
		
		if(Double.isInfinite(z)) {
			System.out.println("���� �Ұ�");
		}else {
			System.out.println(z+2);
		}


	}
}
