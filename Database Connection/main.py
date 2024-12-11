from admin_operations import create_faculty_account, create_student_account
from faculty_operations import create_subject, add_student_to_subject, edit_grade
from student_operations import view_subjects, view_grade
import mysql.connector

# Function to check if faculty login credentials are valid
def faculty_login():
    username = input("Enter Faculty Username: ")
    password = input("Enter Faculty Password: ")
    
    # Create connection to the database
    db = mysql.connector.connect(
        host="localhost",
        user="root",  # Change to your MySQL username
        password="password123W?",  # Change to your MySQL password
        database="PyGrade_DB"
    )
    cursor = db.cursor()
    
    query = "SELECT * FROM Faculty WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    
    result = cursor.fetchone()
    
    if result:
        print("Login successful!")
        return True
    else:
        print("No faculty in the database. Please check your username and password.")
        return False

# Function to check if admin login credentials are valid
def admin_login():
    username = input("Enter Admin Username: ")
    password = input("Enter Admin Password: ")
    
    # Hardcoded Admin credentials
    if username == "kojikendc" and password == "pass1212":
        print("Admin login successful!")
        return True
    else:
        print("Invalid Admin credentials.")
        return False

def admin_operations():
    while True:
        print("Admin Functions:")
        action = input("Do you want to (1) Create Faculty, (2) Create Student, (3) Logout: ")
        if action == "1":
            username = input("Enter Faculty Username: ")
            password = input("Enter Faculty Password: ")
            create_faculty_account(username, password)
        elif action == "2":
            student_id = input("Enter Student ID: ")
            username = input("Enter Student Username: ")
            password = input("Enter Student Password: ")
            create_student_account(student_id, username, password)
        elif action == "3":
            print("Logging out...")
            break  # Log out and exit admin operations
        else:
            print("Invalid option.")

def faculty_operations():
    while True:
        print("Faculty Functions:")
        action = input("Do you want to (1) Create Subject, (2) Add Student to Subject, (3) Edit Grade, (4) Logout: ")

        if action == "1":
            # Creating a subject
            year_level = int(input("Enter Year Level: "))
            sub_type = input("Enter Subject Type (Lec , Lab , Lec/Lab): ").strip()
            sub_code = input("Enter Subject Code: ").strip()
            subject_name = input("Enter Subject Name: ").strip()

            # Call the function to create the subject
            create_subject(year_level, sub_type, sub_code, subject_name)
            print(f"Subject '{subject_name}' created successfully.")

        elif action == "2":
            # Adding student to subject
            student_id = input("Enter Student ID: ").strip()
            subject_id = input("Enter Subject ID: ").strip()  # Updated to accept string

            # Call the function to add student to subject
            add_student_to_subject(student_id, subject_id)

        elif action == "3":
            # Editing grade
            student_id = input("Enter Student ID: ").strip()
            subject_id = input("Enter Subject ID: ").strip()  # Updated to accept string
            new_grade = float(input("Enter New Grade: ").strip())

            # Call the function to edit grade
            edit_grade(student_id, subject_id, new_grade)

        elif action == "4":
            print("Logging out...")
            break  # Exit the loop to log out
        else:
            print("Invalid choice, please try again.")

# xxxxxxxxx
def student_operations():
    while True:
        print("Student Functions:")
        student_id = int(input("Enter your Student ID: "))
        action = input("Do you want to (1) View Subjects, (2) View Grade in Subject, (3) Logout: ")
        if action == "1":
            view_subjects(student_id)
        elif action == "2":
            subject_id = int(input("Enter Subject ID: "))
            view_grade(student_id, subject_id)
        elif action == "3":
            print("Logging out...")
            break  # Log out and exit student operations
        else:
            print("Invalid option.")

def main():
    while True:
        # Login menu
        role = input("Enter your role (admin/faculty/student) or type 'logout' to exit: ").strip().lower()

        if role == "logout":
            print("Logging out...")
            break  # Exit the loop and terminate the program

        if role == "admin":
            if admin_login():
                admin_operations()

        elif role == "faculty":
            if faculty_login():
                faculty_operations()

        elif role == "student":
            student_operations()

        else:
            print("Invalid role.")

if __name__ == "__main__":
    main()
