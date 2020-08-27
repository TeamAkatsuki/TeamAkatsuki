package chap04;

public class BreakOutterExample {
	public static void main(String [] args) {
		Outter: for(char upper='A'; upper <='Z'; upper++) {
			for(char lower = 'a'; lower <= 'z'; lower++) {
				System.out.println(upper + "-" + lower);
				if(lower == 'g') {
					break Outter;
//					Outter를 빠져나감, Outter가 없으면 가장 가까운 반복문 종료
				}
			}
		}
	System.out.println("종 -- 료");
	}

}
