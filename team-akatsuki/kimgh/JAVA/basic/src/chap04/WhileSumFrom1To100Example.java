package chap04;

public class WhileSumFrom1To100Example {
	public static void main(String [] args) {
		int sum = 0;
		
		int i = 1;
		
		while(i<=100) {
			sum += i;
			i++;
			
		}
		System.out.println("1~" + (i-1) + "гу: " + sum);
	}

}
