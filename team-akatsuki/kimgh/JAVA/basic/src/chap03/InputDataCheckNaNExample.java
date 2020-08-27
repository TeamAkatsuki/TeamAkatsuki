package chap03;

import java.util.Currency;

public class InputDataCheckNaNExample {
	public static void main(String[] args) {
		String userInput = "NaN";
		double val = Double.valueOf(userInput);
		//Double.valueOf(String s) 문자열을 더블로 바꾼다.
		
		double currentBalance = 10000.0;
		
		if(Double.isNaN(val)) {
			System.out.println("NaN이므로 ㄱ ㅖ산을 못한다 이것아");
			val = 0.0;
		}
		currentBalance += val;
		System.out.println("현재 잔고는 :  " + currentBalance);
		
	}
}
