package chap06.method;

public class CarExample {
	public static void main(String [] args) {
		Car myCar = new Car();
		
		myCar.setGas(6); // Car 객체의 setGas() 호출
		
		boolean gasState = myCar.isLeftGas();
		if(gasState) {
			System.out.println("출발합니다.");
			myCar.run();
		}
		
		if(myCar.isLeftGas()) {
			System.out.println("기름 남음");
		}else {
			System.out.println("기름 다 떨어졌당");
		}
	}

}
