class Q19_Run {
    public static void main(String[] a) {
        new Checker(12321L).display();
        new Checker(12345L).display();
        new Checker(7L).display();
    }
}

// ANSWER-START
class Checker {
    long num;                   // the number
    long rev;                   // its reverse

    Checker(long z) {           // constructor
        num = z;
        rev = 0;
    }

    // recursive: moves the last digit of q onto rev
    long ReverseNum(long q) {
        if (q == 0)             // base case: no digits left
            return rev;
        rev = rev * 10 + q % 10;
        return ReverseNum(q / 10);
    }

    void display() {
        rev = 0;
        long r = ReverseNum(num);
        if (r == num)
            System.out.println(num + " is a palindrome number");
        else
            System.out.println(num + " is not a palindrome number");
    }
}
// ANSWER-END
