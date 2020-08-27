package chap05;

public class MainStringArrayArgument {
	public static void main(String[] args) {
		if(args.length != 2) {// 인수 갯수가 2가 아니면 사용법 표시
			System.out.println("프로그램 사용법");
			System.out.println("java" + "MainStringArrayArgument num1 num2");
			System.exit(0);
		}
		
		String strNum1 = args[0];// 부여받은 인수를 객체에 저장
		String strNum2 = args[1];
		
		int num1 = Integer.parseInt(strNum1); //그 객체를 정수형으로 전환하여 변수에 저장
		int num2 = Integer.parseInt(strNum2);
		
		int result = num1 + num2;
		System.out.println(num1 + " + " + num2 + " = " + result);
		
		
	}

}
