package day2;

public class ex03_until_one {
	public static void main(String[] args) {
		int n = 25;
		int k = 3;
		
		int count = 0;
		
		while(n != 1){
			if(n % k == 0) {
				n /= k;
				count += 1;
			}
			else {
				n -= 1;
			}

			System.out.println(n);	
		}
		
		System.out.println("count: " + count);	
		
	}
}
