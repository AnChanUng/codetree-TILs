import java.util.*;

public class Main {
    static int[][] edges;
    static List<Node>[] graph;
    static int n;
    
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

        graph = new List[n+1];
        for(int i=1; i<=n; i++) {
            graph[i] = new ArrayList<>();
        }

        edges = new int[n - 1][3];
        for (int i = 0; i < n - 1; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();

            graph[edges[i][0]].add(new Node(edges[i][1], edges[i][2]));
            graph[edges[i][1]].add(new Node(edges[i][0], edges[i][2]));
        }

        Node a = bfs(1); // 아무정점에서 시작해서 가장 먼곳 찾기
        Node b = bfs(a.v); // 가장 먼곳과 가장 먼곳의 최단거리

        System.out.println(b.d);
    }

    private static Node bfs(int start) {
        boolean[] vis = new boolean[n+1];
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{start, 0});
        vis[start] = true;

        Node farthest = new Node(start, 0);

        while(!q.isEmpty()) {
            int[] cur = q.poll();
            int node = cur[0]; // 시작 노드
            int dist = cur[1]; // 누적 가중치

            if(dist > farthest.d) {
                farthest.v = node;
                farthest.d = dist;
            }

            for(Node next : graph[node]) {
                if(vis[next.v]) continue;

                q.offer(new int[]{next.v, dist + next.d});
                vis[next.v] = true;
            }
        }        
        
        return farthest;
    }
}