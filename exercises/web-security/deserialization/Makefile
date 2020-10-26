.PHONY: all run clean

all: Eve.java Employee.java Payroll.java Database.java
	javac Eve.java Employee.java Payroll.java Database.java

database: Employee.java Database.java
	javac Employee.java Database.java 

employee: Employee.java
	javac Employee.java

eve: Eve.java
	javac Eve.java  

payroll: Eve.java Employee.java Payroll.java
	javac Eve.java Employee.java Payroll.java

clean:
	rm -f *.class *.ser
