import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

# for window 
root = Tk()
root.geometry("900x600")
global e1
global e2
global e3
global e4


# For Label
tk.Label(root, text="Employee Registation", fg="blue", font=(None, 30)).place(x=300, y=5)

tk.Label(root, text="Employee ID").place(x=10, y=10)
Label(root, text="Employee Name").place(x=10, y=40)
Label(root, text="Mobile").place(x=10, y=70)
Label(root, text="Salary").place(x=10, y=100)


# to place
e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=70)

e4 = Entry(root)
e4.place(x=140, y=100)

# for button

Button(root, text="Add",command = Add,height=3, width= 13).place(x=30, y=130)
Button(root, text="update",command = update,height=3, width= 13).place(x=140, y=130)
Button(root, text="Delete",command = delete,height=3, width= 13).place(x=250, y=130)


# for 4 col
cols = ('id', 'empname', 'mobile','salary')
listBox = ttk.Treeview(root, columns=cols, show='headings' )


# to display data in that 4 col
for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)







# db conn with exception

mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="payroll")
    mycursor=mysqldb.cursor()

    try:
       sql = "INSERT INTO  registation (id,empname,mobile,salary) VALUES (%s, %s, %s, %s)"
       val = (studid,studname,coursename,feee)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Employee inserted successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()


# to add
def Add():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()


# to update - with conn and exception

def update():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="payroll")
    mycursor=mysqldb.cursor()

    try:
       sql = "Update  registation set empname= %s,mobile= %s,salary= %s where id= %s"
       val = (studname,coursename,feee,studid)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Updateddddd successfully...")

       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()

    except Exception as e:

       print(e)
       mysqldb.rollback()
       mysqldb.close()



# to enable double click 
show()
listBox.bind('<Double-Button-1>',GetValue)

# get value fn for double click 
def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['id'])
    e2.insert(0,select['empname'])
    e3.insert(0,select['mobile'])
    e4.insert(0,select['salary'])



# to show the data for double click 

def show():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="payroll")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT id,empname,mobile,salary FROM registation")
        records = mycursor.fetchall()
        print(records)

        for i, (id,stname, course,fee) in enumerate(records, start=1):
            listBox.insert("", "end", values=(id, stname, course, fee))
            mysqldb.close()



# to delete data

def delete():
    studid = e1.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="payroll")
    mycursor=mysqldb.cursor()

    try:
       sql = "delete from registation where id = %s"
       val = (studid,)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Deleteeeee successfully...")

       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()

    except Exception as e:

       print(e)
       mysqldb.rollback()
       mysqldb.close()




root.mainloop()
