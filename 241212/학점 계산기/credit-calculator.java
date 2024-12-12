import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int subject = sc.nextInt();
        double sum = 0;
        for (int i = 0; i < subject; i++) {
            double score = sc.nextDouble();
            sum += score;
        }

        double averageScore = sum / subject;
        System.out.printf("%.1f", averageScore);
        System.out.println();
        
        if (averageScore >= 4) {
            System.out.print("Perfect");
        } else if (averageScore >= 3) {
            System.out.print("Good");
        } else {
            System.out.print("Poor");
        }
    }
}