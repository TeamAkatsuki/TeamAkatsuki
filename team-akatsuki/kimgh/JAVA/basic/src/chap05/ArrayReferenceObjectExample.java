package chap05;

public class ArrayReferenceObjectExample {
	public static void main(String[] args) {
		String[] strArray = new String[3];
		strArray[0] = "Java";
		strArray[1] = "Java";
		strArray[2] = new String("Java");
		
		System.out.println(strArray[0] == strArray[1]); // 주소가 같다 (같은 객체)
		System.out.println(strArray[0] == strArray[2]); // 주소가 다르다 (다른 객체)
		System.out.println(strArray[0].equals(strArray[2])); // 값은 같다
		
	}

}
