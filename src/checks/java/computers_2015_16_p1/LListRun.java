public class LListRun {         // runner only: builds 22 -> 33 -> 44 -> 55 -> 66
    public static void main(String[] args) {
        LList L = new LList();
        int v[] = {22, 33, 44, 55, 66};
        Node last = null;
        for (int x : v) {
            Node t = new Node(x);
            if (L.Start == null) L.Start = t; else last.link = t;
            last = t;
        }
        L.Displayfront_from_pos(3);
        L.Displayback_from_pos(3);
        L.Displayfront_from_pos(1);
        L.Displayback_from_pos(5);
        L.Displayfront_from_pos(7);
    }
}
// BEGIN ANSWER
class Node {
    int data;       // the one data field
    Node link;      // the one link: reference to the next node

    Node(int d) {
        data = d;
        link = null;
    }
}

class LList {
    Node Start;     // first node of the list (the list already exists)

    // displays the nodes from position pos (1-based) to the end
    void Displayfront_from_pos(int pos) {
        Node p = Start;
        int i = 1;
        while (p != null && i < pos) {   // walk to the pos-th node
            p = p.link;
            i++;
        }
        if (p == null || pos < 1) {
            System.out.println("Invalid position");
            return;
        }
        String s = "";
        while (p != null) {               // print it and every node after it
            s = s + p.data + (p.link != null ? "," : "");
            p = p.link;
        }
        System.out.println(s);
    }

    // displays the nodes from position pos back to the first node.
    // The links only go forward, so the nodes are collected in order and
    // printed in reverse (each new value is put in FRONT of the string).
    void Displayback_from_pos(int pos) {
        Node p = Start;
        int i = 1;
        String s = "";
        while (p != null && i <= pos) {
            s = (i == 1) ? "" + p.data : p.data + "," + s;
            p = p.link;
            i++;
        }
        if (i <= pos || pos < 1) {        // list ended before reaching pos
            System.out.println("Invalid position");
            return;
        }
        System.out.println(s);
    }
}
// END ANSWER
