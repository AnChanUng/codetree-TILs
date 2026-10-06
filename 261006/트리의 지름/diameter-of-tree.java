import java.util.*;
public class Main {
    static List<Node>[] graph;                         
    static boolean[] vis;
    static int[] dist;                                 // dist[i] = 출발점에서 i까지 거리
    static int n;
    static class Node {
        int num, dist;                                 // num: 연결된 정점, dist: 간선 길이
        Node(int num, int dist) {
            this.num = num;
            this.dist = dist;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        vis = new boolean[n+1];
        dist = new int[n+1];
        graph = new List[n+1];
        for(int i=1; i<=n; i++) {
            graph[i] = new ArrayList<>();              // 만들어야 add 가능
        }

        for(int i=1; i<=n-1; i++) {                    // 트리는 간선 n-1개
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();

            graph[u].add(new Node(v, w));              // 방향 없으니 양방향
            graph[v].add(new Node(u, w));
        }

        dfs(1, 0);                                     // 1차: 아무 정점(1번)에서 출발
        int vertex = 1;
        for(int i=1; i<=n; i++) {
            if(dist[i] > dist[vertex]) vertex = i;     // 가장 먼 정점 = 지름의 한쪽 끝
        }

        vis = new boolean[n+1];                        // 2차 dfs 전에 새로 만들어 초기화 (안 하면 바로 끝남)
        dist = new int[n+1];
        dfs(vertex, 0);                                // 2차: 한쪽 끝에서 다시 출발

        int max = 0;
        for(int i=1; i<=n; i++) {
            max = Math.max(max, dist[i]);              // 반대쪽 끝까지 거리 = 지름
        }
        System.out.println(max);
    }

    private static void dfs(int node, int sum) {       // depth 넘기던 것처럼 누적 거리를 파라미터로 넘김
        vis[node] = true;
        dist[node] = sum;                              // 도착한 순간 거리 확정
        for(Node next : graph[node]) {
            if(!vis[next.num]) {
                dfs(next.num, sum + next.dist);        // 내려갈 때 간선 길이만큼 더해서 전달
            }
        }
    }
}