// BEGIN ANSWER
import java.util.Scanner;
// END ANSWER
public class MidRun {           // runner only (the paper says no main is needed)
    public static void main(String[] args) {
        MIDSORT m = new MIDSORT();
        m.readdata();
        m.centre();
        m.print();
    }
}
// BEGIN ANSWER
class MIDSORT {
    String word;    // the word entered (later, the rearranged word)
    int len;        // its length

    // reads a word
    void readdata() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a word: ");
        word = sc.next();
        len = word.length();
    }

    // smallest letter in the centre, then the next bigger to its left,
    // the next to its right, and so on alternately
    void centre() {
        char c[] = word.toCharArray();
        // bubble sort the letters in ascending order
        for (int i = 0; i < len - 1; i++)
            for (int j = 0; j < len - 1 - i; j++)
                if (c[j] > c[j + 1]) {
                    char t = c[j]; c[j] = c[j + 1]; c[j + 1] = t;
                }
        char res[] = new char[len];
        int mid = len / 2;           // centre position
        res[mid] = c[0];             // smallest letter in the centre
        int left = mid - 1, right = mid + 1;
        for (int k = 1; k < len; k++) {
            if (k % 2 == 1)          // 1st, 3rd, 5th ... next letters go to the left
                res[left--] = c[k];
            else                     // 2nd, 4th, 6th ... go to the right
                res[right++] = c[k];
        }
        word = new String(res);
    }

    // prints the changed word
    void print() {
        System.out.println("Output : " + word);
    }
}
// END ANSWER
