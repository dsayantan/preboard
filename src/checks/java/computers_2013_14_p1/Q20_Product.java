// ANSWER-START
import java.util.Scanner;
// ANSWER-END

class Q20_Run {
    public static void main(String[] a) {
        dervpro d = new dervpro();
        d.prod();
        d.disp();
    }
}

// ANSWER-START
class basepro {
    protected float n1, n2;           // the two numbers

    void enter() {                    // inputs n1 and n2
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter two numbers: ");
        n1 = sc.nextFloat();
        n2 = sc.nextFloat();
    }

    void show() {                     // displays n1 and n2
        System.out.println("n1 = " + n1 + ", n2 = " + n2);
    }
}

class dervpro extends basepro {
    float result;                     // product

    void prod() {
        enter();                      // inherited from basepro
        // n1, n2 are protected: visible here
        result = n1 * n2;
    }

    void disp() {
        // inherited display of n1 and n2
        show();
        System.out.println("Product = " + result);
    }
}
// ANSWER-END
