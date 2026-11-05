// BEGIN ANSWER
import java.util.Scanner;

/* Fills an n x n matrix with 1 .. n*n ring by ring, from the outside in.
 * As the paper's three samples show, the rings alternate in direction:
 *   ring 0, 2, 4 ... clockwise      (start top-left, go RIGHT first)
 *   ring 1, 3, 5 ... anticlockwise  (start top-left, go DOWN first)  */
class CircularMatrix {
    int n;          // order of the matrix
    int m[][];      // the matrix

    CircularMatrix(int size) {
        n = size;
        m = new int[n][n];
    }

    void fill() {
        int k = 1;                              // next value to place
        for (int r = 0; r < (n + 1) / 2; r++) { // r = ring number
            int lo = r, hi = n - 1 - r;         // first and last row/column of this ring
            if (lo == hi) {                     // odd n: the single centre cell
                m[lo][lo] = k++;
                break;
            }
            if (r % 2 == 0) {                   // clockwise ring
                for (int j = lo; j <= hi; j++)     m[lo][j] = k++;   // top row, left to right
                for (int i = lo + 1; i <= hi; i++) m[i][hi] = k++;   // right column, down
                for (int j = hi - 1; j >= lo; j--) m[hi][j] = k++;   // bottom row, right to left
                for (int i = hi - 1; i > lo; i--)  m[i][lo] = k++;   // left column, up
            } else {                            // anticlockwise ring
                for (int i = lo; i <= hi; i++)     m[i][lo] = k++;   // left column, down
                for (int j = lo + 1; j <= hi; j++) m[hi][j] = k++;   // bottom row, left to right
                for (int i = hi - 1; i >= lo; i--) m[i][hi] = k++;   // right column, up
                for (int j = hi - 1; j > lo; j--)  m[lo][j] = k++;   // top row, right to left
            }
        }
    }

    void display() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++)
                System.out.print(String.format("%4d", m[i][j]));
            System.out.println();
        }
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size n: ");
        int size = sc.nextInt();
        if (size < 1) {
            System.out.println("INVALID SIZE");
            return;
        }
        CircularMatrix ob = new CircularMatrix(size);
        ob.fill();
        ob.display();
    }
}
// END ANSWER
