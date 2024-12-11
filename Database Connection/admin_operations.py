import mysql.connector
from mysql.connector import Error

def connect_to_db():
    """Connect to the PyGrade_DB MySQL database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password123W?',
            database='PyGrade_DB'
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def create_faculty_account(username, password):
    """Create a new faculty account."""
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO Faculty (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        connection.commit()
        print(f"Faculty account '{username}' created successfully.")
        cursor.close()
        connection.close()

def create_student_account(student_id, username, password):
    """Create a new student account."""
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO Student (student_id, username, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (student_id, username, password))
        connection.commit()
        print(f"Student account with ID {student_id} created successfully.")
        cursor.close()
        connection.close()
