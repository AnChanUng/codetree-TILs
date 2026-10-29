import java.util.*;
/*
    정수 사각형 최장 증가 수열
    - 계속 증가하는 숫자로 이동해야함
    - 시작점은 상관없음

    알고리즘: 2차원 dp

    1. dp 배열 생성
    2. 모든 출발점에서 dfs 돌리기
    2.1 범위 범어나면 continue
    2.2 나보다 더 큰 곳으로 이동
    2.3 다음값 = dp에서 이전값과 지금 현재값중에 더 큰 값 갱신
    3. dp 배열에서 가장 큰 것 출력 (최장 증가 수열)
*/
public class Main {
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    static int[][] dp;
    static int[][] grid;
    static int n;
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        grid = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = sc.nextInt();
            }
        }
        
        dp = new int[n][n];
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                dfs(i, j);
            }
        }

        //System.out.println(Arrays.deepToString(dp));
        int maxCnt = 0;
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                maxCnt = Math.max(maxCnt, dp[i][j]);
            }
        }
        
        System.out.println(maxCnt);
    }

    private static void dfs(int x, int y) {
        if(dp[x][y] != 0) return;
        dp[x][y] = 1;

        for(int dir=0; dir<4; dir++) {
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            if(nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
            if(grid[nx][ny] <= grid[x][y]) continue; // 다음<=현재 크기면 continue

            dfs(nx, ny);
            dp[x][y] = Math.max(dp[x][y], dp[nx][ny] + 1);
        }
    }
}