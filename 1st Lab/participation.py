def calculate_component_scores(component_name):
    scores = [float(input(f"Enter score for {component_name}: "))]
    total_items = [float(input(f"Enter total number of items for {component_name}: "))]
    return scores, total_items

def calculate_participation_scores(phase_name):
    print(f"\n--- {phase_name} Participation Breakdown ---")
        
    # Attendance/Portfolio
    if phase_name == "Midterm":
        attendance_scores, attendance_totals = calculate_component_scores("Attendance")
    else:
        attendance_scores, attendance_totals = calculate_component_scores("Portfolio")

    # Homework (10%)
    homework_scores, homework_totals = calculate_component_scores("Homework")

    return attendance_scores, attendance_totals, homework_scores, homework_totals
