package chap02;

public class FloatDoubleExample {
	public static void main(String[] args) {
		double var1 = 3.141592;
		
		// float var2 = 3.14; //컴파일 에러(type mismatch)
		// 자바에서는 소숫점을 찍으면 기본적으로 double로 인식하기 때문에
		// Type mismatch 발생
		
		float var3 = 3.14f;
		
		// 실수 뒤에 f를 적으면 double이 아니라 float으로 인식
		
		double var4 = 0.1234567890123456789;
		float var5 = 0.1234567890123456789f;
		
		System.out.println("var1 : " + var1);
		System.out.println("var3 : " + var3);
		System.out.println("var4 : " + var4);
		System.out.println("var5 : " + var5);
		
						
	}
}
