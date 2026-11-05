public class PipeRun {          // runner only (main need not be written)
    public static void main(String[] args) {
        Pipe p = new Pipe(3);
        p.pushrear(10); p.pushrear(20); p.pushrear(30);
        p.pushrear(40);                         // pipe full
        p.display();
        System.out.println("popfront -> " + p.popfront());
        System.out.println("poprear  -> " + p.poprear());
        p.display();
        System.out.println("poprear  -> " + p.poprear());
        System.out.println("popfront -> " + p.popfront());   // now empty
        p.display();
        p.pushrear(50);
        p.display();
    }
}
// BEGIN ANSWER
class Pipe {
    int item[];     // holds the integers
    int cap;        // maximum capacity
    int front;      // index of the front element (-1 when empty)
    int rear;       // index of the rear element  (-1 when empty)

    Pipe(int max) {
        cap = max;
        front = rear = -1;
        item = new int[cap];
    }

    // add at the rear
    void pushrear(int v) {
        if (rear == cap - 1) {
            System.out.println("Rear full");
            return;
        }
        if (front == -1)        // first element
            front = 0;
        item[++rear] = v;
    }

    // remove from the front; -999 if empty
    int popfront() {
        if (front == -1)
            return -999;
        int v = item[front];
        if (front == rear)      // that was the only element: reset
            front = rear = -1;
        else
            front++;
        return v;
    }

    // remove from the rear; -999 if empty
    int poprear() {
        if (rear == -1)
            return -999;
        int v = item[rear];
        if (front == rear)
            front = rear = -1;
        else
            rear--;
        return v;
    }

    void display() {
        if (front == -1) {
            System.out.println("Pipe is empty");
            return;
        }
        for (int i = front; i <= rear; i++)
            System.out.print(item[i] + " ");
        System.out.println();
    }
}
// END ANSWER
