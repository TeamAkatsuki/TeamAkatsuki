package chap03;

public class CheckOverflowExample {
	public static void main(String[] args) {
		try {
			int result = safeAdd(2000000000,2000000000);
			System.out.println(result);
			
		}catch(ArithmeticException e) {
			System.out.println("오버플로우 발생" + " 정확한 계산 불가");
			
		}	
	}
	public static int safeAdd(int left, int right) {
		if(right > 0) {
			if((left) > (Integer.MAX_VALUE - right)) {
				throw new ArithmeticException("오버플로우 발생");
				
			}
		}else {
			if((left) < (Integer.MIN_VALUE - right)) {
				
				throw new ArithmeticException("오버플로우 발생");
				
			}
		}
		return left + right;
		
			}
}
