import java.util.*;
public class Main {
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    static int[][] grid;
    static int minX, minY;
    static int n, k, r, c;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        k = sc.nextInt();
        grid = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                grid[i][j] = sc.nextInt();
        r = sc.nextInt();
        c = sc.nextInt();

        minX = r - 1;
        minY = c - 1;

        // K번 이동
        for(int i=0; i<k; i++) {
            int x = minX;
            int y = minY;

            bfs(x, y);

            if(x == minX && y == minY) break;
        }

        System.out.println((minX + 1) + " " + (minY + 1));
    }

    private static void bfs(int x, int y) {
        boolean[][] vis = new boolean[n][n];
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{x, y});
        vis[x][y] = true;

        int maxValue = -1;
        while(!q.isEmpty()) {
            int[] cur = q.poll();
            for(int dir=0; dir<4; dir++) {
                int nx = cur[0] + dx[dir];
                int ny = cur[1] + dy[dir];

                if(nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                if(vis[nx][ny]) continue;
                if(grid[nx][ny] >= grid[x][y]) continue;

                if(grid[nx][ny] < grid[x][y]) {
                    vis[nx][ny] = true;
                    q.offer(new int[]{nx, ny});
                
                    // 더 큰 값을 발견했다면 갱신
                    if(grid[nx][ny] > maxValue) {
                        maxValue = grid[nx][ny];
                        minX = nx;
                        minY = ny;
                    }

                    // 값이 같으면 행이 작은 위치 선택
                    else if(grid[nx][ny] == maxValue) {
                        if(nx < minX || (nx == minX && ny < minY)) {
                            minX = nx;
                            minY = ny;
                        }
                    }
                }
            }
        }
    }
}