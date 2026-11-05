// ANSWER-START
class Output {
    public static void main(String args[]) {
        int x = 10, y = 5, z;
        z = first(x, y);
        System.out.println("\n z=" + z);
    }
    static int first(int x, int y) {
        return (x + second(y));
    }
    static int second(int y) {
        return (++y);
    }
}
// ANSWER-END
