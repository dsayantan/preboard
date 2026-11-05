// Runner first: the single-file launcher takes main from the first class.
public class Volume_Run
{
    public static void main(String args[])
    {
        Volume v = new Volume(7.0, 10.0);
        v.display();
    }
}

class Circle                        // super class (given; need not be written)
{
    double radius, area;
    Circle(double r)
    {
        radius = r;
        area = 0.0;
    }
    void cal_area()
    {
        area = Math.PI * radius * radius;
    }
    void display()
    {
        System.out.println("Area of the circle = " + area);
    }
}

// BEGIN ANSWER
class Volume extends Circle
{
    double height;                  // height of the cylinder
    double volume;                  // volume of the cylinder

    Volume(double r, double h)
    {
        super(r);                   // assigns radius in Circle
        height = h;
        volume = 0.0;
    }

    double calculate()
    {
        volume = Math.PI * radius * radius * height;     // V = pi r^2 h
        return volume;
    }

    void display()
    {
        cal_area();                 // compute the inherited area first
        super.display();            // prints the area of the circle
        System.out.println("Volume of the cylinder = " + calculate());
    }
}
// END ANSWER
