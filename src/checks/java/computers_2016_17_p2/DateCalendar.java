// BEGIN ANSWER
import java.util.Scanner;

/* Reads two dates (dd/mm/yyyy) and the weekday of the 1st of each date's month,
 * prints the number of days from the start date (counted) to the end date
 * (not counted) and the calendar of both months.                            */
class DateCalendar {
    int mdays[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    String mname[] = {"", "January", "February", "March", "April", "May", "June", "July",
                      "August", "September", "October", "November", "December"};
    String wk[] = {"SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"};

    boolean isLeap(int y) {
        return (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0);
    }

    int daysIn(int m, int y) {
        return (m == 2 && isLeap(y)) ? 29 : mdays[m];
    }

    // splits "dd/mm/yyyy" into {d, m, y}; returns null if it is not a valid date
    int[] parse(String s) {
        String p[] = s.trim().split("/");
        if (p.length != 3)
            return null;
        int d, m, y;
        try {
            d = Integer.parseInt(p[0].trim());
            m = Integer.parseInt(p[1].trim());
            y = Integer.parseInt(p[2].trim());
        } catch (NumberFormatException e) {
            return null;
        }
        if (y < 1 || m < 1 || m > 12 || d < 1 || d > daysIn(m, y))
            return null;
        return new int[]{d, m, y};
    }

    // number of days from 1/1/0001 up to and including the given date
    long serial(int d, int m, int y) {
        long n = 0;
        for (int yr = 1; yr < y; yr++)
            n += isLeap(yr) ? 366 : 365;
        for (int mo = 1; mo < m; mo++)
            n += daysIn(mo, y);
        return n + d;
    }

    // weekday name -> 0 (Sunday) .. 6 (Saturday); -1 if not a weekday
    int dayNo(String s) {
        for (int i = 0; i < 7; i++)
            if (wk[i].equalsIgnoreCase(s.trim()))
                return i;
        return -1;
    }

    void line() {
        System.out.println("-----------------------------------");
    }

    // calendar of month m of year y whose 1st falls on weekday f
    void calendar(int m, int y, int f) {
        line();
        System.out.println("           " + mname[m] + " " + y);
        line();
        System.out.println("SUN  MON  TUE  WED  THU  FRI  SAT");
        line();
        int col = 0;
        for (int i = 0; i < f; i++) {          // blank cells before the 1st
            System.out.print("     ");
            col++;
        }
        for (int d = 1; d <= daysIn(m, y); d++) {
            System.out.print(String.format("%-5d", d));
            if (++col == 7) {                  // end of a week
                System.out.println();
                line();
                col = 0;
            }
        }
        if (col != 0) {
            System.out.println();
            line();
        }
        System.out.println();
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        DateCalendar ob = new DateCalendar();
        System.out.println("Start Date (dd/mm/yyyy):");
        int s[] = ob.parse(sc.nextLine());
        System.out.println("End Date (dd/mm/yyyy):");
        int e[] = ob.parse(sc.nextLine());
        if (s == null || e == null) {
            System.out.println("INVALID DATE");
            return;
        }
        long diff = ob.serial(e[0], e[1], e[2]) - ob.serial(s[0], s[1], s[2]);
        if (diff <= 0) {
            System.out.println("INVALID INPUT: end date must be after the start date");
            return;
        }
        boolean same = (s[1] == e[1] && s[2] == e[2]);     // both dates in one month
        System.out.println("1st day of " + ob.mname[s[1]] + ":");
        int f1 = ob.dayNo(sc.nextLine());
        int f2 = f1;
        if (!same) {
            System.out.println("1st day of " + ob.mname[e[1]] + ":");
            f2 = ob.dayNo(sc.nextLine());
        }
        if (f1 < 0 || f2 < 0) {
            System.out.println("INVALID WEEKDAY");
            return;
        }
        System.out.println("No of days between start date and end date: " + diff + " days");
        ob.calendar(s[1], s[2], f1);
        if (!same)
            ob.calendar(e[1], e[2], f2);
    }
}
// END ANSWER
