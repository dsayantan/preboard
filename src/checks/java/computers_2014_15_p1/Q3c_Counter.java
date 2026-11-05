// ANSWER-START
class Counter {
    static int c = 10;
    Counter() {
        c++;
        System.out.println("THE VALUE IS - " + c);
    }
    public static void main(String args[]) {
        Counter c1 = new Counter();
        Counter c2 = new Counter();
        Counter c3 = new Counter();
    }
}
// ANSWER-END
