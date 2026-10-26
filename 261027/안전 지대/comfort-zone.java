import java.util.*;

/*
    k보다 작은 수들끼리 인접할 때, 영역의 수가 최대가 되는 k구하기

    알고리즘: bfs
*/

public class Main {
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    static int[][] grid;
    static boolean[][] vis;
    static int n, m;
    static int k, minCnt;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        grid = new int[n][m];
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
                grid[i][j] = sc.nextInt();
        // Please write your code here.
        
        int maxNum = 0;
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                maxNum = Math.max(grid[i][j], maxNum);
            }
        }
    
        k = 0;
        minCnt = 0;
        int maxK = 1;
        while(maxNum > k) {
            vis = new boolean[n][m];
            k++;
            int index = 0;
            for(int i=0; i<n; i++) {
                for(int j=0; j<m; j++) {
                    if(vis[i][j]) continue;
                    if(grid[i][j] <= k) continue;
                    bfs(i, j);
                    index++;
                }
            }

            // System.out.println("k: " + k + " index: " + index);
            // for(int i=0; i<n; i++) {
            //     for(int j=0; j<m; j++) {
            //         System.out.print(vis[i][j] + " ");
            //     }
            //     System.out.println();
            // }
            
            if(minCnt < index) {
                maxK = k;
                minCnt = index;
            }
        }   
        
        System.out.println(maxK + " " + minCnt);
    }

    private static void bfs(int x, int y) {
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{x, y});
        vis[x][y] = true;
        while(!q.isEmpty()) {
            int[] cur = q.poll();
            for(int dir=0; dir<4; dir++) {
                int nx = cur[0] + dx[dir];
                int ny = cur[1] + dy[dir];

                if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                if(vis[nx][ny]) continue;
                if(grid[nx][ny] <= k) continue;

                q.offer(new int[]{nx, ny});
                vis[nx][ny] = true;
            }
        }
    }
}