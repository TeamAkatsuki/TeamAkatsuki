package chap05;

public class ArrayCopyExample {
	public static void main(String [] args) {
		String[] oldStrArray = {"java", "array", "copy"};
		String[] newStrArray = new String[5];
		
		System.arraycopy(oldStrArray, 0, newStrArray, 0, oldStrArray.length); 
//	    old의 0번째 인덱스부터 old.length까지 복사해서 new의 0번부터 채워넣는다
		
		for(int i = 0; i < newStrArray.length; i++) {
			System.out.print(newStrArray[i] + ",");
		}
	}

}
