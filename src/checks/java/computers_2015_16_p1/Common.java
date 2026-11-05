// BEGIN ANSWER
import java.util.Scanner;
class Common {
    int arr[];      // elements of this object's array
    int n;          // size of the array
    static Scanner sc = new Scanner(System.in);

    // constructor: stores the size and creates the array
    // (the paper writes "void common(int nn)"; a constructor has no return type)
    Common(int nn) {
        n = nn;
        arr = new int[n];
    }

    // reads n elements, rejecting a value already entered (no duplicates)
    void accept() {
        System.out.println("Enter " + n + " distinct elements:");
        int i = 0;
        while (i < n) {
            int v = sc.nextInt();
            boolean dup = false;
            for (int j = 0; j < i; j++)
                if (arr[j] == v)
                    dup = true;
            if (dup)
                System.out.println(v + " already entered, enter another value");
            else
                arr[i++] = v;
        }
    }

    // prints the elements of this object that also occur in object A
    void display(Common A) {
        boolean found = false;
        System.out.print("Common elements: ");
        for (int i = 0; i < n; i++)
            for (int j = 0; j < A.n; j++)
                if (arr[i] == A.arr[j]) {   // A's array, reached through the object
                    System.out.print(arr[i] + " ");
                    found = true;
                }
        if (!found)
            System.out.print("none - no common element found");
        System.out.println();
    }

    public static void main(String args[]) {
        System.out.println("Size of first array: ");
        Common ob1 = new Common(sc.nextInt());
        ob1.accept();
        System.out.println("Size of second array: ");
        Common ob2 = new Common(sc.nextInt());
        ob2.accept();
        ob1.display(ob2);
    }
}
// END ANSWER
