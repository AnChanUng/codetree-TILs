import java.util.*;
/*
    두 도시간의 높이 차가 U이상 D이하 인것중에 최대 개수

    알고리즘: bfs

    1. 전체 n*n 중에 k개 선택해서 출발지점 구하기
    2. bfs()
    2.1 U이상 D이하만 이동
    2.2 이동할때마다 카운트
    3. 카운트가 최대면 갱신
*/
public class Main {
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    static int[][] grid;
    static boolean[][] vis;
    static List<int[]> pick;
    static List<int[]> list;
    static int n, k, u, d;
    static int cnt, maxCnt;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        k = sc.nextInt();
        u = sc.nextInt();
        d = sc.nextInt();

        list = new ArrayList<>();
        pick = new ArrayList<>();
        grid = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                grid[i][j] = sc.nextInt();
                list.add(new int[]{i, j});
            }
        }

        maxCnt = 0;
        dfs(0, 0);
        System.out.print(maxCnt);
    }

    private static void dfs(int start, int depth) {
        if(depth == k) {
            cnt = 0;
            vis = new boolean[n][n];
            for(int i=0; i<pick.size(); i++) {
                int[] c = pick.get(i);
                bfs(c[0], c[1]);
            }
            maxCnt = Math.max(maxCnt, cnt);
            return;
        }
        
        for(int i=start; i<list.size(); i++) {
            int[] cur = list.get(i);
            pick.add(cur);
            dfs(i+1, depth+1);
            pick.remove(pick.size()-1);
        }   
    }
    
    private static int bfs(int x, int y) {
        if(vis[x][y]) return cnt;
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{x, y});
        vis[x][y] = true;
        cnt += 1;
        while(!q.isEmpty()) {
            int[] cur = q.poll();
            for(int dir=0; dir<4; dir++) {
                int nx = cur[0] + dx[dir];
                int ny = cur[1] + dy[dir];
                if(nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                if(vis[nx][ny]) continue;
                
                // U이상 D이하만 이동
                int diff = Math.abs(grid[cur[0]][cur[1]] - grid[nx][ny]);

                if(u <= diff && diff <= d) {
                    q.offer(new int[]{nx, ny});
                    vis[nx][ny] = true;
                    cnt++;
                }
            }
        }
        return cnt;
    }
}