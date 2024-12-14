import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int[] arr = new int[10];
        for (int i=0; i<=9; i++) {
            arr[i] = sc.nextInt();
            // 3, 5, 10번째 정수의 합을 출력하는 프로그램
        }
        int sum = arr[2] + arr[4] + arr[9];
        System.out.print(sum);
    }
}