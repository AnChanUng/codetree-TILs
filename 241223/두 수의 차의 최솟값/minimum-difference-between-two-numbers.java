import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int[] arr = new int[n];

        for (int i=0; i<n; i++) {
            arr[i] = sc.nextInt();
        }

        int result = Integer.MAX_VALUE;
        for (int i=1; i<n; i++) {
            for (int j=0; j<i; j++) {
                if (arr[i]-arr[j] < result) {
                    result = arr[i]-arr[j];
                }
            }
        }
        System.out.print(result);
    }
}