package chap06.constructor;

public class Car3 {
	String company = "����";
	String model;
	String color;
	int maxSpeed;
	
	Car3(String model){
//		this.model = model;
//		this.color = "����";
//		this.maxSpeed = 250;
		
		this(model, "����", 250);
		
	}
	
	Car3(String model, String color){
//		this.model = model;
//		this.color = color;
//		this.maxSpeed = 250;
		
		this(model, color, 250);
	}
	
	Car3(String model, String color, int maxSpeed){
//		this.model = model;
//		this.color = color;
//		this.maxSpeed = maxSpeed;
		
		this(model, color, maxSpeed);
		
	}
}
