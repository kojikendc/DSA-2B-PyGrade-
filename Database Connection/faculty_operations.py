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

def create_subject(year_level, sub_type, sub_code, subject_name):
    """Create a new subject."""
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO Subjects (year_level, sub_type, sub_code, subject_name) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (year_level, sub_type, sub_code, subject_name))
        connection.commit()
        print(f"Subject '{subject_name}' created successfully.")
        cursor.close()
        connection.close()

# xxxxxxxxxxxx
def add_student_to_subject(student_id, subject_id):
    """Assign a student to a subject."""
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO Grades (student_id, subject_id) VALUES (%s, %s)"
        cursor.execute(query, (student_id, subject_id))
        connection.commit()
        print(f"Student with ID {student_id} added to subject with ID {subject_id}.")
        cursor.close()
        connection.close()

# xxxxxxxxxxxx
def edit_grade(student_id, subject_id, new_grade):
    """Edit the grade of a student in a subject."""
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE Grades SET grade = %s WHERE student_id = %s AND subject_id = %s"
        cursor.execute(query, (new_grade, student_id, subject_id))
        connection.commit()
        print(f"Grade updated to {new_grade} for student ID {student_id} in subject ID {subject_id}.")
        cursor.close()
        connection.close()
