// Q9: deleting the first (start) node through void deleteNode(Node first)
public class DeleteNode
{
    static void print(Node p)
    {
        StringBuilder sb = new StringBuilder();
        for (; p != null; p = p.link) sb.append(p.str).append(" -> ");
        System.out.println(sb.append("null"));
    }

    static Node build(String... v)
    {
        Node start = null, last = null;
        for (String s : v)
        {
            Node n = new Node(s);
            if (start == null) start = n; else last.link = n;
            last = n;
        }
        return start;
    }

    public static void main(String[] a)
    {
        DeleteNode d = new DeleteNode();
        Node start = build("Red", "Green", "Blue", "Pink");
        print(start);
        d.deleteNode(start);
        print(start);
        d.deleteNode(start);
        print(start);
        Node one = build("Solo");
        d.deleteNode(one);
        d.deleteNode(null);
    }

// BEGIN ANSWER
void deleteNode(Node first)
{
    if (first == null)                  // nothing to delete
    {
        System.out.println("List is empty");
        return;
    }
    if (first.link == null)             // only one node in the list:
    {                                   // clear it; the caller must
        first.str = null;               // then set start = null
        System.out.println("Only node removed: set start = null");
        return;
    }
    Node second = first.link;           // the node after the start node
    first.str = second.str;             // copy its data into the start
    first.link = second.link;           // and bypass the second node
    second.link = null;                 // detach the removed node
}
// END ANSWER
}

class Node
{
    String str;
    Node link;
    Node(String s) { str = s; link = null; }
}

