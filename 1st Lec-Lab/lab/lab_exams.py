# lab/lab_exams.py

from lab.component_scores import calculate_component_scores, get_weighted_score

def calculate_lab_exams(exam_scores, exam_totals):  # Accept these arguments
    weighted_exam_score = get_weighted_score(exam_scores, exam_totals, 0.4)
    return weighted_exam_score, exam_scores, exam_totals
