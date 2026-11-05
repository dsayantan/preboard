// BEGIN ANSWER
import java.util.Scanner;
// END ANSWER
public class RetireRun {   // test runner only: the launcher needs main in the first class
    public static void main(String[] a) { Retire.main(a); }
}
// BEGIN ANSWER
class Personal {
    String empName;     // employee name
    String Pan;         // PAN number
    double basicPay;    // basic salary ("basic-pay" is not a legal Java name)
    String acc_no;      // bank account number

    Personal(String n, String p, double b, String a) {
        empName = n;
        Pan = p;
        basicPay = b;
        acc_no = a;
    }

    void display() {
        System.out.println("Name           : " + empName);
        System.out.println("PAN            : " + Pan);
        System.out.println("Basic pay      : " + basicPay);
        System.out.println("Account number : " + acc_no);
    }
}

class Retire extends Personal {
    int yrs;            // years of service
    double pf;          // provident fund
    double grat;        // gratuity

    Retire(String n, String p, double b, String a, int y) {
        super(n, p, b, a);          // the super class stores the personal details
        yrs = y;
        pf = 0.0;
        grat = 0.0;
    }

    void provident() {
        pf = (0.02 * basicPay) * yrs;      // 2% of basic pay for each year
    }

    void gratuity() {
        if (yrs >= 10)
            grat = 12 * basicPay;          // 12 months' salary
        else
            grat = 0.0;                    // nil
    }

    void display1() {
        display();                         // inherited: personal details
        System.out.println("Years of service : " + yrs);
        System.out.println("Provident fund   : " + pf);
        System.out.println("Gratuity         : " + grat);
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Name, PAN, basic pay, account no, years: ");
        String n = sc.next(), p = sc.next();
        double b = sc.nextDouble();
        String a = sc.next();
        int y = sc.nextInt();
        Retire ob = new Retire(n, p, b, a, y);
        ob.provident();
        ob.gratuity();
        ob.display1();
    }
}
// END ANSWER
