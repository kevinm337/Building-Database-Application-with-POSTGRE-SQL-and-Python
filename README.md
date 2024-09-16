Student/Football Database Management Application

This Python project provides a graphical interface (GUI) for managing a student database using Tkinter and PostgreSQL. It allows users to perform various operations such as adding, retrieving, and displaying student records.

Features

Add Students: Insert new student records into the database.
View Students: Display all student records in a tree view.
Database Connection: Establishes a connection to a PostgreSQL database.
Error Handling: Displays error messages if any database operations fail.
Prerequisites

Before you begin, ensure you have the following installed on your machine:

Python 3.x
PostgreSQL
Tkinter (comes pre-installed with Python)
psycopg2 (Install it using pip install psycopg2)
Installation

Clone the Repository:
bash
Copy code
git clone https://github.com/yourusername/student-database-app.git
cd student-database-app
Install Dependencies:
Install the required Python libraries:

bash
Copy code
pip install psycopg2
Set Up PostgreSQL:
Create a PostgreSQL database and table by following these steps:

sql
Copy code
CREATE DATABASE studentdb;
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(255),
    age INT,
    number VARCHAR(15)
);
Update the connection parameters in the Python file as needed:

python
Copy code
con=psycopg2.connect(
    dbname="studentdb",
    user="postgres",
    password="your_password",
    host="localhost",
    port="5432"
)
Usage

Run the Application:
Execute the Python script to launch the GUI:

bash
Copy code
python proj2_Updated.py
GUI Overview:
Use the interface to add new student details.
Click "Refresh" to update and display the current list of students.
Handle any errors or issues through the pop-up messages.
Known Issues

Ensure that the PostgreSQL server is running before attempting to execute queries.
Ensure that the correct credentials are provided for the PostgreSQL connection.
Contributing

Feel free to fork this repository and submit pull requests to contribute to this project.

License

This project is licensed under the MIT License.

