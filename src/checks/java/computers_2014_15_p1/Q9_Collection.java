// ANSWER-START
import java.util.Scanner;
// ANSWER-END

class Q9_Run {
    public static void main(String[] a) {
        Collection x = new Collection(6), y = new Collection(5);
        x.readArray();
        y.readArray();
        Collection z = x.common(y);
        z.displayArray();
    }
}

// ANSWER-START
class Collection {
    int arr[];                          // the elements
    // number of elements in use
    int len;
    static Scanner sc = new Scanner(System.in);

    Collection() {                      // default constructor
        arr = new int[100];
        len = 0;
    }

    // array of length n (at most 100)
    Collection(int n) {
        arr = new int[100];
        len = Math.min(n, 100);
    }

    void readArray() {
        System.out.println("Enter " + len + " integers:");
        for (int i = 0; i < len; i++)
            arr[i] = sc.nextInt();
    }

    // elements in both this array and ob's
    Collection common(Collection ob) {
        Collection res = new Collection();
        for (int i = 0; i < len; i++) {
            boolean inOther = false, already = false;
            for (int j = 0; j < ob.len; j++)
                if (arr[i] == ob.arr[j]) {
                    inOther = true;
                    break;
                }
            // keep each common value once
            for (int k = 0; k < res.len; k++)
                if (res.arr[k] == arr[i]) {
                    already = true;
                    break;
                }
            if (inOther && !already)
                res.arr[res.len++] = arr[i];
        }
        return res;
    }

    void displayArray() {
        for (int i = 0; i < len; i++)
            System.out.print(arr[i] + " ");
        System.out.println();
    }
}
// ANSWER-END
