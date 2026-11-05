// ANSWER-START
import java.util.Scanner;
// ANSWER-END

class Q12_Run {
    public static void main(String[] a) {
        Squeue q = new Squeue(4);
        q.insert(10);   // R
        q.insert(20);   // R
        q.insert(5);    // F : shift right, 5 at the front
        q.show();
        System.out.println("delete -> " + q.delete());
        q.insert(1);    // F : slot before front is free, no shift
        q.show();
        q.insert(30);   // R
        q.show();
        q.insert(40);   // R : full -> OVERFLOW
        q.insert(50);   // F : full -> OVERFLOW
        for (int i = 0; i < 5; i++) System.out.println("delete -> " + q.delete());
    }
}

// ANSWER-START
class Squeue {
    int que[] = new int[100];
    // elements are que[front] .. que[rear-1]
    int lim, front, rear;
    static Scanner sc = new Scanner(System.in);

    Squeue(int l) {
        lim = Math.min(l, 100);
        front = rear = 0;
    }

    void insert(int val) {
        System.out.println("Insert " + val + " at Front or Rear (F/R)?");
        char ch = Character.toUpperCase(sc.next().charAt(0));
        if (ch == 'F') {
            // front-most position is empty
            if (front > 0)
                que[--front] = val;
            // no free cell anywhere
            else if (rear == lim)
                System.out.println("OVERFLOW");
            // shift right by one, then insert
            else {
                for (int i = rear; i > front; i--)
                    que[i] = que[i - 1];
                que[front] = val;
                rear++;
            }
        // rear end: as in a normal queue
        } else {
            if (rear == lim)
                System.out.println("OVERFLOW");
            else
                que[rear++] = val;
        }
    }

    int delete() {
        if (front == rear)                       // empty
            return -9999;
        int v = que[front++];
        // became empty: reset
        if (front == rear)
            front = rear = 0;
        return v;
    }
// ANSWER-END

    void show() {
        System.out.print("Queue:");
        for (int i = front; i < rear; i++) System.out.print(" " + que[i]);
        System.out.println();
    }
// ANSWER-START
}
// ANSWER-END
