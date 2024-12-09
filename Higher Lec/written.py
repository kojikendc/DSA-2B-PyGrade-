from component_scores import calculate_component_scores, get_weighted_score

def calculate_written_scores():
    # Summative Quizzes (20%)
    print("\n--- Written Component ---")
    summative_scores, summative_totals = calculate_component_scores("Summative Quizzes")
    total_summative_score = get_weighted_score(summative_scores, summative_totals, 0.2)
    
    # Seatworks (10%)
    attendance_quizzes_scores, attendance_quizzes_totals = calculate_component_scores("Seatworks")
    total_attendance_quizzes_score = get_weighted_score(attendance_quizzes_scores, attendance_quizzes_totals, 0.1)
    
    return total_summative_score, total_attendance_quizzes_score
