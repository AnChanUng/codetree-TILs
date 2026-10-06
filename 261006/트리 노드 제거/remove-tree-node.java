import java.util.*;
/*
    노드 1개 삭제했을 때, 리프노드의 개수 구하기

    알고리즘: 그래프 dfs 인접리스트

    int[] parent
    값이 -1 일때, 루트노드
    각 부모노드의 번호가 주어짐
*/
public class Main {
    static List<Integer>[] graph;
    static int[] parent;
    static int cnt;
    static int deleteNode;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        graph = new List[n];
        for(int i=0; i<n; i++) {
            graph[i] = new ArrayList<>();
        }
        
        parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = sc.nextInt();
            if(parent[i] != -1) { 
                graph[parent[i]].add(i);
            }
        }
        deleteNode = sc.nextInt();

        for(int i=0; i<n; i++) {
            if(parent[deleteNode] == -1) break;
            if(parent[i] == -1) {
                dfs(i);
                break;
            }
        }

        System.out.println(cnt);
    }

    private static void dfs(int node) {
        int child = 0;
        for(int next : graph[node]) {
            if(next == deleteNode) continue;
            child++;
            dfs(next);
        }
        if(child == 0) {
            cnt++;
        }
    }
}