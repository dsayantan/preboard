// BEGIN ANSWER
import java.util.Scanner;
class SeriesSum {
    int n;          // number of terms after the leading 1
    int x;          // value of x
    double sum;     // sum of the series

    SeriesSum(int nn, int xx) {
        n = nn;
        x = xx;
        sum = 0.0;
    }

    // x raised to p, recursively: x^p = x * x^(p-1), x^0 = 1
    int power(int b, int p) {
        if (p == 0)
            return 1;
        return b * power(b, p - 1);
    }

    // m! recursively: m! = m * (m-1)!, 0! = 1! = 1
    int factorial(int m) {
        if (m <= 1)
            return 1;
        return m * factorial(m - 1);
    }

    // Sum = 1 + x/1! + x^3/2! + x^5/3! + ... + x^(2n-1)/n!
    void calcSeries() {
        sum = 1.0;
        for (int i = 1; i <= n; i++)
            sum += (double) power(x, 2 * i - 1) / factorial(i);   // i-th term
    }

    void display() {
        System.out.println("Sum of the series = " + sum);
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter n: ");
        int nn = sc.nextInt();
        System.out.println("Enter x: ");
        int xx = sc.nextInt();
        SeriesSum ob = new SeriesSum(nn, xx);
        ob.calcSeries();
        ob.display();
    }
}
// END ANSWER
