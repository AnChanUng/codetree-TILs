import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int first = sc.nextInt();
        int second = sc.nextInt();

        int[] arr = new int[10];
        arr[0] = first;
        arr[1] = second;

        for (int i=2; i<10; i++) {
            arr[i] = arr[i-1] + 2 * arr[i-2];
        }

        for (int i=0; i<10; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}