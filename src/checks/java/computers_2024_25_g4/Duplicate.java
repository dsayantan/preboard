// BEGIN ANSWER
import java.util.Scanner;

public class Duplicate
{
    String wrd;     // the original string
    String nw;      // the string with duplicate characters removed
    int len;        // length of wrd

    // default constructor
    Duplicate()
    {
        wrd = "";
        nw = "";
        len = 0;
    }

    // accepts the string
    void acceptword()
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a string :");
        wrd = sc.nextLine();
        len = wrd.length();
    }

    /* Recursive: s is the original string, r the result built so far,
       i the index of the character being examined.
       A character is added to r only if it is not already in r,
       so only its first occurrence survives. */
    String remvDup(String s, String r, int i)
    {
        // base case: whole string examined
        if (i == len)
            return r;
        char ch = s.charAt(i);
        if (r.indexOf(ch) == -1)              // not seen before: keep it
            r = r + ch;
        // examine the next character
        return remvDup(s, r, i + 1);
    }

    // displays the original and the modified string
    void display()
    {
        nw = remvDup(wrd, "", 0);
        System.out.println("Original string : " + wrd);
        System.out.println("String after removing duplicate characters : "
                           + nw);
    }

    public static void main(String args[])
    {
        Duplicate ob = new Duplicate();
        ob.acceptword();
        ob.display();
    }
}
// END ANSWER
