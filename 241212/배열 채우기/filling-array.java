import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int[] arr = new int[10];

        for (int i=0; i<10; i++) {
            int number = sc.nextInt();
            if (number == 0) {
                break;
            } else {
                arr[i] = number;
            }
        }

        for (int i=9; i>=0; i--) {
            if (arr[i] != 0) 
                System.out.print(arr[i] + " ");
        }
    }
}