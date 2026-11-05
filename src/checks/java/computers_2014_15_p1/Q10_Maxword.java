// ANSWER-START
import java.util.Scanner;
import java.util.StringTokenizer;

class Maxword_paragraph {
    String sent;                     // the paragraph
    // rem[5][n]: one sentence per row, one word per cell
    String rem[][];

    Maxword_paragraph() {
        sent = "";
    }

    // accept a paragraph of exactly 5 sentences
    void readparagraph() {
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.println("Enter 5 sentences, each ending in . or !");
            sent = sc.nextLine().trim();
            int count = 0;
            for (int i = 0; i < sent.length(); i++) {
                char ch = sent.charAt(i);
                if (ch == '.' || ch == '!')
                    count++;
            }
            int L = sent.length();
            char last = (L > 0) ? sent.charAt(L - 1) : ' ';
            if (count == 5 && (last == '.' || last == '!'))
                break;
            System.out.println("INVALID INPUT");
        }
    }

    void para_to_array() {
        StringTokenizer st = new StringTokenizer(sent, ".!");
        String s[] = new String[5];
        // words in the longest sentence
        int n = 0;
        for (int r = 0; r < 5; r++) {
            s[r] = st.nextToken().trim();
            n = Math.max(n, new StringTokenizer(s[r], " ,;:?").countTokens());
        }
        rem = new String[5][n];
        for (int r = 0; r < 5; r++) {
            StringTokenizer w = new StringTokenizer(s[r], " ,;:?");
            for (int c = 0; c < n; c++)
                // blank cells get "Q"
                rem[r][c] = w.hasMoreTokens() ? w.nextToken() : "Q";
        }
        // display the array
        for (int r = 0; r < 5; r++) {
            for (int c = 0; c < n; c++)
                System.out.print(rem[r][c] + "\t");
            System.out.println();
        }
    }

    // longest word and where it is stored
    void word_max() {
        int mr = 0, mc = 0;
        for (int r = 0; r < rem.length; r++)
            for (int c = 0; c < rem[r].length; c++)
                if (!rem[r][c].equals("Q")
                        && rem[r][c].length() > rem[mr][mc].length()) {
                    mr = r;
                    mc = c;
                }
        System.out.println("Longest word: " + rem[mr][mc]
                + " at rem[" + mr + "][" + mc + "]");
    }

    public static void main(String args[]) {
        Maxword_paragraph ob = new Maxword_paragraph();
        ob.readparagraph();
        ob.para_to_array();
        ob.word_max();
    }
}
// ANSWER-END
