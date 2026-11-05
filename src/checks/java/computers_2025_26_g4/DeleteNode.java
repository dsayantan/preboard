import java.util.Scanner;

public class DeleteNode
{
    static Scanner sc = new Scanner(System.in);

    static void show(Node p)
    {
        while (p != null) { System.out.print(p.info + " -> "); p = p.link; }
        System.out.println("null");
    }

    static Node make(int... v)
    {
        Node s = null, t = null;
        for (int x : v)
        {
            Node n = new Node(); n.info = x;
            if (s == null) s = n; else t.link = n;
            t = n;
        }
        return s;
    }

    public static void main(String args[])
    {
        DeleteNode ob = new DeleteNode();
        for (int k = 0; k < 4; k++)
        {
            Node start = make(10, 20, 30, 40);
            show(start);
            ob.deleteNode(start);
            show(start);
        }
        Node one = make(10);                    // a one-node list
        show(one);
        ob.deleteNode(one);
    }

// BEGIN ANSWER
void deleteNode(Node start)
{
    System.out.print("Enter the value to be deleted : ");
    int val = sc.nextInt();
    if (start == null)                          // empty list
    {
        System.out.println("List is empty");
        return;
    }
    if (start.info == val)                      // the first node is to go
    {
        if (start.link == null)                 // it is the only node
        {
            System.out.println("List now empty: caller sets start = null");
            return;
        }
        // start cannot be re-pointed from here (Java passes the reference
        // by value), so copy the second node into the first and unlink it
        start.info = start.link.info;
        start.link = start.link.link;
        return;
    }
    Node prev = start, ptr = start.link;    // ptr is one node ahead
    while (ptr != null && ptr.info != val)
    {
        prev = ptr;
        ptr = ptr.link;
    }
    if (ptr == null)
        System.out.println(val + " not found");
    else
        prev.link = ptr.link;               // bypass the node
}
// END ANSWER
}

class Node
{
    int info;
    Node link;
}
