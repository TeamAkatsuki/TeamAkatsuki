package chap03;

public class IncreaseDecreaseOperatorExample {
	public static void main(String[] args) {
		int x = 10 ;
		int y = 10 ;
		int z ;
		
		System.out.println("-------------");
		
		x++;
		++x;
		System.out.println("x = " + x);
		
		y--;
		--y;
		System.out.println("y = " + y);
		
		System.out.println("-------------");
		
		z = x++;
		System.out.println("z = " + z);
		System.out.println("x = " + x);
		
		System.out.println("-------------");
		
		z = ++x;
		System.out.println("z = " + z);
		System.out.println("x = " + x);
		
		System.out.println("-------------");
		
		z = ++x + y++;
		System.out.println("z = " + z);
		
		// x = 15 y = 8�� ���¿��� ����
		
		System.out.println("x = " + x);
		System.out.println("y = " + y);
		
		// ���� �Ŀ��� x = 15, y = 9
		//++�� �ڿ� ������ ��ó�� ++�� �տ� ������ ��ó��
	}

}
