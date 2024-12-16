import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[1001];
        int cnt = 3;
        arr[0] = 1;
        arr[1] = n;
        for (int i=2; i<1001; i++) {
            arr[i] = arr[i-1] + arr[i-2];

            if (arr[i] > 100) {
                break;
            }
            cnt++;
        }
        
        for (int i=0; i<cnt; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}