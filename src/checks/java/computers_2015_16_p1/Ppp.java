// Runner: the launcher takes main() from the FIRST class, so it comes first.
public class Ppp {
    public static void main(String[] args) {
        Perm.ppp("", "ABCd");
    }
}
// BEGIN ANSWER
class Perm {
    // As printed, except the recursive call (printed as permute) is made to ppp itself
    public static void ppp(String begstr, String endstr) {
        if (endstr.length() <= 2) {
            System.out.println(begstr + endstr);
        } else {
            for (int i = 0; i < endstr.length(); i++) {
                String newendstr = endstr.substring(i + 1) + endstr.substring(0, i);
                String newbegstr = endstr.charAt(i) + begstr;
                ppp(newbegstr, newendstr);
            }
        }
    }
}
// END ANSWER
