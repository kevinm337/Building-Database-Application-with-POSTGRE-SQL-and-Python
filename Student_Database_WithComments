from tkinter import *  # Import all classes and functions from the tkinter module for GUI
from tkinter import ttk  # Import the themed tkinter widgets
from tkinter import messagebox  # Import messagebox for showing error/info dialogs
import psycopg2  # Import psycopg2 to interact with a PostgreSQL database

# Function to execute SQL queries
def run_query(query, parameters=()):
    # Connect to PostgreSQL database
    con = psycopg2.connect(
        dbname="studentdb",  # Database name
        user="postgres",  # Database user
        password="Messi123!@#",  # Database password
        host="localhost",  # Host where the database is running
        port="5432"  # Port number for PostgreSQL
    )
    
    cur = con.cursor()  # Create a cursor object to execute queries
    query_result = None  # Initialize variable to store query results
    try:
        cur.execute(query, parameters)  # Execute the query with parameters
        if query.lower().startswith("select"):  # Check if it's a SELECT query
            query_result = cur.fetchall()  # Fetch all results for SELECT queries
        con.commit()  # Commit the transaction to the database
    except psycopg2.Error as e:  # Handle any database errors
        messagebox.showerror("Database Error", str(e))  # Display error message
    finally:
        cur.close()  # Close the cursor
        con.close()  # Close the database connection
    return query_result  # Return the query result if applicable

# Function to refresh the data in the Treeview widget
def refresh_treeview():
    for item in tree.get_children():  # Loop through each item in the Treeview
        tree.delete(item)  # Delete all current items to avoid repetition
    records = run_query("select * from students;")  # Query to fetch all records from the 'students' table
    for record in records:  # Loop through each record
        tree.insert('', END, values=record)  # Insert each record into the Treeview

# Function to insert new data into the database
def insert_data():
    query = "insert into students(name, address, age, number) values (%s, %s, %s, %s)"  # SQL query to insert data
    parameters = (name_entry.get(), address_entry.get(), age_entry.get(), phoneNumber_entry.get())  # Get input values
    run_query(query, parameters)  # Execute the query with parameters
    messagebox.showinfo("Information", "Data inserted successfully")  # Show success message
    refresh_treeview()  # Refresh the Treeview to display new data

# Function to delete data from the database
def delete_data():
    selected_item = tree.selection()[0]  # Get the selected item from the Treeview
    student_id = tree.item(selected_item)['values'][0]  # Get the student_id of the selected item
    query = 'delete from students where student_id=%s'  # SQL query to delete data
    parameters = (student_id,)  # Parameter for the query
    run_query(query, parameters)  # Execute the delete query
    messagebox.showinfo("Information", "Data deleted successfully")  # Show success message
    refresh_treeview()  # Refresh the Treeview to remove the deleted item

# Function to update data in the database
def update_data():
    selected_item = tree.selection()[0]  # Get the selected item from the Treeview
    student_id = tree.item(selected_item)['values'][0]  # Get the student_id of the selected item
    query = "update students set name=%s, address=%s, age=%s, number=%s where student_id=%s"  # SQL query to update data
    parameters = (name_entry.get(), address_entry.get(), age_entry.get(), phoneNumber_entry.get(), student_id)  # Parameters
    run_query(query, parameters)  # Execute the update query
    messagebox.showinfo("Information", "Data updated successfully")  # Show success message
    refresh_treeview()  # Refresh the Treeview to display updated data

# Function to create the 'students' table if it doesn't exist
def create_table():
    query = "create table if not exists students(student_id serial primary key, name text, address text, age int, number text);"  # SQL query to create the table
    run_query(query)  # Execute the query
    messagebox.showinfo("Information", "Table created successfully")  # Show success message
    refresh_treeview()  # Refresh the Treeview after creating the table

# Create the main window for the GUI
root = Tk()
root.title("Student Management System")  # Set the window title

# Create a LabelFrame to hold the input fields for student data
frame = LabelFrame(root, text="Student Data")
frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")  # Position the frame

# Create and position input fields and labels for student information
Label(frame, text="Name: ").grid(row=0, column=0, padx=2, sticky="w")
name_entry = Entry(frame)
name_entry.grid(row=0, column=1, pady=2, sticky="ew")

Label(frame, text="Address: ").grid(row=1, column=0, padx=2, sticky="w")
address_entry = Entry(frame)
address_entry.grid(row=1, column=1, pady=2, sticky="ew")

Label(frame, text="Age: ").grid(row=2, column=0, padx=2, sticky="w")
age_entry = Entry(frame)
age_entry.grid(row=2, column=1, pady=2, sticky="ew")

Label(frame, text="Phone Number: ").grid(row=3, column=0, padx=2, sticky="w")
phoneNumber_entry = Entry(frame)
phoneNumber_entry.grid(row=3, column=1, pady=2, sticky="ew")

# Create a button frame to hold action buttons
button_frame = Frame(root)
button_frame.grid(row=1, column=0, pady=5, sticky="ew")

# Create and position buttons for different actions (Create, Add, Update, Delete)
Button(button_frame, text="Create Table", command=create_table).grid(row=0, column=0, padx=5)
Button(button_frame, text="Add Data", command=insert_data).grid(row=0, column=1, padx=5)
Button(button_frame, text="Update Data", command=update_data).grid(row=0, column=2, padx=5)
Button(button_frame, text="Delete Data", command=delete_data).grid(row=0, column=3, padx=5)

# Create a frame to hold the Treeview widget for displaying data
tree_frame = Frame(root)
tree_frame.grid(row=2, column=0, padx=10, sticky='nsew')

# Add a vertical scrollbar to the Treeview
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create and configure the Treeview widget to display student data
tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse")
tree.pack()
tree_scroll.config(command=tree.yview)  # Connect the scrollbar to the Treeview

# Define columns for the Treeview widget
tree['columns'] = ('student_id', 'name', 'address', 'age', 'number')
tree.column("#0", width=0, stretch=NO)  # Hide the default first column
tree.column("student_id", anchor=CENTER, width=80)
tree.column("name", anchor=CENTER, width=120)
tree.column("address", anchor=CENTER, width=120)
tree.column("age", anchor=CENTER, width=50)
tree.column("number", anchor=CENTER, width=120)

# Define headings for each column in the Treeview widget
tree.heading("student_id", text="ID", anchor=CENTER)
tree.heading("name", text="name", anchor=CENTER)
tree.heading("address", text="address", anchor=CENTER)
tree.heading("age", text="age", anchor=CENTER)
tree.heading("number", text="phone number", anchor=CENTER)

# Call the function to refresh and populate the Treeview with data
refresh_treeview()

# Start the Tkinter event loop to display the GUI
root.mainloop()
