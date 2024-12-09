from main_helper import calculate_phase_grade

def main():
    print("Welcome to the Grading System")
    
    # Midterm Grade
    midterm_grade = calculate_phase_grade("Midterm")
    
    # Tentative Final Grade
    tentative_final_grade = calculate_phase_grade("Tentative Final")
    
    # Final Grade
    total_final_grade = (midterm_grade + tentative_final_grade) / 2
    print("\n--- Total Final Grade Report ---")
    print(f"Midterm Grade: {midterm_grade:.2f}")
    print(f"Tentative Final Grade: {tentative_final_grade:.2f}")
    print(f"Total Final Grade: {total_final_grade:.2f}")

# Run the program
if __name__ == "__main__":
    main()
