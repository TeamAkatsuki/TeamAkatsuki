package chap02;

public class CharExample {
	public static void main(String [] arg) {
		char c1 = 'A';
		char c2 = 65;
		
		// 65는 ASCII 코드의 65
		// 0~127까지 할당되어 있는 표준 코드
		// American Standard Code for Information Interchange
		// 미국 정보 교환 표준 부호
		
		// 유니코드 - 전세계 모든 언어 지원
		// 키보드에서 한글을 제외한 모든 것은 ASCII로 구성
		
		char c3 = '\u0041';
		char c4 = '가';
		char c5 = 44032;
		char c6 = '\uac00';
		
		int uniCode = c1; //유니코드 얻기
		
		//타입 자동변환
		
		System.out.println(c1);
		System.out.println(c2);
		System.out.println(c3);
		System.out.println(c4);
		System.out.println(c5);
		System.out.println(uniCode);
		
	}

}
