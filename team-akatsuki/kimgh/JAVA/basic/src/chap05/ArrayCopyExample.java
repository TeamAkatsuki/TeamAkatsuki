package chap05;

public class ArrayCopyExample {
	public static void main(String [] args) {
		String[] oldStrArray = {"java", "array", "copy"};
		String[] newStrArray = new String[5];
		
		System.arraycopy(oldStrArray, 0, newStrArray, 0, oldStrArray.length); 
//	    old�� 0��° �ε������� old.length���� �����ؼ� new�� 0������ ä���ִ´�
		
		for(int i = 0; i < newStrArray.length; i++) {
			System.out.print(newStrArray[i] + ",");
		}
	}

}
