import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int[] arr = new int[10];

        for (int i=0; i<10; i++) {
            arr[i] = sc.nextInt();
        }

        int sum = 0;
        double average = 0;
        int cnt = 0;
        for (int i = 0; i < 10; i++) {
            if ((i+1) % 2 == 0) {
                sum += arr[i];
            }

            if ((i+1) % 3 == 0) {
                average += arr[i];
                cnt++;
            }
        }
        System.out.printf("%d %.1f", sum, average/cnt);
    }
}