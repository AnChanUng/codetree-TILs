import java.util.*;
public class Main {
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    static int[][] grid;
    static List<int[]> list;
    static int[][] startPoints;
    static int n, k, m;
    static int maxCnt;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        k = sc.nextInt();
        m = sc.nextInt();

        list = new ArrayList<>();
        grid = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = sc.nextInt();
                if(grid[i][j] == 1) {
                    list.add(new int[]{i, j});
                }
            }
        }
        startPoints = new int[k][2];
        for (int i = 0; i < k; i++) {
            startPoints[i][0] = sc.nextInt() - 1;
            startPoints[i][1] = sc.nextInt() - 1;
        }
        // Please write your code here.
        maxCnt = 0;
        dfs(0, 0);
        System.out.println(maxCnt);
    }

    private static void dfs(int start, int depth) {
        if(depth == m) {
            maxCnt = Math.max(maxCnt, bfs());
            return;
        }

        for(int i=start; i<list.size(); i++) {
            int[] cur = list.get(i);
            int x = cur[0];
            int y = cur[1];
            grid[x][y] = 0;
            dfs(i+1, depth+1);
            grid[x][y] = 1;
        }
    }

    private static int bfs() {
        int cnt = 0;
        boolean[][] vis = new boolean[n][n];
        Queue<int[]> q = new ArrayDeque<>();
        for(int i=0; i<k; i++) {
            int x = startPoints[i][0];
            int y = startPoints[i][1];
            q.offer(new int[]{x, y});
            vis[x][y] = true;
            cnt++;
        }

        while(!q.isEmpty()) {
            int[] cur = q.poll();
            for(int dir=0; dir<4; dir++) {
                int nx = cur[0] + dx[dir];
                int ny = cur[1] + dy[dir];
                if(nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                if(grid[nx][ny] == 1) continue;
                if(vis[nx][ny]) continue;
                vis[nx][ny] = true;
                q.offer(new int[]{nx, ny});
                cnt++;
            }
        }

        return cnt;
    }
}