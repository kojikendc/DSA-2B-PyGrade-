# main_helper.py

from lecture.lecture import calculate_lecture_grade
from lab.lab import calculate_lab_grade

def calculate_combined_grades(phase_name):
    """
    Calculates the combined grade for lecture and laboratory.
    Lecture is weighted 40%, and Lab is weighted 60%.
    """
    print(f"\n+++ {phase_name} Lec/Lab Grade Calculation +++")
    
    # Calculate Lecture Grade
    lecture_grade, exam_scores, exam_totals = calculate_lecture_grade(phase_name)
    
    # Calculate Lab Grade
    lab_grade = calculate_lab_grade(phase_name, exam_scores, exam_totals)
    
    # Combine Grades (40% Lecture, 60% Lab)
    combined_grade = (0.4 * lecture_grade) + (0.6 * lab_grade)
    
    print(f"\n--- {phase_name} Lec/Lab Combined Grade: {combined_grade:.2f} ---")
    return combined_grade
