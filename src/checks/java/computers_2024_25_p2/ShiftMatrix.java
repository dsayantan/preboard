// BEGIN ANSWER
import java.util.Scanner;

public class ShiftMatrix
{
    int A[][];      // the matrix
    int M, N;       // rows and columns

    ShiftMatrix(int m, int n)
    {
        M = m;
        N = n;
        A = new int[M][N];
    }

    void input(Scanner sc)
    {
        System.out.println("Enter the elements in the matrix:");
        for (int i = 0; i < M; i++)
            for (int j = 0; j < N; j++)
                A[i][j] = sc.nextInt();
    }

    void display(String msg)
    {
        System.out.println(msg);
        for (int i = 0; i < M; i++)
        {
            for (int j = 0; j < N; j++)
                System.out.printf("%6d", A[i][j]);
            System.out.println();
        }
    }

    // each column moves one step right; the last comes round to the first
    void shift()
    {
        for (int i = 0; i < M; i++)
        {
            int last = A[i][N - 1];
            for (int j = N - 1; j > 0; j--)
                A[i][j] = A[i][j - 1];
            A[i][0] = last;
        }
    }

    /* second smallest DISTINCT value and its location (first occurrence,
       scanning row by row) in the shifted matrix */
    void secondSmallest()
    {
        int min = A[0][0];
        for (int i = 0; i < M; i++)
            for (int j = 0; j < N; j++)
                if (A[i][j] < min)
                    min = A[i][j];
        boolean found = false;
        int sec = 0, r = -1, c = -1;
        for (int i = 0; i < M; i++)
            for (int j = 0; j < N; j++)
                if (A[i][j] > min && (!found || A[i][j] < sec))
                {
                    sec = A[i][j];
                    r = i;
                    c = j;
                    found = true;
                }
        if (!found)
            System.out.println("No second smallest element: "
                               + "all elements are equal");
        else
            System.out.println("Second Smallest Element : " + sec
                               + " (Row: " + r + " and Column: " + c
                               + ")");
    }

    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("M = ");
        int m = sc.nextInt();
        System.out.println(m);
        System.out.print("N = ");
        int n = sc.nextInt();
        System.out.println(n);
        if (m <= 2 || m >= 10 || n <= 2 || n >= 10)
        {
            System.out.println("Size is out of Range. Invalid Entry");
            return;
        }
        ShiftMatrix ob = new ShiftMatrix(m, n);
        ob.input(sc);
        ob.display("Input matrix");
        ob.shift();
        ob.display("Formed matrix after shifting");
        ob.secondSmallest();
    }
}
// END ANSWER
