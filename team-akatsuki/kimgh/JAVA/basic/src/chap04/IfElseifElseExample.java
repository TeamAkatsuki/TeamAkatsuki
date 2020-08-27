package chap04;

public class IfElseifElseExample {
	public static void main(String[] args) {
		int score = 75;
		
		if(score >= 90) {
			System.out.println("90 - 100 구간의 점수입니다.");
			System.out.println("A등급");
		}else if(score >= 80) {
			System.out.println("80-89 구간의 점수입니다.");
			System.out.println("B등급");
		}else if(score >= 70) { 
			System.out.println("70-79 구간의 점수입니다.");
			System.out.println("C등급");
		}else {
			System.out.println("0-69 구간의 점수입니다.");
			System.out.println("D등급");
		}
	}
}
