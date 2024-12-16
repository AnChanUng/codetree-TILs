import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int first = sc.nextInt();
        int second = sc.nextInt();
        int[] arr = new int[10];

        for (int i=0; i<10; i++) {
            if (i == 0) {
                arr[i] = first;
            } else if (i == 1) {
                arr[i] = second;
            } else {
                arr[i] = (arr[i-1] + arr[i-2]) % 10;
            }
        }
        
        for (int i=0; i<10; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}