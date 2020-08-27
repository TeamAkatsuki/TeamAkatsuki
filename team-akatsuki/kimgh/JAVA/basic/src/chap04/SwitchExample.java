 package chap04;

public class SwitchExample {
	public static void main(String [] args) {
		int num = (int)(Math.random() * 6) + 1; 
		// 0 <= x < 1 사이의 값을 출력 num은 연산결과 1~6 사이의 랜덤
		String num2 = "1";
		
		
		switch(num) { 
		//switch - case - default -> switch 뒤의 인수를 case와 비교, 비교, 
		// 그 이외의 경우default 수행
		
		case 1:
			System.out.println("1이 나왔습니다.");
			break;
			
		case 2:
			System.out.println("2가 나왔습니다.");
			break;
			
		case 3:
			System.out.println("3이 나왔습니다.");
			break;
			
		case 4:
			System.out.println("4가 나왔습니다.");
			break;
			
		case 5:
			System.out.println("5가 나왔습니다.");
			break;
			
		default :
			System.out.println("6이 나왔습니다.");
			break;
			
		}
		
	}

}
