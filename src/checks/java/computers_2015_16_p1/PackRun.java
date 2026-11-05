// BEGIN ANSWER
import java.util.Scanner;
// END ANSWER
// Runner first: the single-file launcher takes main() from the first class.
public class PackRun {
    public static void main(String[] args) {
        Pack p = new Pack();
        p.accept();
        p.packer(1, 0);      // start comparing from index 1; index 0 is always kept
        p.printer();
    }
}
// BEGIN ANSWER
class Pack {
    int size;       // number of elements currently in the array
    int n[];        // the sorted values

    // reads the size and the (already sorted) values
    void accept() {
        Scanner sc = new Scanner(System.in);
        size = sc.nextInt();
        n = new int[size];
        for (int i = 0; i < size; i++)
            n[i] = sc.nextInt();
    }

    // Recursive packing.
    // i : index of the element being examined
    // k : index of the last element kept so far (n[0..k] is already packed)
    void packer(int i, int k) {
        if (size == 0)
            return;
        if (i == size) {          // base case: every element examined
            size = k + 1;         // the packed array is n[0..k]
            return;
        }
        if (n[i] != n[k]) {       // a new value (sorted: no repeat later)
            k++;
            n[k] = n[i];          // move it next to the last kept value
        }
        packer(i + 1, k);         // smaller problem: one element fewer
    }

    // prints the packed array
    void printer() {
        for (int i = 0; i < size; i++)
            System.out.print(n[i] + (i < size - 1 ? "," : "\n"));
    }
}
// END ANSWER
