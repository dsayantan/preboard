class Q3b_Rec {
    public static String fun_with_recursion(String str) {
        if (str.length() < 2) {
            return str;
        }
        return fun_with_recursion(str.substring(1)) + str.charAt(0);
    }
    public static void main(String[] a) {
        System.out.println("[" + fun_with_recursion("Hello World!") + "]");
        System.out.println("[" + fun_with_recursion(" Hello World!") + "]");
    }
}
