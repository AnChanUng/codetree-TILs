import java.util.*;
/*
    m개의 돌을 치웠을 때 방문 가능한 서로 다른 칸 수의 최대값

    알고리즘: bfs

    1 이동x
    0 이동o

    1. 격자에서 돌들이 들어 올때 리스트에 인덱스 저장 
    2. 리스트 전체의 개수 C m개를 0으로 변경하는 모든 경우의 수 구하기
    3. dfs(int start, int depth)
    4. 모든 경우의 수를 bfs 돌려서 1의 개수가 더 최대값이면 갱신
    5. 최대값 출력
*/
public class Main {
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    static int[][] grid;
    static int[][] startPoints;
    static List<int[]> list;
    static int n, k, m;
    static int maxCnt;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt(); // 격자의 크기
        k = sc.nextInt(); // 시작점의 수
        m = sc.nextInt(); // 돌의 개수
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
        
        dfs(0, 0);
        System.out.println(maxCnt);
    }
    
    private static int bfs() {
        boolean[][] vis = new boolean[n][n];
        Queue<int[]> q = new ArrayDeque<>();
        
        int cnt = 0;
        for(int i=0; i<startPoints.length; i++) {
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
                if(vis[nx][ny]) continue;
                if(grid[nx][ny] == 1) continue;
                q.offer(new int[]{nx, ny});
                vis[nx][ny] = true;
                cnt++;
            }
        }
        
        return cnt;
    }

    private static void dfs(int start, int depth) {
        if(depth == m) {
            maxCnt = Math.max(maxCnt, bfs());
            return;
        }    

        for(int i=start; i<list.size(); i++) {
            int[] cur = list.get(i);
            int x = cur[0], y = cur[1];
            grid[x][y] = 0;
            dfs(i+1, depth+1);
            grid[x][y] = 1;
        }
    }
}