import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[10];
        int cnt = 0;
        int sum = 0;
        for (int i=0; i<10; i++) {
            int number = sc.nextInt();

            if (number % 2 == 0 && number != 0) {
                sum += number;
                cnt++;
            } 

            if (number == 0) {
                break;
            }

            System.out.print(sum + " " + cnt);
        }
    }
}