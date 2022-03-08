from tkinter import ttk

import tkinter as tk

import psycopg2

def connect():

    con = psycopg2.connect(database="postgres", user="postgres", password="rekhu", host="127.0.0.1", port="5432")

    cur = con.cursor()

    cur.execute("SELECT * from appointments")

    con.commit()

    cur.close()


def View():

    con = psycopg2.connect(database="postgres", user="postgres", password="rekhu", host="127.0.0.1", port="5432")

    cur = con.cursor()

    cur.execute("SELECT * FROM appointments")

    rows = cur.fetchall()    

    for row in rows:

        print(row) 

        tree.insert("", tk.END, values=row)        

    cur.close()


# connect to the database

#connect() 

root = tk.Tk()

tree = ttk.Treeview(root, column=("c1", "c2", "c3","c4", "c5", "c6","c7", "c8"), show='headings')

tree.column("#1", anchor=tk.CENTER)

tree.heading("#1", text="patient_id")

tree.column("#2", anchor=tk.CENTER)

tree.heading("#2", text="patient_name")

tree.column("#3", anchor=tk.CENTER)

tree.heading("#3", text="patient_fathername")
tree.column("#4", anchor=tk.CENTER)

tree.heading("#4", text="patient_place")
tree.column("#5", anchor=tk.CENTER)

tree.heading("#5", text="patient_phonenumber")
tree.column("#6", anchor=tk.CENTER)

tree.heading("#6", text="patient_appointment_date")
tree.column("#7", anchor=tk.CENTER)

tree.heading("#7", text="patient_appointment_fees")
tree.column("#8", anchor=tk.CENTER)

tree.heading("#8", text="patient_appointment_doctor")

tree.pack()

button1 = tk.Button(text="Get Data", command=View)

button1.pack(pady=10)

root.mainloop()