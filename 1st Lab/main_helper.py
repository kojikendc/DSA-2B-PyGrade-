from written import calculate_written_scores
from participation import calculate_participation_scores
from lab_activity import calculate_lab_activity_scores
from exam import calculate_exam_scores


def get_weighted_score(scores, total_items, weight):
    total_score = sum((score / total) * 100 for score, total in zip(scores, total_items))
    weighted_score = (total_score / len(scores)) * weight
    return weighted_score

def calculate_phase_grade(phase_name):
    print(f"\n--- {phase_name} Grade Calculation ---")
    
    # Written Component (30%)
    written_scores, written_totals = calculate_written_scores()
    total_written_score = get_weighted_score(written_scores, written_totals, 0.3)
    
    # Participation Component (30%)
    attendance_scores, attendance_totals, homework_scores, homework_totals = calculate_participation_scores(phase_name)
    lab_scores, lab_totals = calculate_lab_activity_scores(phase_name)
    total_lab_score = get_weighted_score(lab_scores, lab_totals, 0.1)
    total_attendance_score = get_weighted_score(attendance_scores, attendance_totals, 0.1)
    total_homework_score = get_weighted_score(homework_scores, homework_totals, 0.1)
    total_participation_score = total_lab_score + total_attendance_score + total_homework_score

    # Exam Component (40%)
    exam_scores, exam_totals = calculate_exam_scores()
    total_exam_score = get_weighted_score(exam_scores, exam_totals, 0.4)
    
    # Total Grade
    total_grade = total_written_score + total_participation_score + total_exam_score
    print(f"\n--- {phase_name} Grade Report ---")
    print(f"Weighted Quiz Grade: {total_written_score:.2f}")
    print(f"Weighted Participation Grade: {total_participation_score:.2f}")
    print(f"Weighted Exam Grade: {total_exam_score:.2f}")
    print(f"{phase_name} Grade: {total_grade:.2f}")
    return total_grade
