// BEGIN ANSWER
import java.util.Scanner;
import java.util.StringTokenizer;

/* Merge cipher.
 * Encrypt: pair word 1 with the last word, word 2 with the last-but-one, ...
 *   A pair is merged letter by letter, first word's letter first; where the
 *   shorter word has run out its place is taken by '*'.
 *   With an odd number of words the middle word has no partner: it is
 *   reversed and written as *...*.
 * Decrypt: a token beginning with '*' is the middle word; in every other token
 *   the letters at even positions belong to the first word of the pair and
 *   those at odd positions to the second ('*' fillers are dropped).          */
class MergeCipher {

    // splits a sentence into words, dropping the full stop / ? / ! at the end
    String[] words(String s) {
        s = s.trim();
        char last = s.charAt(s.length() - 1);
        if (last == '.' || last == '?' || last == '!')
            s = s.substring(0, s.length() - 1);
        StringTokenizer st = new StringTokenizer(s);
        String w[] = new String[st.countTokens()];
        for (int i = 0; i < w.length; i++)
            w[i] = st.nextToken();
        return w;
    }

    // merges two words, padding the shorter one with '*'
    String merge(String a, String b) {
        String r = "";
        int L = Math.max(a.length(), b.length());
        for (int i = 0; i < L; i++) {
            r += (i < a.length()) ? a.charAt(i) : '*';
            r += (i < b.length()) ? b.charAt(i) : '*';
        }
        return r;
    }

    String reverse(String a) {
        String r = "";
        for (int i = a.length() - 1; i >= 0; i--)
            r += a.charAt(i);
        return r;
    }

    String encrypt(String sentence) {
        String w[] = words(sentence);
        int n = w.length;
        String out = "";
        for (int i = 0; i < n / 2; i++)             // the pairs, outside in
            out += merge(w[i], w[n - 1 - i]) + " ";
        if (n % 2 == 1)                             // the unpaired middle word
            out += "*" + reverse(w[n / 2]) + "*";
        return out.trim();
    }

    String decrypt(String code) {
        String t[] = words(code);
        int pairs = t.length, mid = 0;
        String middle = "";
        if (t[t.length - 1].charAt(0) == '*') {     // last token is the middle word
            pairs = t.length - 1;
            mid = 1;
            String m = t[t.length - 1];
            middle = reverse(m.substring(1, m.length() - 1));
        }
        int n = 2 * pairs + mid;                    // number of words in the sentence
        String w[] = new String[n];
        for (int k = 0; k < pairs; k++) {
            String a = "", b = "";
            for (int i = 0; i < t[k].length(); i++) {
                char ch = t[k].charAt(i);
                if (ch == '*')
                    continue;                       // filler, not a letter
                if (i % 2 == 0) a += ch; else b += ch;
            }
            w[k] = a;                               // k-th word from the front
            w[n - 1 - k] = b;                       // k-th word from the back
        }
        if (mid == 1)
            w[n / 2] = middle;
        String out = "";
        for (int i = 0; i < n; i++)
            out += w[i] + (i < n - 1 ? " " : "");
        return out;
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        MergeCipher ob = new MergeCipher();
        System.out.println("1. Encrypted to original   2. Original to encrypted");
        int ch = Integer.parseInt(sc.nextLine().trim());
        System.out.println("Enter the word / sentence:");
        String s = sc.nextLine().toUpperCase();
        if (s.trim().length() == 0) {
            System.out.println("INVALID INPUT");
            return;
        }
        if (ch == 1)
            System.out.println("Original Sentence : " + ob.decrypt(s));
        else if (ch == 2)
            System.out.println("Encrypted Sentence : " + ob.encrypt(s));
        else
            System.out.println("INVALID CHOICE");
    }
}
// END ANSWER
