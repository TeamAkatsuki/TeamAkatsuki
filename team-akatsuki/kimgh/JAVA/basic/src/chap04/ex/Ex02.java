package chap04.ex;

public class Ex02 {
	
	public static void main(String[] args) {
		//while문과 Math.random() 메소드 사용, 두 개의 주사위를 던졌을 때 나오는 눈을 
		//이항 튜플 형태로 표시하고, 5가 아니면 던지고, 5이면 멈추게 만들어봐
		Outter: while(true) {
		int a = (int)(Math.random() * 6) + 1;
		int b = (int)(Math.random() * 6) + 1;
		System.out.println("(" + a + " , " + b + ")");
			
		
		if(a + b == 5) {
			break Outter;
			}
		}
	}
}
