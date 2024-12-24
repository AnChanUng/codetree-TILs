import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[][] arr = new int[2][4];
        double total = 0;
        for (int i=0; i<2; i++) {
            for (int j=0; j<4; j++) {
                arr[i][j] = sc.nextInt(); 
            }
        }

        for (int i=0; i<2; i++) {
            double garo = 0;
            for (int j=0; j<4; j++) {
                garo += arr[i][j];
            }
            System.out.printf("%.1f ", garo / 4);
        }
        System.out.println();

        for (int i=0; i<4; i++) {
            double sero = 0;
            for (int j=0; j<2; j++) {
                sero += arr[j][i];
            }
            System.out.printf("%.1f ", sero / 2);
        }
        System.out.println();
        
        for (int i=0; i<2; i++) {
            for (int j=0; j<4; j++) {
                total += arr[i][j];
            }
        }
        System.out.printf("%.1f", total/8);
    }
}