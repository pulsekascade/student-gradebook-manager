""" 

Version 1 – Stage 2: Student Gradebook Manager 

Features: 

- Menu interface 

- Add student and score 

- Input validation (score must be between 0 and 100) 

- Display all student records 

""" 

# This function prints the main menu options to the screen.
def show_menu(): 
    print("\n--- Gradebook Manager ---")  # Title/header
    print("1. Add student data")        # Option to add student data
    print("2. Display all student records")  # Option to display all records
    print("3. Exit")                    # Option to exit the program

    # This function collects a student's name and test score, validates the input,
# and stores the data in the records dictionary.
def add_student_data(records):
    name = input("Enter student name: ").strip()  # Ask for student's name, strip removes extra spaces

    score_input = input("Enter test score (0–100): ").strip()  # Ask for test score as string

    try:
        score = int(score_input)  # Try converting the input into an integer

        if 0 <= score <= 100:  # Check if the score is between 0 and 100
            if name in records:  # If the student already exists in the dictionary
                records[name].append(score)  # Add the new score to their list
            else:
                records[name] = [score]  # Create a new entry with the score in a list

            print(f"Added data for {name}.")  # Confirm that the data was added
        else:
            print("Score must be between 0 and 100.")  # Show error if score is out of range

    except ValueError:
        # This runs if the score_input is not a number (e.g. "abc")
        print("Invalid input. Please enter a whole number.")
# This function prints out all student names and their scores from the dictionary.
def display_all_records(records):
    if not records:
        # If the dictionary is empty, tell the user there are no records
        print("No records to display.")
    else:
        print("\nAll Student Records:")  # Header
        for name, scores in records.items():  # Loop through each student and their scores
            print(f"{name}: Scores = {scores}")  # Print each name and list of scores
# This is the main function that controls the program's flow.
def main():
    student_records = {}  # Create an empty dictionary to store student data

    while True:  # Loop will repeat until user chooses to exit
        show_menu()  # Display the main menu
        choice = input("Enter your choice (1–3): ").strip()  # Ask for user's menu choice

        if choice == "1":
            add_student_data(student_records)  # Call function to add student data
        elif choice == "2":
            display_all_records(student_records)  # Call function to show all records
        elif choice == "3":
            print("Exiting program. Goodbye!")  # Say goodbye
            break  # Exit the loop, ending the program
        else:
            # This runs if the user types a menu option that isn't 1, 2, or 3
            print("Invalid choice. Please enter 1, 2, or 3.")


# This line checks if the program is being run directly (not imported)
# and then calls the main() function to start the program.
if __name__ == "__main__":
    main()