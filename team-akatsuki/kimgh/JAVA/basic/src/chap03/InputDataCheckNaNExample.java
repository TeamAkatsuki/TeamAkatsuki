package chap03;

import java.util.Currency;

public class InputDataCheckNaNExample {
	public static void main(String[] args) {
		String userInput = "NaN";
		double val = Double.valueOf(userInput);
		//Double.valueOf(String s) ���ڿ��� ����� �ٲ۴�.
		
		double currentBalance = 10000.0;
		
		if(Double.isNaN(val)) {
			System.out.println("NaN�̹Ƿ� �� �ƻ��� ���Ѵ� �̰;�");
			val = 0.0;
		}
		currentBalance += val;
		System.out.println("���� �ܰ�� :  " + currentBalance);
		
	}
}
