package chap04;

public class IfElseifElseExample {
	public static void main(String[] args) {
		int score = 75;
		
		if(score >= 90) {
			System.out.println("90 - 100 ������ �����Դϴ�.");
			System.out.println("A���");
		}else if(score >= 80) {
			System.out.println("80-89 ������ �����Դϴ�.");
			System.out.println("B���");
		}else if(score >= 70) { 
			System.out.println("70-79 ������ �����Դϴ�.");
			System.out.println("C���");
		}else {
			System.out.println("0-69 ������ �����Դϴ�.");
			System.out.println("D���");
		}
	}
}
