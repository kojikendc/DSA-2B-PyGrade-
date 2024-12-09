from component_scores import calculate_component_scores, get_weighted_score

def calculate_exam_scores():
    print("\n--- Exam Component ---")
    exam_scores, exam_totals = calculate_component_scores("Exams")
    total_exam_score = get_weighted_score(exam_scores, exam_totals, 0.4)
    return total_exam_score
