// BEGIN ANSWER
import java.util.Scanner;
class ParagraphSort {
    String str;         // the paragraph
    String lines[];     // the sentences, one per element
    int wrds[];         // number of words in each sentence

    ParagraphSort(String s) {
        str = s.trim();
    }

    // splits the paragraph into sentences at '.', '?' or '!'
    // and counts the words of each
    void split() {
        int count = 0;                          // number of sentences
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if (ch == '.' || ch == '?' || ch == '!')
                count++;
        }
        lines = new String[count];
        wrds = new int[count];
        int k = 0, start = 0;
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if (ch == '.' || ch == '?' || ch == '!') {
                lines[k] = str.substring(start, i + 1).trim();   // keep the terminator
                wrds[k] = countWords(lines[k]);
                k++;
                start = i + 1;
            }
        }
    }

    // number of words = number of blank-separated tokens
    int countWords(String s) {
        int c = 0;
        boolean inWord = false;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != ' ' && !inWord) {   // a word starts here
                c++;
                inWord = true;
            } else if (s.charAt(i) == ' ')
                inWord = false;
        }
        return c;
    }

    // bubble sort in DECREASING order of word count, moving the sentence
    // together with its count; equal counts keep their original order
    void sort(String lines[], int wrds[]) {
        int n = wrds.length;
        for (int i = 0; i < n - 1; i++)
            for (int j = 0; j < n - 1 - i; j++)
                if (wrds[j] < wrds[j + 1]) {
                    int t = wrds[j]; wrds[j] = wrds[j + 1]; wrds[j + 1] = t;
                    String s = lines[j]; lines[j] = lines[j + 1]; lines[j + 1] = s;
                }
    }

    void print(String lines[], int wrds[]) {
        for (int i = 0; i < lines.length; i++)
            System.out.println(lines[i] + "   [words = " + wrds[i] + "]");
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the paragraph:");
        ParagraphSort ob = new ParagraphSort(sc.nextLine());
        ob.split();
        ob.sort(ob.lines, ob.wrds);
        ob.print(ob.lines, ob.wrds);
    }
}
// END ANSWER
