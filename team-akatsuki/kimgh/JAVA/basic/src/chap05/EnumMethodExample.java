package chap05;

public class EnumMethodExample {
	public static void main(String [] args) {
		//name() �޽��
		//���� ��ü�� ������ �ִ� ���ڿ��� �����Ѵ�
		Week today = Week.SUNDAY;
		System.out.println("name() ���");
		String name = today.name();
		
		
		System.out.println(name);
		
		//ordinal() �����
		//��ü ���� ��ü �߿� �� ��° ���� ��ü���� �����Ѵ�
		int ordinal = today.ordinal();
		
		System.out.println("ordinal() ���");
		System.out.println(ordinal);
		
		//compareTo() �޽��������
		//�Ű������� �־��� ���� ��ü�� �������� ���� ��ġ�� ���ڷ� �����Ѵ�
		Week day1 = Week.MONDAY;
		Week day2 = Week.TUESDAY;
		int result1 = day1.compareTo(day2);
		int result2 = day2.compareTo(day1);
		
		System.out.println("compareTo() ���");
		System.out.println(result1);
		System.out.println(result2);
		
		//valueOf() ��th�ǵ�
		//�Ű������� �־��� ���ڿ��� ������ ���ڿ��� ������ ���� ��ü ����
		if(args.length ==1) {
			String strDay = args[0];
			Week weekDay = Week.valueOf(strDay);
			System.out.println("valueOf() ���");
			if(weekDay == Week.SATURDAY || weekDay == Week.SUNDAY) {
				System.out.println("�ָ��̱���!");
			}else {
				System.out.println("�����̳׿�...");
			}
		}
		
		//values() ��sword
		//����Ÿ���� ��� ���� ��ü���� �迭�� ����
		
		System.out.println("values() ���");
		Week[] days = Week.values();
		for(Week day : days) {
			System.out.println(day);
		}
		
	}

}
