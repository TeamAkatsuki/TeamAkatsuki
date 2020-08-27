package chap06;

public class Studentexample {
	public static void main(String[] args) {
		Student s1 = new Student();
		System.out.println("s1 변수가 Student 객체를 참조");
		
		Student s2 = new Student();
		System.out.println("s2 변수가 다른 Student 객체를 참조");
	}
}
