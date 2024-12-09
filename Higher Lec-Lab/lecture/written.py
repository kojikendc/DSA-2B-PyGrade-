# lecture/written.py

from lecture.component_scores import calculate_component_scores, get_weighted_score

def calculate_written_works():
    written_scores, written_totals = calculate_component_scores("Written Works")
    return get_weighted_score(written_scores, written_totals, 0.3)
