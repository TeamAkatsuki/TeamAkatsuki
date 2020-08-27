package chap02;

public class PromotionExample {
	
	public static void main(String[] args) {
		
		byte byteValue = 10;
		int intValue = byteValue; // byte -> int promoted
		System.out.println(intValue);
		
		char charValue = '��';
		intValue = charValue; // char -> int promoted
		System.out.println("���� �����ڵ� = " + intValue);
		
		intValue = 500;
		long longValue = intValue; // int -> long promoted
		System.out.println(longValue);
		
		intValue = 200;
		double doubleValue = intValue; // int -> double promoted
		System.out.println(doubleValue);
		
	}
}
