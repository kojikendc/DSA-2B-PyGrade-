from written import calculate_written_scores
from participation import calculate_participation_scores
from exam import calculate_exam_scores

def calculate_phase_grade(phase_name):
    print(f"\n--- {phase_name} Grade Calculation ---")
    
    # Written Works (Summative Quizzes + Seatworks)
    total_summative_score, total_attendance_quizzes_score = calculate_written_scores()
    
    # Participation (Attendance + Assignments + Portfolio)
    total_attendance_score, total_assignment_score, total_portfolio_score = calculate_participation_scores()
    
    # Exams
    total_exam_score = calculate_exam_scores()
    
    # Total Grade Calculation
    total_written_works_score = total_summative_score + total_attendance_quizzes_score
    total_participation_score = total_attendance_score + total_assignment_score + total_portfolio_score
    total_grade = total_written_works_score + total_exam_score + total_participation_score

    print(f"\n--- {phase_name} Grade Report ---")
    print(f"Weighted Summative Quizzes Grade: {total_summative_score:.2f}")
    print(f"Weighted Seatworks Grade: {total_attendance_quizzes_score:.2f}")
    print(f"Weighted Exam Grade: {total_exam_score:.2f}")
    print(f"Weighted Attendance Grade: {total_attendance_score:.2f}")
    print(f"Weighted Assignment Grade: {total_assignment_score:.2f}")
    print(f"Weighted Portfolio Grade: {total_portfolio_score:.2f}")
    print(f"{phase_name} Grade: {total_grade:.2f}")
    
    return total_grade
