package chap02;

public class OperationsPromotionExample {
	public static void main(String[] args) {
		
		byte byteValue1 = 10;
		byte byteValue2 = 20;
		
		byte byteValue3 = (byte)(byteValue1 + byteValue2);
		System.out.println(byteValue3);
		int intValue1 = byteValue1 + byteValue2;
		System.out.println(intValue1);
		
		// 정수 연산의 기본 자료형은 int. casting을 해줘야 byte로 계산됨.
		// 피 연산자를 4byte 단위로 저장하기 때문.
		
		char charValue1 = 'A';
		char charValue2 = 1;
//		char charValue3 = charValue1 + charValue2;
		// 'A1'로 저장되지 않는다. char 끼리의 연산은 의미가 없음. 
		
		char charValue3 = (char)(charValue1+charValue2);
		System.out.println(charValue3);
		
		// 유니코드로 이용하고 싶은 것이 아니면 의미 없음.
		
		int intValue2 = charValue1 + charValue2;
		
		System.out.println("유니코드 : " + intValue2);
		System.out.println("출력문자 : " + (char)intValue2);
		
		// 위의 비교
		
		int intValue3 = 10;
		int intValue4 = intValue3/4;
		System.out.println(intValue4);
		
		//int는 정수 밖에 저장하지 않으므로 2.5가 아니라 2로 저장됨
		
		double doubleValue1 = intValue3/4;
		double doubleValue2 = intValue3/4.0;
		System.out.println(doubleValue1);
		System.out.println(doubleValue2);
		
		//정수끼리의 연산으로 나타내지 않고 작위적으로
        //double로 인식하게 만들어 주면 2.5가 된다
		
		int intValue5 = 10;
        //int intValue6 = intValue5 / 4.0;
		//실수끼리의 연산은 실수로 나오므로 int 안에 넣을 수 없다
		
		
		
		
	}
}
