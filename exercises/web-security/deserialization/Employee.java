import java.io.*;

class Employee implements Serializable {

    private String id;
    private int numHoursWorked;

    public Employee(String id, int numHoursWorked) {
        this.id = id;
        this.numHoursWorked = numHoursWorked;
    }

    public String toString() {
        return id + " worked " + numHoursWorked + " hours";
    }

    // This methods always gets called during deserialization
    private void readObject(ObjectInputStream in) throws IOException, ClassNotFoundException {
        System.out.println("*** Employee::readObj(): ***");
        in.defaultReadObject();
    }
}
