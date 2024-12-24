import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[][] arr = new String[5][3];

        for (int i=0; i<5; i++) {
            for (int j=0; j<3; j++) {
                String chr = sc.next();
                arr[i][j] = chr.toUpperCase();
            }
        }
         
        for (int i=0; i<5; i++) {
            for (int j=0; j<3; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}