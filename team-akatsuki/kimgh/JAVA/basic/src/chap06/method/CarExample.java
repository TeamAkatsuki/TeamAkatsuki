package chap06.method;

public class CarExample {
	public static void main(String [] args) {
		Car myCar = new Car();
		
		myCar.setGas(6); // Car ��ü�� setGas() ȣ��
		
		boolean gasState = myCar.isLeftGas();
		if(gasState) {
			System.out.println("����մϴ�.");
			myCar.run();
		}
		
		if(myCar.isLeftGas()) {
			System.out.println("�⸧ ����");
		}else {
			System.out.println("�⸧ �� ��������");
		}
	}

}
