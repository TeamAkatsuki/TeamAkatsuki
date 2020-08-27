package chap02;

public class GarbageValueExample {
	public static void main(String[] args) {
		byte var1 = 125;
		int var2 = 125;
		
		for (int i = 0; i < 5; i++) {
			var1++;
			var2++;
			System.out.println("byte var1: " + var1 + "\t" + "int var2: " + var2);
			
			/* 신뢰할 수 없는, 쓸 데 없는 값 = GarbageValue
			 * 오버플로우의 결과물, 최대값을 뛰어 넘는 값을 더하여 엉뚱한 값이 되는 것
			 *  */
			
		}
	}
}
