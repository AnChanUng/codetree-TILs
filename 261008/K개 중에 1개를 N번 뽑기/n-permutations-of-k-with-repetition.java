import java.util.*;
/*
    1~K의 수들을 N개 선택하기

    알고리즘: 순열 DFS 백트래킹

    - 1~k 배열 만들기
    - dfs(int depth)
     - n개 선택되면 return
*/
public class Main {
    static int[] arr;
    static int[] pick;  
    static int k, n;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        k = sc.nextInt();
        n = sc.nextInt();
        
        pick = new int[n];
        arr = new int[k];
        for(int i=1; i<=k; i++) {
            arr[i-1] = i;
        }

        dfs(0);
    }

    private static void dfs(int depth) {
        if(depth > n) return;
        if(depth == n) {
            for(int i=0; i<pick.length; i++) {
                System.out.print(pick[i] + " ");
            }
            System.out.println();
            return;
        }
        for(int i=0; i<k; i++) {
            pick[depth] = arr[i];
            dfs(depth+1);
        }
    }
}