// BEGIN ANSWER
import java.util.Scanner;

/* Increasing: no digit is smaller than the digit on its left  (556778)
 * Decreasing: no digit is smaller than the digit on its right (663320)
 * Bouncy    : a positive integer that is neither                (29748)  */
class Bouncy {
    long num;       // the number to test

    Bouncy(long n) {
        num = n;
    }

    boolean isIncreasing() {
        String s = Long.toString(num);
        for (int i = 1; i < s.length(); i++)
            if (s.charAt(i) < s.charAt(i - 1))    // a digit exceeded by the one on its left
                return false;
        return true;
    }

    boolean isDecreasing() {
        String s = Long.toString(num);
        for (int i = 0; i < s.length() - 1; i++)
            if (s.charAt(i) < s.charAt(i + 1))    // a digit exceeded by the one on its right
                return false;
        return true;
    }

    boolean isBouncy() {
        return !isIncreasing() && !isDecreasing();
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a positive integer:");
        long n = sc.nextLong();
        if (n <= 0) {
            System.out.println("INVALID INPUT: enter a positive integer");
            return;
        }
        Bouncy ob = new Bouncy(n);
        if (ob.isBouncy())
            System.out.println(n + " is a Bouncy Number");
        else if (ob.isIncreasing() && ob.isDecreasing())
            System.out.println(n + " is NOT a Bouncy Number (all its digits are equal)");
        else if (ob.isIncreasing())
            System.out.println(n + " is NOT a Bouncy Number (it is an increasing number)");
        else
            System.out.println(n + " is NOT a Bouncy Number (it is a decreasing number)");
    }
}
// END ANSWER
