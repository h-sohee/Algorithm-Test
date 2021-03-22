package day2;

public class ex03_change {

	public static void main(String[] args) {
		int change = 1260;
		
		int coin500 = 0;
		int coin100 = 0;
		int coin50 = 0;
		int coin10 = 0;
		
		coin500 = change / 500;
		change %= 500;
		
		coin100 = change / 100;
		change %= 100;
		
		coin50 = change / 50;
		change %= 50;
		
		coin10 = change / 10;
		change %= 10;
		
		System.out.println("동전개수");
		System.out.println("500:" + coin500);
		System.out.println("100:" + coin100);
		System.out.println("50:" + coin50);
		System.out.println("10:" + coin10);
		
	}

}
