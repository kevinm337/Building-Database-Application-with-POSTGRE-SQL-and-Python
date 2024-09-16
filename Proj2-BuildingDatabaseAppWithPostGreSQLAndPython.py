import psycopg2 


con=psycopg2.connect(
    dbname="studentdb",
    user="postgres",
    password="Messi123!@#",
    host="localhost",
    port="5432"
    )



# Function for Creating table
def create_table():
    cur=con.cursor()
    cur.execute("create table students(student_id serial primary key, name text, address text, age int, number text);")
    print("Students Table Created")
    con.commit()
    con.close()


# Function for Inserting Hard Coded Data
def insert_data_hardCoded():
    cur=con.cursor()
    cur.execute("insert into students(name,address,age,number) values ('Kevin','Dallas',26,'777');")
    print("Data Inserted in students table")
    con.commit()
    con.close()


# Function for Inserting Data
def insert_data_acceptDataFromUser():
    #code to accept data from the user
    name= input("Enter the name: ")
    address= input("Enter the address: ")
    age= input("Enter the age: ")
    number= input("Enter the number: ")
    cur=con.cursor()
    cur.execute("insert into students(name,address,age,number) values (%s,%s,%s,%s)",(name,address,age,number))#%s are the placeholders for (name,address,age,number). So we need 4 %s as there are 4 attributes
    print("Data Inserted in students table")
    con.commit()
    con.close()


# Function for Updating Data
def update_data():
    student_id=input("Enter id of the student to be updated")
    name= input("Enter the name: ")
    address= input("Enter the address: ")
    age= input("Enter the age: ")
    number= input("Enter the number: ")
    cur=con.cursor()
    cur.execute("update students set name=%s ,address=%s ,age=%s ,number=%s where student_id=%s",(name,address,age,number,student_id))
    print("Data Updated in students table")
    con.commit()
    con.close()
    

# Function for Updating single field
def update_single_field():
    student_id=input("Enter id of the student to be updated")
    cur=con.cursor()
    # This dictionary can be used to prompt users for different types of input by matching the key with the corresponding field
    # and message. For example, if a user selects key "1", they will be prompted to enter a new name.
    # Key: "1"...., Value: Tuple with field "name"... and message "Enter the new name"...
    fields = {
        "1":("name","Enter the new name"),
        "2":("address","Enter the new address"),
        "3":("age","Enter the new age"),
        "4":("number","Enter the new number")
    }
    print("Which field would you like to update: ")
    for key in fields:
        print(f"{key}:{fields[key][0]}")
    field_choice=input("Enter the number of the field you want to update: ")

    if field_choice in fields:
        field_name, promt= fields[field_choice]
        new_value=input(promt)
        sql= f"update students set {field_name}= %s where student_id=%s"
        cur.execute(sql,(new_value,student_id))
        print(f"{field_name} is updated successfully")
    else:
        print("This is an invalid choice")

    
    print("Data Updated in students table")
    con.commit()
    con.close()    



# Function for Deleting Data
def delete_data():
    student_id=input("Enter the ID of the student you want to delete")
    cur=con.cursor()

    cur.execute("select * from students where student_id=%s",(student_id,))
    student=cur.fetchone()


    if(student):
        print(f"Student to be deleted: ID {student[0]}, Name: {student[1]}, Address: {student[2]}, Age: {student[3]}, Number: {student[4]}")
        choice=input("Are you sure you want to delete the student? (yes/no)")
        if choice.lower() == "yes":
            cur.execute("delete from students where student_id=%s",(student_id,))
            print("Student record deleted")
        else:
            print("Deletion Canceled")
    else:
        print("Student not found")

    con.commit()
    con.close()  


def read_data():
    cur=con.cursor()
    cur.execute("select * from students;")
    students=cur.fetchall()
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Address: {student[2]}, Age: {student[3]}")
    cur.close() 


while True:
    print("\n Welcome to the student database management system")
    print("1. Create Table")
    print("2. Insert Data")
    print("3. Read Data")
    print("4. Update Data")
    print("5. Delete Data")
    print("6. Exit")
    choice=input("Enter your choice (1-6): ")
    if(choice=='1'):
        create_table()
    elif(choice=='2'):
        insert_data_acceptDataFromUser()
    elif(choice=='3'):
        read_data()
    elif(choice=='4'):
        update_single_field()
    elif(choice=='5'):
        delete_data()
    elif(choice=='6'):
        break
    else:
        print("Invalid Choice. Please enter a number between 1-6")
