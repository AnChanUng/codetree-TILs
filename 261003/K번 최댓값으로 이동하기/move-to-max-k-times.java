import java.util.*;
/*
    시작점에서 출발해서 k번 이동해서 현재 위치 구하기

    알고리즘: bfs

    1. bfs(r, c)에서 출발
    2. bfs(int x, int y)
    2.1 나보다 작은것중에 가장 큰 곳으로 이동
        같은 곳이 있으면 열이 더 작은 곳으로 이동   
    3. 현재 위치 출력
*/
public class Main {
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    static int[][] grid;
    static boolean[][] vis;
    static int n, k, r, c;
    static int startVal;
    static int bestX, bestY;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        k = sc.nextInt();

        grid = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                grid[i][j] = sc.nextInt();
        r = sc.nextInt() - 1;
        c = sc.nextInt() - 1;

        for(int t=0; t<k; t++) {       
            bfs(r, c);
            if(bestX == -1) break;     
            r = bestX;                 
            c = bestY;
        }

        System.out.println((r+1) + " " + (c+1));
    }
    
    private static void bfs(int x, int y) {
        vis = new boolean[n][n];
        startVal = grid[x][y];
        bestX = -1;
        bestY = -1;

        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{x, y});
        vis[x][y] = true;
        while(!q.isEmpty()) {
            int[] cur = q.poll();
            for(int dir=0; dir<4; dir++) {
                int nx = cur[0] + dx[dir];
                int ny = cur[1] + dy[dir];

                if(nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                if(vis[nx][ny]) continue;
                if(grid[nx][ny] >= startVal) continue;
                
                q.offer(new int[]{nx, ny});
                vis[nx][ny] = true;
                if(isBetter(nx, ny)) {
                    bestX = nx;
                    bestY = ny;
                }
            }    
        }
    }

    private static boolean isBetter(int x, int y) {
        if(bestX == -1) return true;                          // 후보가 없으면 무조건 1등
        if(grid[x][y] != grid[bestX][bestY])
            return grid[x][y] > grid[bestX][bestY];           // 1순위: 값이 큰 쪽
        if(x != bestX) return x < bestX;                      // 2순위: 행이 작은 쪽
        return y < bestY;                                     // 3순위: 열이 작은 쪽
    }
}