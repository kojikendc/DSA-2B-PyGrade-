# lecture/participation.py

from lecture.component_scores import calculate_component_scores, get_weighted_score

def calculate_participation_activities():
    participation_scores, participation_totals = calculate_component_scores("Participation Activities")
    return get_weighted_score(participation_scores, participation_totals, 0.3)
