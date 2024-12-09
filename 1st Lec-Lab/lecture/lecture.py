# lecture/lecture.py

from lecture.written import calculate_written_works
from lecture.participation import calculate_participation_activities
from lecture.lecture_exams import calculate_lecture_exams

def calculate_lecture_grade(phase_name):
    print(f"\n--- {phase_name} Lecture Grade Calculation ---")

    total_written_score = calculate_written_works()
    total_participation_score = calculate_participation_activities()
    total_exam_score, exam_scores, exam_totals = calculate_lecture_exams()

    total_lecture_grade = total_written_score + total_participation_score + total_exam_score

    print(f"\n--- {phase_name} Lecture Grade Report ---")
    print(f"Weighted Written Grade: {total_written_score:.2f}")
    print(f"Weighted Participation Grade: {total_participation_score:.2f}")
    print(f"Weighted Exam Grade: {total_exam_score:.2f}")
    print(f"{phase_name} Lecture Grade: {total_lecture_grade:.2f}")

    return total_lecture_grade, exam_scores, exam_totals
