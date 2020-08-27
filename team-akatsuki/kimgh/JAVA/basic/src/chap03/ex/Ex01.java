package chap03.ex;

public class Ex01 {
	public static void main(String[] args) {
		// 문제  ! 입력이 90점 이상이면 A, 80점 이상이면 B, 70점 이상이면 C 60점 이상이면 D!
		int score = 87;
		
		char grade = (score >= 90 ? 'A' : (score >= 80 ? 'B' : (score >= 70 ? 'C' : 'D')));
		System.out.println("등급은 " + grade + "임니다");
		
	}

}
