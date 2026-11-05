// BEGIN ANSWER
import java.util.Scanner;

/* Finds the pair (i, j), i < j, whose elements differ the least.
 * Pairs are examined with i increasing and, for each i, j increasing, and the
 * stored pair is replaced only by a STRICTLY smaller difference.  So on a tie
 * the pair with the lower first index is kept, and if the first indices are
 * equal, the one with the lower second index -- exactly conditions 2 and 3.  */
class MinDiff {
    int a[];        // the array
    int n;          // its size

    MinDiff(int size) {
        n = size;
        a = new int[n];
    }

    void accept(Scanner sc) {
        for (int i = 0; i < n; i++)
            a[i] = sc.nextInt();
    }

    // returns {i, j} of the pair with the smallest difference
    int[] closest() {
        int bi = 0, bj = 1;
        int best = Math.abs(a[0] - a[1]);
        for (int i = 0; i < n - 1; i++)
            for (int j = i + 1; j < n; j++) {
                int d = Math.abs(a[i] - a[j]);     // actual difference of the elements
                if (d < best) {                    // strictly smaller only
                    best = d;
                    bi = i;
                    bj = j;
                }
            }
        return new int[]{bi, bj};
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Number of elements:");
        int size = sc.nextInt();
        if (size < 2) {
            System.out.println("INVALID INPUT: at least two elements are needed");
            return;
        }
        MinDiff ob = new MinDiff(size);
        System.out.println("Enter the elements:");
        ob.accept(sc);
        int p[] = ob.closest();
        System.out.println("The indices are " + p[0] + ", " + p[1] + ".");
    }
}
// END ANSWER
