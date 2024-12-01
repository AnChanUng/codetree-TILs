import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        // sum
        int res1 = a + b + c;
        int res2 = (a+b+c) / 3;
        int res3 = res1 - res2;

        System.out.println(res1);
        System.out.println(res2);
        System.out.println(res3);
    }
}