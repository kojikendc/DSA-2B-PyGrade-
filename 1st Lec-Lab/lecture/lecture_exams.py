# lecture/lecture_exams.py

from lecture.component_scores import calculate_component_scores, get_weighted_score

def calculate_lecture_exams():
    exam_scores, exam_totals = calculate_component_scores("Exams")
    weighted_exam_score = get_weighted_score(exam_scores, exam_totals, 0.4)
    return weighted_exam_score, exam_scores, exam_totals
