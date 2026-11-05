// runner: the single-file launcher takes main from the FIRST class in the file
class Run { public static void main(String[] a) { Main.main(a); } }

// BEGIN ANSWER
interface Staff
{
    // no instance data in an interface; the method is public and abstract
    void display();
}

class Worker implements Staff
{
    protected String name;      // name of the worker
    protected double basic;     // basic pay

    Worker(String ns, double bs)
    {
        name = ns;
        basic = bs;
    }

    public void display()
    {
        System.out.println("Name        : " + name);
        System.out.println("Basic pay   : " + basic);
    }
}

// Wages also implements Staff, through Worker
class Wages extends Worker
{
    int hours;                  // hours worked
    double rate;                // rate per hour
    double wage;                // overall wages

    Wages(String ns, double bs, int h, double r)
    {
        super(ns, bs);          // super class members first
        hours = h;
        rate = r;
        wage = 0.0;
    }

    double overtime()
    {
        return hours * rate;
    }

    public void display()
    {
        wage = overtime() + basic;
        super.display();        // name and basic pay
        System.out.println("Hours       : " + hours);
        System.out.println("Rate        : " + rate);
        System.out.println("Overtime    : " + overtime());
        System.out.println("Total wages : " + wage);
    }
}
// END ANSWER
// BEGIN ANSWER
public class Main
{
    public static void main(String args[])
    {
        Staff s1 = new Worker("Ravi Kumar", 15000.0);
        s1.display();
        System.out.println();
        Staff s2 = new Wages("Asha Das", 15000.0, 12, 250.0);
        s2.display();           // dynamic binding: Wages.display() runs
    }
}
// END ANSWER
