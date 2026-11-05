// BEGIN ANSWER
import java.util.Scanner;

/* Prints the calendar of any month of 2015, given that 1 January 2015 was a
 * Thursday.  Day numbers: 0 = Sunday, 1 = Monday, ... 6 = Saturday.
 * As in the paper's samples, cells before day 1 are left blank and the
 * cells after the last day, up to Saturday, are filled with '*'.          */
class Calendar2015 {
    String names[] = {"JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY",
                      "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"};
    int days[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};   // 2015 is not a leap year
    String head[] = {"Sun", "Mon", "Tues", "Wed", "Thrus", "Fri", "Sat"};  // as printed
    int month;      // 0 .. 11, or -1 if the name is not a month

    // finds the month number from its name (case ignored)
    void setMonth(String s) {
        month = -1;
        for (int i = 0; i < 12; i++)
            if (names[i].equalsIgnoreCase(s.trim()))
                month = i;
    }

    // weekday of the 1st of the month: Thursday (4) plus all the days before it, mod 7
    int firstDay() {
        int total = 0;
        for (int i = 0; i < month; i++)
            total += days[i];
        return (4 + total) % 7;
    }

    void print() {
        if (month == -1) {
            System.out.println("INVALID MONTH NAME");
            return;
        }
        int start = firstDay();
        for (int i = 0; i < 7; i++)
            System.out.print(String.format("%-7s", head[i]));
        System.out.println();
        int col = 0;
        for (int i = 0; i < start; i++) {          // blanks before the 1st
            System.out.print(String.format("%-7s", ""));
            col++;
        }
        for (int d = 1; d <= days[month]; d++) {
            System.out.print(String.format("%-7d", d));
            col++;
            if (col == 7) {                         // Saturday done: new line
                System.out.println();
                col = 0;
            }
        }
        if (col != 0) {                             // fill the last week with '*'
            while (col < 7) {
                System.out.print(String.format("%-7s", "*"));
                col++;
            }
            System.out.println();
        }
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the name of a month of 2015:");
        Calendar2015 ob = new Calendar2015();
        ob.setMonth(sc.nextLine());
        ob.print();
    }
}
// END ANSWER
