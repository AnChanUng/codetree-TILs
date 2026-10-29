import java.util.*;
/*
    최대 감소 수열 찾기

    알고리즘: dp
*/
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
    
        int answer = 0;

        int[] dp = new int[n];
        for(int i=0; i<n; i++) {
            dp[i] = 1;
            //System.out.println(Arrays.toString(dp));
            for(int j=0; j<i; j++) {
                if(arr[j] > arr[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }    
            answer = Math.max(dp[i], answer);
        }
        //System.out.println(Arrays.toString(dp));
        System.out.println(answer);
    }
}