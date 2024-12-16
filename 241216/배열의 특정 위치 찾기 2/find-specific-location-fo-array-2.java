import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[10];
        // 10개의 정수 입력받아 홀수 번째 입력받은 정수의 합과 짝수 번째 입력받은 정수의 합 
        // 큰 수에서 작은 수 빼기
        int odd = 0;
        int even = 0;
        for (int i=0; i<10; i++) {
            arr[i] = sc.nextInt();
        }

        for (int i=0; i<10; i++) {
            if ((i+1) % 2 == 1) {
                odd += arr[i];
            } else {
                even += arr[i];
            }
        }
        
        if (odd > even) {
            System.out.print(odd - even);
        } else if (odd < even) {
            System.out.print(even - odd);
        } else {
            System.out.print(0);
        }
    }
}