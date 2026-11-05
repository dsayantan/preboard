// BEGIN ANSWER
import java.util.Scanner;

public class Anagram
{
    String s1, s2;          // the two words in lower case
    int l1, l2;             // number of characters in s1 and s2

    // parameterised constructor
    Anagram(String s1, String s2)
    {
        this.s1 = s1.toLowerCase();
        this.s2 = s2.toLowerCase();
        l1 = this.s1.length();
        l2 = this.s2.length();
    }

    // sorts c[] in ascending order (bubble sort)
    void sort(char c[])
    {
        for (int i = 0; i < c.length - 1; i++)
            for (int j = 0; j < c.length - 1 - i; j++)
                if (c[j] > c[j + 1])
                {
                    char t = c[j];
                    c[j] = c[j + 1];
                    c[j + 1] = t;
                }
    }

    // true if str1 and str2 hold the same letters
    boolean areAnagram(char[] str1, char[] str2)
    {
        if (str1.length != str2.length)
            return false;
        sort(str1);
        sort(str2);
        for (int i = 0; i < str1.length; i++)
            if (str1[i] != str2[i])
                return false;
        return true;
    }

    void check()
    {
        char a[] = s1.toCharArray();
        char b[] = s2.toCharArray();
        if (areAnagram(a, b))
            System.out.println(s1 + " and " + s2
                               + " are anagram of each other");
        else
            System.out.println(s1 + " and " + s2
                               + " are not anagram of each other");
    }

    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter first word -> ");
        String w1 = sc.next();
        System.out.print("Enter second word -> ");
        String w2 = sc.next();
        Anagram ob = new Anagram(w1, w2);
        ob.check();
    }
}
// END ANSWER
