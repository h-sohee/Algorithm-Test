package day2;

import java.util.*;

public class ex11_multi_or_add {

	public static void main(String[] args) {
//		Scanner sc = new Scanner(System.in);
//		String S = sc.next();
		
//		String str = "02984";
		String str = "567";
		
		int [] num = new int [str.length()];

		
		for(int i=0;i<str.length();i++) {
			num[i] = (int)str.charAt(i) - 48;
			System.out.println("num: " + num[i]);
		}
		
		int result = num[0];
		
		for(int i=1;i<str.length();i++) {
			if(num[i-1] + num[i] >= num[i-1] * num[i]) {
				System.out.println(num[i-1] + num[i]);
				result += num[i];
			}
			else{
				System.out.println(num[i-1] * num[i]);
				result *= num[i];
			}
			System.out.println("result: " + result);
		}
		
		
//		String s="0567";
//		int sum=0;
//		
//		
//		for(int i=0;i<s.length();i++) {	
//			if(sum==0||s.charAt(i)=='0'||s.charAt(i)=='1') {
//				System.out.println("+");
//				sum=sum+(s.charAt(i)-'0');
//			}else {
//				System.out.println("*");
//				sum=sum*(s.charAt(i)-'0');
//			}
//			
//		}

	}

}
