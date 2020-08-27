package chap03;

public class BitShiftExample {
	public static void main(String[] args) {
		System.out.println("1 << 3 = " + (1 << 3));
		System.out.println("-8 >> 3 = " + (-8 >> 3));
		System.out.println("-8 >>> 3 = " + (-8 >>> 3));
		// 좌측 이동, 우측 이동은 작용이 다르다.
	} 

}
