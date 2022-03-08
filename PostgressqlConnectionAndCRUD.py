import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="rekhu", host="127.0.0.1", port="5432")
print("Database opened successfully")

cur = con.cursor()

#''' Data Create
cur.execute("INSERT INTO appointments (patient_id,patient_name,patient_fathername,patient_place,patient_phonenumber,patient_appointment_date,patient_appointment_fees,patient_appointment_doctor) VALUES (3419, 'Abel', 'Naresh', 'Bangalore', '345345445','2016-06-22 19:10:25-07','500','Dr.Vikram Prasad')");

con.commit()
print("Records inserted successfully")
con.close()
#'''

''' Data Read
cur.execute("SELECT * from appointments")
rows = cur.fetchall()

for row in rows:
    print("patient_id =", row[0])
    print("patient_name =", row[1])
    print("patient_fathername =", row[2])
    print("patient_place =", row[3])
    print("patient_phonenumber =", row[4]), 
    print("patient_appointment_date =", row[5]),
    print("patient_appointment_fees =", row[6]),
    print("patient_appointment_doctor =", row[7], "\n")

print("Record Retrieved successfully")
con.close()
'''

''' Data Update
cur.execute("UPDATE appointments set patient_name = 'TestPatient' where patient_id = 3419")
con.commit()
print("Total updated rows:", cur.rowcount)

cur.execute("SELECT * from appointments")
rows = cur.fetchall()

for row in rows:
    print("patient_id =", row[0])
    print("patient_name =", row[1])
    print("patient_fathername =", row[2])
    print("patient_place =", row[3])
    print("patient_phonenumber =", row[4]), 
    print("patient_appointment_date =", row[5]),
    print("patient_appointment_fees =", row[6]),
    print("patient_appointment_doctor =", row[7], "\n")

print("Operation done successfully")
con.close()
'''

''' Data Delete
cur.execute("DELETE from appointments where patient_id=3419")
con.commit()
print("Total deleted rows:", cur.rowcount)

cur.execute("SELECT * from appointments")
rows = cur.fetchall()
for row in rows:
    print("patient_id =", row[0])
    print("patient_name =", row[1])
    print("patient_fathername =", row[2])
    print("patient_place =", row[3])
    print("patient_phonenumber =", row[4]), 
    print("patient_appointment_date =", row[5]),
    print("patient_appointment_fees =", row[6]),
    print("patient_appointment_doctor =", row[7], "\n")

print("Deletion successful")
con.close()
'''