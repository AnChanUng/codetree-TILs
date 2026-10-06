import java.util.*;
public class Main {
    static List<Integer>[] graph;
    static boolean[] vis;
    static int[] parent;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        parent = new int[n+1];
        vis = new boolean[n+1];
        graph = new List[n+1];
        for(int i=1; i<=n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 1; i <= n - 1; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            graph[x].add(y);
            graph[y].add(x);
        }
        
        dfs(1);
 
        for(int i=2; i<=n; i++) {
            System.out.println(parent[i]);
        }
    }
   
    private static void dfs(int node) {
        vis[node] = true;
        for(int next : graph[node]) {
            if(!vis[next]) {
                parent[next] = node;
                dfs(next);
            }
        }
    }
}