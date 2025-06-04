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