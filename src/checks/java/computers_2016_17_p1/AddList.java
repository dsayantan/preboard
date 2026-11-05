public class AddList {          // runner only
    public static void main(String[] args) {
        float v[] = {2.5f, 4.0f, 1.25f, 3.75f};
        ListNode head = null;
        for (int i = v.length - 1; i >= 0; i--) {
            ListNode t = new ListNode();
            t.data = v[i]; t.ptr = head; head = t;
        }
        System.out.println("Sum = " + new Lists().addList(head));
        System.out.println("Sum of empty list = " + new Lists().addList(null));
    }
}
class ListNode {
    float data;
    ListNode ptr;
}
class Lists {
// BEGIN ANSWER
    float addList(ListNode head) {
        float sum = 0.0f;
        ListNode temp = head;          // start at the first node
        while (temp != null) {         // until the end of the list
            sum = sum + temp.data;     // add this node's data
            temp = temp.ptr;           // move to the next node
        }
        return sum;
    }
// END ANSWER
}
