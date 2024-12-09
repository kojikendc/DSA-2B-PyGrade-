# lab/lab.py
from lab.lab_activities import calculate_lab_activities
from lab.lab_exams import calculate_lab_exams

def calculate_lab_grade(phase_name, exam_scores, exam_totals):
    print(f"\n--- {phase_name} Laboratory Grade Calculation ---")

    # Pass the necessary arguments to the functions
    total_lab_activities_score = calculate_lab_activities(exam_scores, exam_totals)
    total_lab_exam_score, _, _ = calculate_lab_exams(exam_scores, exam_totals)

    total_lab_grade = total_lab_activities_score + total_lab_exam_score

    print(f"\n--- {phase_name} Laboratory Grade Report ---")
    print(f"Weighted Laboratory Activities Grade: {total_lab_activities_score:.2f}")
    print(f"Weighted Lab Exam Grade: {total_lab_exam_score:.2f}")
    print(f"{phase_name} Laboratory Grade: {total_lab_grade:.2f}")

    return total_lab_grade
