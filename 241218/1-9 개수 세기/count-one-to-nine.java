import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] countArr = new int[10];
        int[] arr = new int[100];

        for (int i=0; i<n; i++) {
            arr[i] = sc.nextInt();
            countArr[arr[i]]++;
        }

        for (int i=1; i<=9; i++) {
            System.out.println(countArr[i]);
        }
    }
}