import java.io.*;

public class Database {

    public static void main(String[] args) {

        try {

            if (args.length < 1) {
                System.err.println("Abort: Missing path to serialized employee file");
                System.exit(1);
            }

            // Deserialization
            FileInputStream file = new FileInputStream(args[0]);
            ObjectInputStream in = new ObjectInputStream(file);
            Employee employee = (Employee)in.readObject(); /* This is the vulnerability point */
            in.close();
            file.close();
            System.out.println(employee.toString());

            // todo: Put in payroll database

        } catch (Exception ex) {
            ex.printStackTrace();
            System.exit(1);
        }
    }
}
