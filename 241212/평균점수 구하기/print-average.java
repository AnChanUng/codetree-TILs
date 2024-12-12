import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        double sum = 0;
        for (int i = 0; i < 8; i++) {
            double score = sc.nextDouble();
            sum += score;
        }

        double average = sum / 8;

        System.out.printf("%.1f", average);
    }
}