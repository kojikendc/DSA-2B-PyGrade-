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

def view_subjects(student_id):
    """View subjects enrolled by the student."""
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = """
        SELECT sub.subject_name
        FROM Grades g
        JOIN Subjects sub ON g.subject_id = sub.id
        WHERE g.student_id = %s
        """
        cursor.execute(query, (student_id,))
        subjects = cursor.fetchall()
        for subject in subjects:
            print(subject[0])
        cursor.close()
        connection.close()

def view_grade(student_id, subject_id):
    """View the grade of a student in a specific subject."""
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        query = """
        SELECT g.grade
        FROM Grades g
        WHERE g.student_id = %s AND g.subject_id = %s
        """
        cursor.execute(query, (student_id, subject_id))
        grade = cursor.fetchone()
        if grade:
            print(f"Grade for subject ID {subject_id}: {grade[0]}")
        else:
            print("No grade found.")
        cursor.close()
        connection.close()
