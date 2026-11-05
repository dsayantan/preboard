class Q11_Run {
    public static void main(String[] a) {
        new Student("Ujaan", 12).show();
    }
}

// ANSWER-START
class Person {
    protected String name;
    Person(String name) {
        // 'this' separates the field from the parameter
        this.name = name;
    }
    void show() {
        System.out.println("Name : " + name);
    }
}

class Student extends Person {
    int roll;
    Student(String name, int roll) {
        // calls the superclass constructor (must be first)
        super(name);
        // this.roll is the field, roll the parameter
        this.roll = roll;
    }
    void show() {                  // overrides Person.show()
        // calls the overridden superclass version
        super.show();
        System.out.println("Roll : " + this.roll);
    }
}
// ANSWER-END

