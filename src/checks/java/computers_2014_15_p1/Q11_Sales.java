class Q11_Run {
    public static void main(String[] a) {
        Sales s = new Sales("R. Sen", "Kolkata", 101, 5, 250.0, 1200.0, "Pen drive");
        s.show();
    }
}

// ANSWER-START
class Salesman {
    String name, address;

    Salesman(String n, String ad) {
        name = n;
        address = ad;
    }

    void show() {
        System.out.println("Name of salesman : " + name);
        System.out.println("Address          : " + address);
    }
}

class Sales extends Salesman {
    int billno, qty;
    double price, psales;
    String pname;

    Sales(String n, String ad, int b, int q,
          double p, double s, String pr) {
        // constructor of the base class first
        super(n, ad);
        billno = b;
        qty = q;
        price = p;
        psales = s;
        pname = pr;
    }

    double calculate() {
        return price * qty + psales;  // total sales
    }

    void show() {                     // overrides Salesman.show()
        // display of the super class
        super.show();
        System.out.println("Product          : " + pname);
        System.out.println("Bill number      : " + billno);
        System.out.println("Quantity         : " + qty);
        System.out.println("Previous sales   : " + psales);
        System.out.println("Total sales      : " + calculate());
    }
}
// ANSWER-END
