import java.util.*;
/*
    최장 증가 부분 수열

    알고리즘: DP

    dp[i] = i번째 원소로 끝나는 가장 긴 증가 부분 수열의 길이
*/
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();
        
        int answer = 0;

        int[] dp = new int[n];
        for(int i=0; i<n; i++) {
            dp[i] = 1;
            for(int j=0; j<i; j++) {
                if(arr[j] < arr[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }

            answer = Math.max(answer, dp[i]);
        }

        System.out.println(answer);
    }
}