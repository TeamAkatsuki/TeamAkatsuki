package chap03;

public class SignOperatorExample {
	public static void main(String[] args) {
		int x = -100;
		int result1 = +x;
		int result2 = -x;
		System.out.println("result1 = " + result1);
		System.out.println("result2 = " + result2);
		
		short s = 100;
//		short result3 = -s;
//		부호 연산만 하더라도 int로 산출되기 때문에 int보다 작은 타입에 값을 넣을 수 없다.
		
		int result3 = -s;
		System.out.println("result3 = " + result3);
		
	}
}
