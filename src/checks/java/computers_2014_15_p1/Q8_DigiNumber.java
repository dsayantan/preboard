// ANSWER-START
import java.util.Scanner;

class DigiNumber {
    long num;                               // the number

    DigiNumber() {                          // default constructor
        num = 0;
    }

    // parameterised constructor
    DigiNumber(long n) {
        num = n;
    }

    // frequency of each digit present in num
    void digitfrequency() {
        int freq[] = new int[10];
        long t = Math.abs(num);
        if (t == 0)
            freq[0] = 1;
        while (t > 0) {
            freq[(int) (t % 10)]++;
            t /= 10;
        }
        System.out.println("Digit\tFrequency");
        for (int d = 0; d <= 9; d++)
            if (freq[d] > 0)
                System.out.println(d + "\t" + freq[d]);
    }

    // recursive sum of digits
    long sumDigits(long N) {
        if (N == 0)                         // base case
            return 0;
        return N % 10 + sumDigits(N / 10);
    }

    void printsum() {
        System.out.println("Sum of digits of " + num + " = "
                           + sumDigits(Math.abs(num)));
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        DigiNumber ob = new DigiNumber(sc.nextLong());
        ob.digitfrequency();
        ob.printsum();
    }
}
// ANSWER-END
