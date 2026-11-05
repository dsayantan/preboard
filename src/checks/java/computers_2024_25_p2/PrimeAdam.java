// BEGIN ANSWER
import java.util.Scanner;

public class PrimeAdam
{
    // true if n has exactly two factors, 1 and n
    static boolean isPrime(int n)
    {
        if (n < 2)
            return false;
        for (int i = 2; i * i <= n; i++)
            if (n % i == 0)
                return false;
        return true;
    }

    // the digits of n in reverse order
    static long reverse(long n)
    {
        long r = 0;
        while (n > 0)
        {
            r = r * 10 + n % 10;
            n = n / 10;
        }
        return r;
    }

    // Adam: square of the reverse of n = reverse of the square of n
    static boolean isAdam(int n)
    {
        long sq = (long) n * n;
        long rn = reverse(n);
        long sqr = rn * rn;
        return sqr == reverse(sq);
    }

    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();                        // lower limit
        int n = sc.nextInt();                        // upper limit
        // m must be less than n
        if (m <= 0 || n <= 0 || m >= n)
        {
            System.out.println("INVALID INPUT");
            return;
        }
        // number of Prime-Adam integers found
        int freq = 0;
        // the integers found, space separated
        String list = "";
        for (int i = m; i <= n; i++)
        {
            if (isPrime(i) && isAdam(i))
            {
                list = list + i + " ";
                freq++;
            }
        }
        System.out.println("THE PRIME-ADAM INTEGERS ARE:");
        if (freq == 0)
            System.out.println("NIL");
        else
            System.out.println(list.trim());
        System.out.println("FREQUENCY OF PRIME-ADAM INTEGERS IS: "
                           + freq);
    }
}
// END ANSWER
