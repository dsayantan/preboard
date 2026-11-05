// ANSWER-START
import java.util.Scanner;

class time {
    int hrs, min;                       // hours and minutes

    // constructor: 0 to hrs and min
    time() {
        hrs = 0;
        min = 0;
    }

    // assigns h to hrs and m to min
    void gettime(int h, int m) {
        hrs = h;
        min = m;
    }

    void printTime() {                  // displays hrs and min
        System.out.println(hrs + " hrs " + min + " mins");
    }

    // adds t1 and t2, returns the sum
    time sumtime(time t1, time t2) {
        time t = new time();
        // everything in minutes
        int total = (t1.hrs + t2.hrs) * 60 + t1.min + t2.min;
        t.hrs = total / 60;             // carry whole hours over
        t.min = total % 60;
        return t;
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        time t1 = new time(), t2 = new time(), t3 = new time();
        System.out.print("Enter hours and minutes of Time1: ");
        t1.gettime(sc.nextInt(), sc.nextInt());
        System.out.print("Enter hours and minutes of Time2: ");
        t2.gettime(sc.nextInt(), sc.nextInt());
        t3 = t3.sumtime(t1, t2);
        System.out.print("\nTime1 : "); t1.printTime();
        System.out.print("Time2 : ");   t2.printTime();
        System.out.print("Sum   : ");   t3.printTime();
    }
}
// ANSWER-END
