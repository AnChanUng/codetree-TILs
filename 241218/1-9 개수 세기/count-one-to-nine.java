import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] arr = new int[10];

        for (int i=0; i<n; i++) {
            int number = sc.nextInt();
            arr[number-1] += 1;
        }

        for (int i=0; i<9; i++) {
            System.out.println(arr[i]);
        }
    }
}