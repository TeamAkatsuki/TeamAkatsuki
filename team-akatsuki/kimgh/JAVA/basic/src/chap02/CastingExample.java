package chap02;

public class CastingExample {
	public static void main(String[] args) {
		 int intValue = 44032;
		 char charValue = (char) intValue;
		 System.out.println(charValue);
		 
		 long longValue = 500;
		 intValue = (int) longValue;
		 System.out.println(intValue);
		 
		 // syso + ctrl + space -> println 자동완성
		 
		 double doubleValue = 3.14;
		 intValue = (int) doubleValue;
		 System.out.println(intValue);
		 
	}

}
