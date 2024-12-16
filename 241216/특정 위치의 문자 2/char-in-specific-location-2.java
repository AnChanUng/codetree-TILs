import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for (int i=0; i<10; i++) {
            String word = sc.next();

            if ((i+1) == 2) {System.out.print(word + " ");}
            if ((i+1) == 5) {System.out.print(word + " ");}
            if ((i+1) == 8) {System.out.print(word + " ");}
        }
    }
}