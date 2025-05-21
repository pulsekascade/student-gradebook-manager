"""
Version 2 – Student Gradebook Manager

Upgrades from Version 1:
- Introduced input validation loop in a reusable function
- Used constants for score range (MIN_SCORE, MAX_SCORE)
- Enhanced user feedback
- Improved output formatting
- More modular code for maintainability
"""

# Constants for minimum and maximum valid scores
MIN_SCORE = 0
MAX_SCORE = 100

# Function to display the main menu
def show_menu():
    print("\n--- Gradebook Manager ---")  # Title
    print("1. Add student data")         # Option 1
    print("2. Display all student records")  # Option 2
    print("3. Exit")                     # Option 3

# Reusable function to validate and return a score
def get_valid_score():
    while True:
        # Prompt user to enter a score
        score_input = input(f"Enter test score ({MIN_SCORE}–{MAX_SCORE}): ").strip()
        try:
            score = int(score_input)  # Convert to integer
            if MIN_SCORE <= score <= MAX_SCORE:  # Check if score is in range
                return score  # Valid score returned
            else:
                print(f"Score must be between {MIN_SCORE} and {MAX_SCORE}.")  # Out of range
        except ValueError:
            print("Invalid input. Please enter a whole number.")  # Not a number

# Function to add a student and their score
def add_student_data(records):
    name = input("Enter student name: ").strip()  # Prompt for name

    score = get_valid_score()  # Call validation function to get score

    # Add the score to the student's record
    if name in records:
        records[name].append(score)  # Append score to existing student
    else:
        records[name] = [score] # Create new entry if student is new

    # Display how many scores the student has now
    print(f"Added score for {name}. Total scores recorded: {len(records[name])}")

# Function to display all student records in a table
def display_all_records(records):
    if not records:
        print("No records to display.")  # If dictionary is empty
    else:
        print("\nAll Student Records:")  # Header
        print(f"{'Student':<12} | Scores")  # Column titles
        print("-" * 30)  # Divider
        for name, scores in records.items():
            print(f"{name:<12} | {scores}")  # Print each student's name and scores

# Main program function to control flow
def main():
    student_records = {}  # Dictionary to store data


    while True:  # Loop until user chooses to exit
        show_menu()  # Show main menu
        choice = input("Enter your choice (1–3): ").strip()  # Get menu choice

        if choice == "1":
            add_student_data(student_records)  # Add student
        elif choice == "2":
            display_all_records(student_records)  # Display records
        elif choice == "3":
            print("Exiting program. Goodbye!")  # Exit message
            break  # End loop and exit
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")  # Invalid menu input

# Entry point for the program
if __name__ == "__main__":
    main()
