public class Repeat
{
    int st[];
    int cap, f, r;

    Repeat(int m)
    {
        cap = m;
        f = 0;
        r = -1;
        st = new int[100];          // holds at most 100; cap of them are used
    }

// BEGIN ANSWER
void pushValue(int v)
{
    if (r == cap - 1)                       // rear has reached the last cell
        System.out.println("Overflow! Insertion not possible.");
    else
    {
        r = r + 1;                          // move rear forward
        st[r] = v;                          // insert at the rear
    }
}

int popValue()
{
    if (f > r)                              // no element between front and rear
    {
        System.out.println("Underflow! Deletion not possible.");
        return -9999;
    }
    int v = st[f];                          // element at the front
    f = f + 1;                              // move front forward
    if (f > r)                              // queue became empty: reset
    {
        f = 0;
        r = -1;
    }
    return v;
}
// END ANSWER

    void disp()
    {
        if (f > r)
            System.out.println("Queue empty");
        else
        {
            for (int i = f; i <= r; i++)
                System.out.print(st[i] + " ");
            System.out.println();
        }
    }

    public static void main(String args[])
    {
        Repeat q = new Repeat(3);
        q.pushValue(10); q.pushValue(20); q.pushValue(30);
        q.disp();
        q.pushValue(40);
        System.out.println("popped " + q.popValue());
        q.disp();
        System.out.println("popped " + q.popValue());
        System.out.println("popped " + q.popValue());
        System.out.println("popped " + q.popValue());
        q.pushValue(50);
        q.disp();
    }
}
