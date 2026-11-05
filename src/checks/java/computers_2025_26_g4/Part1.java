// Part I checks: Q1(vi), Q1(vii), Q2(iii) findPos, Q2(iv) tribonacci
public class Part1 {
    public static void main(String[] a) {
        System.out.println("Q1vi " + "RocKet".substring(0,4).compareTo("Rock".replace('m','o')));
        char[] set = {'*','D','5'};
        System.out.print("Q1vii ");
        System.out.print(Character.isDigit(set[2])+" ");
        System.out.print(Character.isWhitespace(set[0])+" ");
        System.out.println(Character.isLetterOrDigit(set[1]));
        Part1 p = new Part1();
        int[] arr = {3, 7, 12, 18, 25, 31, 42, 53};
        System.out.println("Q2iii " + p.findPos(arr, 0, arr.length - 1, 31));
        StringBuilder sb = new StringBuilder("Q2iv");
        for (int n = 0; n < 8; n++) sb.append(" ").append(p.tribonacci(n));
        System.out.println(sb);
    }
    int depth = 0;
    public int findPos(int arr[], int f, int l, int x) {
        System.out.println("call findPos(f=" + f + ", l=" + l + ")");
        if (f > l) return -1;
        int m = (2 * f + l) / 3;
        System.out.println("  m=" + m + " arr[m]=" + arr[m]);
        if (arr[m] == x) return m;
        else if (arr[m] > x) return findPos(arr, f, m - 1, x);
        else {
            int k = findPos(arr, m + 1, l, x);
            System.out.println("  returned k=" + k);
            if (k == -1) return -1;
            else return k + 1;
        }
    }
// BEGIN ANSWER
public int tribonacci(int n)
{
   if (n == 0)                       // ?1
      return 0;
   else if (n == 1 || n == 2)        // ?2
      return 1;
   else
      return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3);   // ?3
}
// END ANSWER
}
