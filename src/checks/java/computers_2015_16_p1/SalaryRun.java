public class SalaryRun {        // runner only (main need not be written)
    public static void main(String[] args) {
        salary s = new salary("Amit Sen", 20000.0);
        s.calDA();
        s.calGP();
        s.show();
    }
}
// BEGIN ANSWER
class employee {                    // the super class, as described in the paper
    String name;
    double basicpay;
    double DA;

    employee(String n, double b) {
        name = n;
        basicpay = b;
        DA = 0.0;
    }

    void calDA() {
        DA = 0.35 * basicpay;       // 35% of basic pay
    }
}

class salary extends employee {
    double grosspay;                // basic pay + DA

    // passes name and basic pay up to the super class constructor
    salary(String n, double b) {
        super(n, b);
        grosspay = 0.0;
    }

    void calGP() {
        calDA();                    // make sure DA is computed first
        grosspay = basicpay + DA;   // inherited members used directly
    }

    void show() {
        System.out.println("Name       : " + name);
        System.out.println("Basic pay  : " + basicpay);
        System.out.println("DA         : " + DA);
        System.out.println("Gross pay  : " + grosspay);
    }
}
// END ANSWER
