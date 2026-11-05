// BEGIN ANSWER
import java.util.Scanner;

public class Keypad
{
    // letters on keys 2 to 9; KEYS[d - 2] holds the letters on key d
    static final String KEYS[] = {"ABC", "DEF", "GHI", "JKL",
                                  "MNO", "PQRS", "TUV", "WXYZ"};

    // the key that carries letter ch
    static int key(char ch)
    {
        for (int d = 0; d < KEYS.length; d++)
            if (KEYS[d].indexOf(ch) >= 0)
                return d + 2;
        return -1;
    }

    // presses needed for ch: its position on its key, counting from 1
    static int presses(char ch)
    {
        return KEYS[key(ch) - 2].indexOf(ch) + 1;
    }

    static String times(int n)
    {
        return n == 1 ? "1 time" : n + " times";
    }

    /* prints, for one word, every key used and the total presses on it,
       keys listed in the order they are first used */
    static void word(String w)
    {
        System.out.println(w);
        int count[] = new int[10];      // presses per key 0..9
        int order[] = new int[10];      // keys in order of first use
        int k = 0;
        for (int i = 0; i < w.length(); i++)
        {
            char ch = w.charAt(i);
            int d = key(ch);
            if (count[d] == 0)
                order[k++] = d;
            count[d] += presses(ch);
        }
        for (int i = 0; i < k; i++)
            System.out.println("Number " + order[i] + " is pressed "
                               + times(count[order[i]]));
    }

    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine().trim().toUpperCase();
        // only letters and single spaces between words are allowed
        boolean ok = s.length() > 0;
        for (int i = 0; i < s.length() && ok; i++)
        {
            char ch = s.charAt(i);
            if (!(Character.isLetter(ch) || ch == ' '))
                ok = false;
            if (ch == ' ' && s.charAt(i + 1) == ' ')
                ok = false;
        }
        if (!ok)
        {
            System.out.println("Invalid Entry");
            return;
        }
        String w[] = s.split(" ");
        for (int i = 0; i < w.length; i++)
        {
            if (i > 0)
            {
                System.out.println("White Space");
                System.out.println("Number 0 is pressed 1 time.");
            }
            word(w[i]);
        }
    }
}
// END ANSWER
