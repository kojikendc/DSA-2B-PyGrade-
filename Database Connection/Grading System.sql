-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS PyGrade_DB;
USE PyGrade_DB;

-- Admin (Admin can create faculty and student accounts)
CREATE TABLE IF NOT EXISTS Admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL -- Store hashed passwords
);

-- Faculty (Faculty will manage subjects and grades)
CREATE TABLE IF NOT EXISTS Faculty (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL -- Store hashed passwords
);

-- Student (Students will have their own login and view subjects/grades)
CREATE TABLE IF NOT EXISTS Student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id SMALLINT UNSIGNED NOT NULL UNIQUE,  -- Unique student_id
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL -- Store hashed passwords
);

-- Subjects (Subjects that the faculty can create)
CREATE TABLE IF NOT EXISTS Subjects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    year_level INT NOT NULL,
    sub_type ENUM('Lec', 'Lab', 'Lec/Lab') NOT NULL,
    sub_code VARCHAR(10) NOT NULL UNIQUE,  -- Allow letters and numbers
    subject_name VARCHAR(50) NOT NULL
);

-- Enrollment (Handles the enrollment of students in subjects)
CREATE TABLE IF NOT EXISTS Enrollment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT UNSIGNED NOT NULL,  -- Foreign key references student_id in Student
    subject_id INT NOT NULL,  -- Foreign key references Subjects table
    FOREIGN KEY (student_id) REFERENCES Student(id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES Subjects(id) ON DELETE CASCADE,
    UNIQUE(student_id, subject_id, term_phase)  -- Prevent duplicate enrollments
);

-- Grades (Stores grades for students in specific subjects and terms)
CREATE TABLE IF NOT EXISTS Grades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT UNSIGNED NOT NULL,  -- Foreign key references student_id in Student
    subject_id INT NOT NULL,  -- Foreign key references Subjects table
    term_phase VARCHAR(20) NOT NULL,
    grade DECIMAL(5,2) NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Student(id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES Subjects(id) ON DELETE CASCADE,
    UNIQUE(student_id, subject_id, term_phase)  -- Prevent duplicate grades for the same term
);

-- Query to view subjects and grades for a student (used in the student functions)
SELECT s.student_id, sub.subject_name, g.term_phase, g.grade
FROM Grades g
JOIN Student s ON g.student_id = s.id
JOIN Subjects sub ON g.subject_id = sub.id
WHERE s.student_id = ?; -- Placeholder for dynamic student_id
