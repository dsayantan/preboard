// BEGIN ANSWER
import java.util.Scanner;
// END ANSWER
public class AngleRun {         // runner only (main need not be written)
    public static void main(String[] args) {
        Angle a = new Angle(), b = new Angle(), c = new Angle();
        a.inputAngle();
        b.inputAngle();
        Angle s = c.sumAngle(a, b);
        s.dispAngle();
    }
}
// BEGIN ANSWER
class Angle {
    int deg;        // degrees
    int min;        // minutes (0 to 59)
    static Scanner sc = new Scanner(System.in);

    Angle() {
        deg = 0;
        min = 0;
    }

    void inputAngle() {
        System.out.println("Degrees: ");
        deg = sc.nextInt();
        System.out.println("Minutes: ");
        min = sc.nextInt();
    }

    void dispAngle() {
        System.out.println("Angle = " + deg + " degrees " + min + " minutes");
    }

    // returns A + B: add the minutes, carry every 60 minutes into a degree
    Angle sumAngle(Angle A, Angle B) {
        Angle S = new Angle();
        int m = A.min + B.min;
        S.min = m % 60;                    // minutes left over
        S.deg = A.deg + B.deg + m / 60;    // whole degrees plus the carry
        return S;
    }
}
// END ANSWER
