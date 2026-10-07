import java.util.*;
public class Main {
    static List<Node>[] graph;
    static int n, m;
    static class Node {
        int v, d;

        Node(int v, int d) {
            this.v = v;
            this.d = d;
        }
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        
        graph = new List[n+1];
        for(int i=1; i<=n; i++) {
            graph[i] = new ArrayList<>();
        }
        
        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int d = sc.nextInt();

            graph[u].add(new Node(v, d));
            graph[v].add(new Node(u, d));
        }
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();

            int answer = bfs(u, v);
            System.out.println(answer);
        }
    }
    
    private static int bfs(int x, int y) {
        boolean[] vis = new boolean[n+1];
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{x, 0});
        vis[x] = true;

        while(!q.isEmpty()) {
            int[] cur = q.poll();
            int node = cur[0]; // 현재 정점
            int dist = cur[1]; // 지금까지의 거리

            if(node == y) return dist;

            for(Node next : graph[node]) {
                if(vis[next.v]) continue;
                q.offer(new int[]{next.v, dist + next.d});
                vis[next.v] = true;          
            }
        }

        return -1;
    }
}