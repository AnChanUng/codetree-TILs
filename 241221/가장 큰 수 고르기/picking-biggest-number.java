import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int maxVal = 0;
        for (int i=0; i<10; i++) {
            int number = sc.nextInt();

            if (maxVal < number) {
                maxVal = number;
            }
        }
        System.out.print(maxVal);
    }
}