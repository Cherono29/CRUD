import sqlite3

conn = sqlite3.connect('company.db')
print("Connected")

conn.execute("INSERT INTO Company1(ID, FIRSTNAME, LASTNAME, AGE,SALARY,TASK) \
            VALUES (1,'Andrew','Kaguai',20,70000.40,'Manager')");
conn.execute("INSERT INTO Company1(ID, FIRSTNAME, LASTNAME, AGE,SALARY,TASK) \
            VALUES (2,'Sophia','Gabriel',19,25000.40,'Secretary')");
conn.execute("INSERT INTO Company1(ID, FIRSTNAME, LASTNAME, AGE,SALARY,TASK) \
            VALUES (3,'Sam','Bett',23,40000.20,'Client')");
conn.execute("INSERT INTO Company1(ID, FIRSTNAME, LASTNAME, AGE,SALARY,TASK) \
             VALUES (4,'Leone','Maina',27,50000.40,'Trainer')");

conn.commit();
print("Successfully inserted values in Company1 table");

conn.close()

