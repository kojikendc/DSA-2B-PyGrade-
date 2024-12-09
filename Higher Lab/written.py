def calculate_written_scores():
    print("\n--- Written Component (Quizzes) ---")
    num_scores = int(input("Enter the number of quizzes: "))
    scores = [float(input(f"Enter score for Quiz {i + 1}: ")) for i in range(num_scores)]
    total_items = [float(input(f"Enter total number of items for Quiz {i + 1}: ")) for i in range(num_scores)]
    return scores, total_items
