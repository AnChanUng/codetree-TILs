import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int number = sc.nextInt();
        int arr[] = new int[100];
        int cnt = 0;
        for (int i=0; i<number; i++) {
            arr[i] = sc.nextInt();
        }

        int minVal = arr[0];
        for (int i=1; i<number; i++) {
            if (minVal > arr[i]) {
                minVal = arr[i];
            }
        }

        for (int i=0; i<number; i++) {
            if (arr[i] == minVal) {
                cnt++;
            }
        }

        System.out.print(minVal + " " + cnt);
    }
}