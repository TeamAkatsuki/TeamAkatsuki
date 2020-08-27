package chap03;

public class AccuracyExample {
	public static void main(String[] args) {
		int apple = 1;
		double pieceUnit = 0.1;
		int number = 7;
		
		double result = apple - number * pieceUnit;
		System.out.println("사과 한 개에서 0.7조각을 빼면");
		System.out.println(result + "조각?");
		
		// float이나 double, 실수형은 0.1을 정확하게 표기하지 못함...
		
		int apple2 = 1;
		int totalPieces = apple2 * 10;
		
		int number2 = 7;
		int temp = totalPieces - number2;
		
		double result2 = temp / 10.0;
		
		System.out.println("사과 한 개에서 0.7조각을 빼면");
		System.out.println(result2 + "조각!");
		
		
		
	}
}
