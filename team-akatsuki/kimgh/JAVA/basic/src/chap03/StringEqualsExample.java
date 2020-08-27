package chap03;

public class StringEqualsExample {
	public static void main(String[] args) {
		String strVal1 = "무농주";
		String strVal2 = "무농주";
		
		// Val1과 Val2의 주소가 같은 이유는 Val1이 저장되고 나서 Val2의 값은 기존에 저장되어 있던
		// 주소에서 추출하기 때문... 개신기
		
		String strVal3 = new String("무농주");
		
		// 값을 비교하는 것이 아니라 값이 저장되어 있는 주소를 비교하는 것이므로 다르다.
		
		System.out.println(strVal1);
		System.out.println(strVal2);
		System.out.println(strVal3);
		
		System.out.println(strVal1 == strVal2);
		System.out.println(strVal1 == strVal3);
	}

}
