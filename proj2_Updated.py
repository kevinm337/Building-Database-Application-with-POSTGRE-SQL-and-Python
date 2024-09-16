from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import psycopg2


def run_query(query,parameters=()):
    con=psycopg2.connect(
    dbname="studentdb",
    user="postgres",
    password="Messi123!@#",
    host="localhost",
    port="5432")
    cur=con.cursor()
    query_result= None
    try:
        cur.execute(query,parameters)
        if query.lower().startswith("select"):
            query_result=cur.fetchall()
        con.commit()
    except psycopg2.Error as e :
        messagebox.showerror("Database Error",str(e))
    finally:
        cur.close()
        con.close()
    return query_result


def refresh_treeview():
    for item in tree.get_children():
        tree.delete(item) # This means that even if you call this function twice, data will not get repeated
    records=run_query("select * from students;")
    for record in records:
        tree.insert('',END,values=record)


def insert_data():
    query="insert into students(name,address,age,number) values (%s,%s,%s,%s)"
    parameters=(name_entry.get(),address_entry.get(),age_entry.get(),phoneNumber_entry.get())
    run_query(query,parameters)
    messagebox.showinfo("Information","Data inserted successfully")
    refresh_treeview()

def delete_data():
    selected_item=tree.selection()[0]
    student_id=tree.item(selected_item)['values'][0]
    query='delete from students where student_id=%s'
    parameters=(student_id,)
    run_query(query,parameters)
    messagebox.showinfo("Information","Data deleted successfully")
    refresh_treeview()


def update_data():
    selected_item=tree.selection()[0]
    student_id=tree.item(selected_item)['values'][0]
    query="update students set name=%s,address=%s,age=%s,number=%s where student_id=%s"
    parameters=(name_entry.get(),address_entry.get(),age_entry.get(),phoneNumber_entry.get(),student_id)
    run_query(query,parameters)
    messagebox.showinfo("Information","Data updated successfully")
    refresh_treeview()


def create_table():
    query="create table if not exists students(student_id serial primary key, name text, address text, age int, number text);"
    run_query(query)
    messagebox.showinfo("Information","Table created successfully")
    refresh_treeview()



root=Tk()
root.title("Student Management System")

frame=LabelFrame(root, text="Student Data")
frame.grid(row=0,column=0,padx=10,pady=10,sticky="ew")

Label(frame,text="Name: ").grid(row=0,column=0,padx=2,sticky="w")
name_entry=Entry(frame)
name_entry.grid(row=0,column=1,pady=2,sticky="ew")

Label(frame,text="Address: ").grid(row=1,column=0,padx=2,sticky="w")
address_entry=Entry(frame)
address_entry.grid(row=1,column=1,pady=2,sticky="ew")

Label(frame,text="Age: ").grid(row=2,column=0,padx=2,sticky="w")
age_entry=Entry(frame)
age_entry.grid(row=2,column=1,pady=2,sticky="ew")

Label(frame,text="Phone Number: ").grid(row=3,column=0,padx=2,sticky="w")
phoneNumber_entry=Entry(frame)
phoneNumber_entry.grid(row=3,column=1,pady=2,sticky="ew")

button_frame=Frame(root)
button_frame.grid(row=1,column=0,pady=5,sticky="ew")

Button(button_frame,text="Create Table",command=create_table).grid(row=0,column=0,padx=5)
Button(button_frame,text="Add Data",command=insert_data).grid(row=0,column=1,padx=5)
Button(button_frame,text="Update Data",command=update_data).grid(row=0,column=2,padx=5)
Button(button_frame,text="Delete Data",command=delete_data).grid(row=0,column=3,padx=5)


tree_frame=Frame(root)
tree_frame.grid(row=2,column=0,padx=10,sticky='nsew')

tree_scroll=Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)

tree=ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,selectmode="browse")
tree.pack()
tree_scroll.config(command=tree.yview)

tree['columns']=('student_id','name','address','age','number')
tree.column("#0",width=0,stretch=NO)
tree.column("student_id",anchor=CENTER,width=80)
tree.column("name",anchor=CENTER,width=120)
tree.column("address",anchor=CENTER,width=120)
tree.column("age",anchor=CENTER,width=50)
tree.column("number",anchor=CENTER,width=120)

tree.heading("student_id",text="ID",anchor=CENTER)
tree.heading("name",text="name",anchor=CENTER)
tree.heading("address",text="address",anchor=CENTER)
tree.heading("age",text="age",anchor=CENTER)
tree.heading("number",text="phone number",anchor=CENTER)


refresh_treeview()

root.mainloop()