import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[10];
        int count = 0;    
        for(int i=0; i<10; i++) {
            arr[i] = sc.nextInt();
        }
        double sum = 0;
        for(int i=0; i<10; i++) {
            if (arr[i] < 250) {
                sum += arr[i];
                count++;
            } else {
                break;
            }
        }

        double average = sum / count;
        System.out.print((int)sum + " ");
        System.out.print(sum/5);
    }
}