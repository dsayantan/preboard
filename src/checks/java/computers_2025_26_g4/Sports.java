// BEGIN ANSWER
import java.util.Scanner;

public class Sports
{
    double height[];        // height of each player
    String name;            // name of the team
    int n;                  // number of players (at most 15)
    static Scanner sc = new Scanner(System.in);

    Sports()                // default constructor
    {
        n = 0;
        name = "";
        height = new double[15];
    }

    Sports(int n, String name)
    {
        if (n < 1 || n > 15)      // at most fifteen players
            n = 15;
        this.n = n;
        this.name = name;
        height = new double[n];
    }

    void fillHeight()
    {
        System.out.println("Enter the heights of the " + n
                           + " players of " + name);
        for (int i = 0; i < n; i++)
            height[i] = sc.nextDouble();
    }

    double averageHeight()
    {
        double sum = 0;
        for (int i = 0; i < n; i++)
            sum += height[i];
        return sum / n;
    }

    // name of the team with the higher average, or the "same" message
    String compare(Sports s1, Sports s2)
    {
        double a1 = s1.averageHeight(), a2 = s2.averageHeight();
        if (a1 > a2)
            return s1.name;
        else if (a2 > a1)
            return s2.name;
        else
            return "Both teams have the same average height.";
    }

    void display(String msg)
    {
        if (msg.equals("Both teams have the same average height."))
            System.out.println(msg);
        else
            System.out.println("Team with the higher average height : "
                               + msg);
    }

    public static void main(String args[])
    {
        System.out.println("Team 1 - enter name and number of players :");
        String t1 = sc.next();
        int n1 = sc.nextInt();
        System.out.println("Team 2 - enter name and number of players :");
        String t2 = sc.next();
        int n2 = sc.nextInt();
        Sports a = new Sports(n1, t1);
        Sports b = new Sports(n2, t2);
        a.fillHeight();
        b.fillHeight();
        Sports ob = new Sports();
        String msg = ob.compare(a, b);
        ob.display(msg);
    }
}
// END ANSWER
