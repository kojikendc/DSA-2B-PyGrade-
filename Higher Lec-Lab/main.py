# main.py

from main_helper import calculate_combined_grades

def main():
    print("Welcome to the Grading System")

    # Calculate the Combined Grades for Midterm and Tentative Final
    midterm_combined_grade = calculate_combined_grades("Midterm")
    tentative_final_combined_grade = calculate_combined_grades("Tentative Final")

    # Calculate the Total Final Grade (Midterm = 33%, Tentative Final = 67%)
    total_final_grade = (midterm_combined_grade + tentative_final_combined_grade) / 2

    print("\n--- Total Final Grade Report ---")
    print(f"Midterm Combined Grade: {midterm_combined_grade:.2f}")
    print(f"Tentative Final Combined Grade: {tentative_final_combined_grade:.2f}")
    print(f"Total Final Grade: {total_final_grade:.2f}")

if __name__ == "__main__":
    main()
