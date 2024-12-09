# lecture/component_scores.py

def get_weighted_score(scores, total_items, weight):
    total_score = sum((score / total) * 100 for score, total in zip(scores, total_items))
    weighted_score = (total_score / len(scores)) * weight
    return weighted_score

def calculate_component_scores(component_name):
    num_scores = int(input(f"\nEnter the number of {component_name}: "))
    scores = [float(input(f"Enter score for {component_name} {i + 1}: ")) for i in range(num_scores)]
    total_items = [float(input(f"Enter total number of items for {component_name} {i + 1}: ")) for i in range(num_scores)]
    return scores, total_items
