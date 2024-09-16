import psycopg2

con=psycopg2.connect(
    dbname="footballdb",
    user="postgres",
    password="Messi123!@#",
    host="localhost",
    port="5432"
    )


def create_table():
    cur=con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS football(
            football_id SERIAL PRIMARY KEY,
            name TEXT,
            address TEXT,
            age INT,
            number TEXT
        );
    """)
    print("Football Table Created (if it did not already exist)")
    con.commit()
    

def insert_data():
    cur=con.cursor()
    name=input("Enter name: ")
    address=input("Enter address: ")
    age=input("Enter age: ")
    number=input("Enter number: ")
    cur.execute("insert into football(name,address,age,number) values (%s,%s,%s,%s)",(name,address,age,number))
    print("Data Inserted")
    con.commit()
    


def update_data():
    cur=con.cursor()
    football_id=input("Enter the ID of the student: ")
    name=input("Enter new name: ")
    address=input("Enter new address: ")
    age=input("Enter new age: ")
    number=input("Enter new number: ")
    cur.execute("update football set name=%s, address=%s, age=%s, number=%s where football_id=%s", (name,address,age,number,football_id))
    print("Data Updated")
    con.commit()
    


def update_single_field():
    cur=con.cursor()
    football_id=input("Enter the ID of the football player: ")
    fields={
        "1":("name","Enter the new name: "),
        "2":("address","Enter the new address: "),
        "3":("name","Enter the new age: "),
        "4":("number","Enter the new number: ")
    }
    print("Which field would you like to update: ")
    for key in fields:
        print(f"{key}:{fields[key][0]}")
    field_choice=input("Enter the number of the field you want to update: ")

    if field_choice in fields:
        field_name,promt=fields[field_choice]
        new_value=input(promt)
        sql= f"update football set {field_name}= %s where football_id=%s"
        cur.execute(sql,(new_value,football_id))
        print(f"{field_name} is updated successfully")
    else:
        print("This is an invalid choice")
    
    print("Data Updated in football table")
    con.commit()
     



def delete_data():
    cur=con.cursor()
    football_id=input("Enter the ID of the football player: ")
    cur.execute("select * from football where football_id=%s",football_id,)
    football=cur.fetchone()
    
    if(football):
        print(f"Football student to be deleted is: ID: {football[0]}, Name: {football[1]}, Address: {football[2]}, Age: {football[3]}, Number: {football[4]}")
        choice=input("Are you sure you want to delete this record- (yes/no): ")
        if(choice.lower()=='yes'):
            cur.execute("delete from football where football_id=%s", (football_id,))
            print("Football record deleted")
        else:
            print("Deletion Canceled")
    else:
        print("Football Record not found")
    con.commit()
    


def read_data():
    cur=con.cursor()
    cur.execute("select * from football;")
    football=cur.fetchall()
    for footb in football:
        print(f"ID: {footb[0]}, Name: {footb[1]}, Address: {footb[2]}, Age: {footb[3]}, Number: {footb[4]}")
    


while(True):
    print("\n Welcome to the student database management system")
    print("1. Create Table")
    print("2. Insert Data")
    print("3. Read Data")
    print("4. Update Data")
    print("5. Delete Data")
    print("6. Exit")
    choice=input("Enter your choice (1-6): ")
    if choice=='1':
        create_table()
    elif choice=='2':
        insert_data()
    elif choice=='3':
        read_data()
    elif choice=='4':
        update_single_field()
    elif choice=='5':
        delete_data()
    elif choice=='6':
        break
    else:
        print("Invalid Choice. Please select choice from 1-6. ")
    