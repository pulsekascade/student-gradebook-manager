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