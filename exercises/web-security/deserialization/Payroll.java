import java.io.*;
import java.util.*;

public class Payroll {

    public static void serialize(Object employee, String path) throws IOException {
        FileOutputStream file = new FileOutputStream(path);
        ObjectOutputStream out = new ObjectOutputStream(file);
        out.writeObject(employee);
        out.close();
        file.close();
    }

    public static void main(String[] args) {
        try {

            serialize(new Employee("Alice", 40), "alice.ser");

            // serialize(new Employee("Bob", 13), "bob.ser");

            // serialize(new String("Hey there!"), "string.ser");

            // serialize(Eve.getDos(), "dos.ser");

        } catch (ClassCastException ex) {
            ex.printStackTrace();
        } catch (IOException ex) {
            ex.printStackTrace();
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}
