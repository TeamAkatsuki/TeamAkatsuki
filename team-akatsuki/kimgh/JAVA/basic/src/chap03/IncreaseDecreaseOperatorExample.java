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
		
		// x = 15 y = 8인 상태에서 연산
		
		System.out.println("x = " + x);
		System.out.println("y = " + y);
		
		// 연산 후에는 x = 15, y = 9
		//++가 뒤에 있으면 후처리 ++가 앞에 있으면 선처리
	}

}
