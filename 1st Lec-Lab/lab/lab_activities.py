# lab/lab_activities.py

from lab.component_scores import calculate_component_scores, get_weighted_score

def calculate_lab_activities(exam_scores, exam_totals):  
    lab_scores, lab_totals = calculate_component_scores("Laboratory Activities")
    return get_weighted_score(lab_scores, lab_totals, 0.6)