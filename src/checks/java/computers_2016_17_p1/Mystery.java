public class Mystery {
    public static void main(String[] args) {
        mystery(8);
        System.out.println();
    }
// BEGIN ANSWER
    public static void mystery(int n) {
        if (n <= 1) {
            System.out.print(": ");
        } else {
            System.out.print((n % 2) + " ");
            mystery(n / 2);
            System.out.print(n + " ");
        }
    }
// END ANSWER
}
