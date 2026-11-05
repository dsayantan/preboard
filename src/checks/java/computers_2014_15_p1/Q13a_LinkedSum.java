class Q13a_Run {
    public static void main(String[] a) {
        Node head = null;
        int[] v = {4, 25, 7, 12};
        for (int x : v) { Node n = new Node(); n.item = x; n.ptr = head; head = n; }
        System.out.println("sum = " + new LinkedOps().sum(head));
        System.out.println("sum(empty) = " + new LinkedOps().sum(null));
    }
}

class Node {
    int item;
    Node ptr;
}

class LinkedOps {
// ANSWER-START
    int sum(Node ptr_start) {
        int s = 0;
        Node temp = ptr_start;          // start at the first node
        // until the end of the list
        while (temp != null) {
            s = s + temp.item;          // add this node's value
            temp = temp.ptr;            // move to the next node
        }
        return s;
    }
// ANSWER-END
}
