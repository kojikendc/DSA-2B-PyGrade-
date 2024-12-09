from component_scores import calculate_component_scores, get_weighted_score

def calculate_participation_scores():
    print("\n--- Participation Component ---")
    
    # Attendance (10%)
    attendance_scores, attendance_totals = calculate_component_scores("Attendance")
    total_attendance_score = get_weighted_score(attendance_scores, attendance_totals, 0.1)
    
    # Assignments (10%)
    assignment_scores, assignment_totals = calculate_component_scores("Assignments")
    total_assignment_score = get_weighted_score(assignment_scores, assignment_totals, 0.1)
    
    # Portfolio (10%)
    portfolio_scores, portfolio_totals = calculate_component_scores("Portfolio")
    total_portfolio_score = get_weighted_score(portfolio_scores, portfolio_totals, 0.1)
    
    return total_attendance_score, total_assignment_score, total_portfolio_score
