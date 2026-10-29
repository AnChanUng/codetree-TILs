import java.util.*;
/*
    4가지 연산을 적절히 사용하여 연산의 횟수를 최소화

    현재 수에서 1을 뺍니다.
    현재 수에 1을 더합니다.
    현재 수가 2로 나누어 떨어질 경우, 현재 수를 2로 나눕니다.
    현재 수가 3으로 나누어 떨어질 경우, 현재 수를 3으로 나눕니다.
*/
public class Main {
    static int[] dist;
    static int minDepth;
    static int n;
    static int limit;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        
        minDepth = Integer.MAX_VALUE;
        
        limit = n + 1;
        
        dist = new int[limit + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        
        dfs(n, 0);

        System.out.println(minDepth);
    }

    private static void dfs(int n, int depth) {
        // 범위 검사
        if(n < 1 || n > limit) return;

        // 이미 구한 정답보다 연산 횟수가 많거나 같으면 종료
        if(depth >= minDepth) return;

        // 더 적은 횟수로 방문한 적이 있으면 종료
        if(dist[n] <= depth) return;

        // 현재 숫자까지의 최소 연산 횟수 저장
        dist[n] = depth;

        if(n == 1) {
            minDepth = Math.min(depth, minDepth);
            return;
        }
        if(n % 3 == 0) {
            dfs(n/3, depth+1);
        }
        if(n % 2 == 0) {
            dfs(n/2, depth+1);
        }
        dfs(n+1, depth+1);
        dfs(n-1, depth+1);
    }
}