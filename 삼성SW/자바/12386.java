import java.util.Scanner;

public class Solution {	
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		
		int T=sc.nextInt();
		int a,b;
		
		for(int i=1;i<T+1;i++) {
			a=sc.nextInt();
			b=sc.nextInt();
			
			System.out.println("#"+i+" "+Cal(a,b));
		}
	}
	
	public static int Cal(int x,int y) {
		int res=x+y;
		
		if(res>=24)res-=24;
		return res;
	}
}