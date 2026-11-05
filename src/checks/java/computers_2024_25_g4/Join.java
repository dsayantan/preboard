// BEGIN ANSWER
import java.util.Scanner;

public class Join
{
    int num;                     // the number
    // one Scanner shared by all objects
    static Scanner sc = new Scanner(System.in);

    // constructor: legal initial value
    Join()
    {
        num = 0;
    }

    // accepts the number
    void readNumber()
    {
        System.out.println("Enter a number :");
        num = sc.nextInt();
    }

    /* Joins X.num and Y.num numerically: X.num is shifted left by
       as many decimal places as Y.num has digits, then Y.num is added.
       e.g. 65 and 723 : 65 * 1000 + 723 = 65723 */
    Join JoinNum(Join X, Join Y)
    {
        // 10 ^ (number of digits of Y.num)
        int p = 1;
        int t = Y.num;
        do
        {
            p = p * 10;
            t = t / 10;
        // do-while: 0 still counts as one digit
        } while (t > 0);
        Join R = new Join();
        R.num = X.num * p + Y.num;
        return R;
    }

    // shows the merged number and its odd-positioned digits (from left)
    void show()
    {
        System.out.println("Merged number : " + num);
        int d = 0, t = num;
        do                               // count the digits
        {
            d++;
            t = t / 10;
        } while (t > 0);
        // odd-positioned digits, kept in order
        int odd = 0, p = 1;
        t = num;
        // rightmost digit is position d
        for (int pos = d; pos >= 1; pos--)
        {
            int dig = t % 10;
            t = t / 10;
            if (pos % 2 == 1)
            {
                odd = odd + dig * p;
                p = p * 10;
            }
        }
        System.out.println("Odd positioned digits : " + odd);
    }

    public static void main(String args[])
    {
        Join a = new Join();
        Join b = new Join();
        a.readNumber();
        b.readNumber();
        Join c = new Join();
        c = c.JoinNum(a, b);
        c.show();
    }
}
// END ANSWER
