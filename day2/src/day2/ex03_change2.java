package day2;

public class ex03_change2 {

	public static void main(String[] args) {
		int change = 1260;
		
		int [] coinValue = {500, 100, 50, 10};
		int [] coinCount = {0, 0, 0, 0};
		
		int c = 0;
		
		for(int i=0; i<4; i++) {
			coinCount[i] = change / coinValue[i];
			change %= coinValue[i];
			c += coinCount[i];
		}
		
		System.out.println("동전개수: " + c);
		System.out.println("500원: " + coinCount[0]);
		System.out.println("100원: " + coinCount[1]);
		System.out.println("50원: " + coinCount[2]);
		System.out.println("10원: " + coinCount[3]);
		
	}

}
