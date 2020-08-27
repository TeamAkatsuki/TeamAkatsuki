package chap06.method;

public class Car {

	//필드
	
	int gas = 15;
	
	//생성자
	
	
	
	//메소드
	
	void setGas(int gas) {
		this.gas = gas;
	}
	
	boolean isLeftGas() {
		if(gas == 0) {
			System.out.println("기름 없다");
			return false;
		}
		
		System.out.println("기름 있다");
		return true;
	}
	
	void run() {
		while(true) {
			if(gas > 0) {
				System.out.println("달려엇~~~~~~~~~~~~(기름 :" + gas + ")");
				gas -= 1;
			}else {
				System.out.println("멈춰~~~~~~!(기름 : " + gas + ")");
				return;
			}
		}
	}
}
