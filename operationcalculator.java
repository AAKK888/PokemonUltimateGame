import java.util.Scanner;
public class operationcalculator {
    public static void main(String[] args) {
        Scanner calculator = new Scanner(System.in);
        String Hello = "Hello. Welcome to calculator.Please type 1 for addition, 2 for subtract, 3 for divide, or 4 for multiply in the line below.";
        System.out.println(Hello);
        int num1 = calculator.nextInt();
        if (num1 == 1) {
            System.out.println("What are your numbers?");
            double add1 = calculator.nextDouble();
            double add2 = calculator.nextDouble();
            System.out.println("Here is your answer!");
            System.out.println(add1+add2);
        }
        if (num1 == 2) {
            System.out.println("What are your numbers?");
            double subtract1 = calculator.nextDouble();
            double subtract2 = calculator.nextDouble();
            System.out.println("Here is your answer!");
            System.out.println(subtract1 - subtract2);
        }
        if (num1 == 3) {
            System.out.println("What are your numbers?");
            double divide1 = calculator.nextInt();
            double divide2 = calculator.nextInt();
            System.out.println("Here is your answer!");
            System.out.print(divide1 / divide2);
        }
        if (num1 == 4) {
            System.out.println("What are your numbers?");
            double mul1 = calculator.nextDouble();
            double mul2 = calculator.nextDouble();
            System.out.println("Here is your answer!");
            System.out.println(mul1*mul2);
        }
    }
}

