package chap03;

public class infinityAndNaNCheckExample {
	public static void main(String[] args) {
		int x =  5;
		double y = 0.0;
		
		// 실수형의 0.0과 정수형의 0은 애매하게 다르다.
		
		
		double z = x / y;
		double z2 = x % y;
		
		System.out.println("5 / 0.0 = z, z는 infinite인가용?  " + Double.isInfinite(z));
		System.out.println("z는 NaN인가용?  " + Double.isNaN(z));
		System.out.println("5 % 0.0 = z2, z2는 infinite인가용?  " + Double.isInfinite(z2));
		System.out.println("z2는 NaN인가용?  " + Double.isNaN(z2));
		
		System.out.println(z);
		
		// 대문자로 시작하는 파란 표시는 객체들, 각자의 내장 메소드를 가지고 있음
		// 엄밀히는 변수와 다르지만 상호 호환은 된다.
		
		if(Double.isInfinite(z)) {
			System.out.println("산출 불가");
		}else {
			System.out.println(z+2);
		}


	}
}
