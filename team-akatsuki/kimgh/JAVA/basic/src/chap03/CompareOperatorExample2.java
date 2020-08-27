package chap03;

public class CompareOperatorExample2 {
	public static void main(String[] args) {
		int v2 = 1;
		double v3 = 1.0;
		System.out.println(v2==v3); //true
		
		double v4 = 0.1;
		float v5 = 0.1f;
		System.out.println(v4==v5); //????? false
		// binary format으로 지수와 가수를 이용하여 수를 파악하는 float은 근사값이다.
		// 정확한 수를 지칭할 수 없다
		
		System.out.println((float)v4 == v5); //??!?!?! true
	}

}
