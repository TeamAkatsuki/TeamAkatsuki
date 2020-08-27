package chap02;

public class FromIntToFloat {
	public static void main(String[] args) {
		int num1 = 123456780;
		int num2 = 123456780;
		System.out.println("원래 num2 = " + num2 + '\n');
		float num3 = num2;
		num2 = (int)num3;
		// num2가 float로 갔다가 int로 다시 돌아옴
		
		int result = num1 - num2;
		
		System.out.println("float으로 보낸 num2 = " + num3);
		System.out.println("다시 int로 돌아온 num2 = " + num2);
		System.out.println("변화폭 = " + result + "\n");
		///////////////////////////////////////////////////////////////////////
		
		
		num2 = 123456780;
		double num4 = num2;
		System.out.println("double로 보낸 num2 = " + num4);
		
		num2 = (int)num4;
		System.out.println("다시 int로 온 num2 = " + num2);
		
		int result2 = num1 - num2;
		System.out.println("변화폭 = " + result2);
		
		// float 자료형보다 double형이 정확히 표현할 수 있는 범위가 더 크기 때문에 일어나는 차이
	}

}
