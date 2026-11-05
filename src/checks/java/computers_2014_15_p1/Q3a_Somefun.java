class Q3a_Somefun {
    // ANSWER-START
    static int somefun(String s, int last) {
        if (last < 0)
            return 0;
        if (s.charAt(last) == '0')
            return 2 * somefun(s, last - 1);
        else
            return 1 + 2 * somefun(s, last - 1);
    }
    // ANSWER-END
    public static void main(String[] a) {
        System.out.println(somefun("10011", 4));
        System.out.println(somefun("001001101", 5));
        for (int k = 0; k <= 4; k++) System.out.println("somefun(\"10011\"," + k + ") = " + somefun("10011", k));
    }
}
