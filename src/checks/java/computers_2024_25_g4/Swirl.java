// BEGIN ANSWER
import java.util.Scanner;

public class Swirl
{
    int arr[][];     // the matrix
    int M;           // number of rows
    int N;           // number of columns
    int k;           // position wanted in the spiral order

    // constructor: legal initial values
    Swirl()
    {
        M = 0;
        N = 0;
        k = 0;
        arr = new int[1][1];
    }

    // accepts the order, the elements and k
    void read()
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of rows and columns :");
        M = sc.nextInt();
        N = sc.nextInt();
        arr = new int[M][N];
        System.out.println("Enter the elements row by row :");
        for (int i = 0; i < M; i++)
            for (int j = 0; j < N; j++)
                arr[i][j] = sc.nextInt();
        System.out.println("Enter k :");
        k = sc.nextInt();
    }

    /* Walks the matrix in spiral order - top row left to right, right
       column downwards, bottom row right to left, left column upwards -
       then moves the four boundaries inwards, counting elements
       until the k-th. */
    int element_k()
    {
        int top = 0, bottom = M - 1, left = 0, right = N - 1;
        int count = 0;
        while (top <= bottom && left <= right)
        {
            for (int j = left; j <= right; j++)            // top row
                if (++count == k) return arr[top][j];
            top++;
            for (int i = top; i <= bottom; i++)            // right column
                if (++count == k) return arr[i][right];
            right--;
            if (top <= bottom)
            {
                for (int j = right; j >= left; j--)        // bottom row
                    if (++count == k) return arr[bottom][j];
                bottom--;
            }
            if (left <= right)
            {
                for (int i = bottom; i >= top; i--)        // left column
                    if (++count == k) return arr[i][left];
                left++;
            }
        }
        // k out of range
        return -1;
    }

    // displays the k-th element
    void show()
    {
        if (k < 1 || k > M * N)
        {
            System.out.println("Invalid k : the matrix has only "
                               + (M * N) + " elements");
            return;
        }
        System.out.println("Element number " + k + " in spiral order = "
                           + element_k());
    }

    public static void main(String args[])
    {
        Swirl ob = new Swirl();
        ob.read();
        ob.show();
    }
}
// END ANSWER
