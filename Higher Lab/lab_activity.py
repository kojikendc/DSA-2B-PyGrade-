def calculate_component_scores(component_name):
    num_scores = int(input(f"\nEnter the number of {component_name}: "))
    scores = [float(input(f"Enter score for {component_name} {i + 1}: ")) for i in range(num_scores)]
    total_items = [float(input(f"Enter highest possible score in {component_name} {i + 1}: ")) for i in range(num_scores)]
    return scores, total_items

def calculate_lab_activity_scores(phase_name):
    # Lab Report (10%)
    lab_scores, lab_totals = calculate_component_scores("Lab Report")

    return lab_scores, lab_totals
