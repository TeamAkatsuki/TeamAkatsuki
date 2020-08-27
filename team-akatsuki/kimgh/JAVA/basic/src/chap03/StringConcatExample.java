package chap03;

public class StringConcatExample {
	public static void main(String[] args) {
		String str1 = "JDK " + 6.0;
		String str2 = str1 + " 특징";
		
		System.out.println(str2);
		
		String str3 = "JDK" + 3 + 3.0;
		String str4 = 3 + 3.0 + "JDK";
		
		
		System.out.println(str3);
		System.out.println(str4);
		System.out.println(str4.concat(str3));
		// +와 결과가 같긴 한데 잘 안 쓴다. 그냥 + 쓴다
	}

}
