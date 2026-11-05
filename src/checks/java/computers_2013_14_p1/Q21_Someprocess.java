// ANSWER-START
import java.util.Scanner;
// ANSWER-END

class Q21_Run {
    public static void main(String[] a) {
        someprocess d = new someprocess();
        d.LineDisplay();                          // empty
        // empty -> -999.99
        System.out.println(d.DeleteFront());
        d.InsertRear();   // 2.5
        d.InsertRear();   // 4.0
        // front is at index 0 -> line is full (no room at the front)
        d.InsertFront();
        d.LineDisplay();
        System.out.println("Deleted from front: " + d.DeleteFront());
        d.InsertFront();  // 1.5 goes into the freed slot
        d.LineDisplay();
        System.out.println("Deleted from rear: " + d.DeleteRear());
        System.out.println("Deleted from rear: " + d.DeleteRear());
        System.out.println("IsEmpty = " + d.IsEmpty());
        d.LineDisplay();
    }
}

// ANSWER-START
class someprocess {
    double line[] = new double[100];
    int capacity, front, rear;
    double num;
    static Scanner sc = new Scanner(System.in);

    someprocess() {
        capacity = 100;
        // -1 marks an empty line
        front = rear = -1;
    }

    int IsEmpty() {
        return (front == -1) ? 1 : 0;
    }

    void InsertRear() {
        // no room at the rear end
        if (rear == capacity - 1) {
            System.out.println("line is full");
            return;
        }
        System.out.print("Enter number: ");
        num = sc.nextDouble();
        if (front == -1)                      // first element
            front = 0;
        line[++rear] = num;
    }

    void InsertFront() {
        // no room before the front element
        if (front == 0) {
            System.out.println("line is full");
            return;
        }
        System.out.print("Enter number: ");
        num = sc.nextDouble();
        // empty line: first element
        if (front == -1) {
            front = rear = 0;
            line[0] = num;
        } else
            line[--front] = num;
    }

    double DeleteFront() {
        if (IsEmpty() == 1) {
            System.out.println("line is empty");
            return -999.99;
        }
        num = line[front];
        // last element removed
        if (front == rear)
            front = rear = -1;
        else
            front++;
        return num;
    }

    double DeleteRear() {
        if (IsEmpty() == 1) {
            System.out.println("line is empty");
            return -999.99;
        }
        num = line[rear];
        if (front == rear)
            front = rear = -1;
        else
            rear--;
        return num;
    }

    void LineDisplay() {
        if (IsEmpty() == 1) {
            System.out.println("line is empty");
            return;
        }
        for (int i = front; i <= rear; i++)
            System.out.print(line[i] + "  ");
        System.out.println();
    }
}
// ANSWER-END
