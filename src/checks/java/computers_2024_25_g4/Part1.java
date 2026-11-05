// Part I checks: Q1(vii) trick(3,4) and Q2(iv) the completed string-to-integer program
public class Part1 {
    static void trick(int a, int b)
    {
        int p = 1;
        for (int j = 1; j <= b; j++, p *= a)
            System.out.println(p);
    }

    public static void main(String[] args) {
        System.out.println("Q1vii trick(3,4) prints:");
        trick(3, 4);
        System.out.print("Q2iv ");
        preboard.main(args);
        System.out.println();
        System.out.println("Q2iv Inte(\"7\") = " + preboard.Inte("7") + ", Inte(\"40096\") = " + preboard.Inte("40096"));
    }
}

// BEGIN ANSWER
public class preboard {
    static int Inte(String str)
    {
        if (str.length() == 1)                       // ?1?
            return (str.charAt(0) - '0');            // ?2?
        double y = Inte(str.substring(1));           // value of the tail
        double x = str.charAt(0) - '0';              // ?3?
        x = x * Math.pow(10, str.length() - 1) + y;  // ?4?
        return (int)(x);
    }
    public static void main(String[] args)
    {
        String str = "1235";
        System.out.print(Inte(str));                 // ?5?
    }
}
// END ANSWER
