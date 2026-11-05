// BEGIN ANSWER
import java.util.Scanner;

public class Mix_sort
{
    int a[][];      // the matrix
    int m, n;       // rows, columns
    int orig[][];   // copy of the original, kept for display()
    static Scanner sc = new Scanner(System.in);

    Mix_sort(int row, int col)
    {
        m = row;
        n = col;
        a = new int[m][n];
        orig = new int[m][n];
    }

    void input()
    {
        System.out.println("Enter the array elements");
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
            {
                a[i][j] = sc.nextInt();
                orig[i][j] = a[i][j];
            }
    }

    // insertion sort, ascending
    void ascEven(int x[])
    {
        for (int i = 1; i < x.length; i++)
        {
            int key = x[i];
            int j = i - 1;
            while (j >= 0 && x[j] > key)     // shift larger elements right
            {
                x[j + 1] = x[j];
                j--;
            }
            x[j + 1] = key;
        }
    }

    // insertion sort, descending
    void dscOdd(int x[])
    {
        for (int i = 1; i < x.length; i++)
        {
            int key = x[i];
            int j = i - 1;
            while (j >= 0 && x[j] < key)     // shift smaller elements right
            {
                x[j + 1] = x[j];
                j--;
            }
            x[j + 1] = key;
        }
    }

    // rows are numbered from 1 as in the sample: rows 1, 3, 5 ... (odd
    // positions) descending, rows 2, 4, 6 ... (even positions) ascending
    void arrange()
    {
        for (int i = 0; i < m; i++)
        {
            int x[] = new int[n];
            for (int j = 0; j < n; j++)      // copy row i out
                x[j] = a[i][j];
            if ((i + 1) % 2 == 0)
                ascEven(x);
            else
                dscOdd(x);
            for (int j = 0; j < n; j++)      // store the sorted row back
                a[i][j] = x[j];
        }
    }

    void display()
    {
        System.out.println("Before sort :");
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
                System.out.print(orig[i][j] + " ");
            System.out.println();
        }
        System.out.println("After sort :");
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
                System.out.print(a[i][j] + " ");
            System.out.println();
        }
    }

    public static void main(String args[])
    {
        System.out.print("Row = ");
        int r = sc.nextInt();
        System.out.print("Column = ");
        int c = sc.nextInt();
        Mix_sort ob = new Mix_sort(r, c);
        ob.input();
        ob.arrange();
        ob.display();
    }
}
// END ANSWER
