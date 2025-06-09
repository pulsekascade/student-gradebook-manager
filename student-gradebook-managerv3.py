import os  # Import the os module to interact with the operating system (used to check if a file exists)

MIN_SCORE = 0           # Define the minimum allowed score constant
MAX_SCORE = 100         # Define the maximum allowed score constant
DATA_FILE = "data.txt"  # Define the filename for saving/loading student data

def show_menu():  # Define function to display the main menu
    print("\n--- Gradebook Manager ---")  # Print a blank line and the menu header
    print("1. Add student data")         # Print menu option 1
    print("2. Display all student records")  # Print menu option 2
    print("3. Search for a student")     # Print menu option 3
    print("4. Exit")                     # Print menu option 4

def get_valid_name():  # Define function to get a non-empty student name
    while True:  # Start an infinite loop to repeatedly ask for input until valid
        name = input("Enter student name: ").strip()  # Ask for input and remove leading/trailing whitespace
        if name == "":  # Check if the name is an empty string
            print("Student name cannot be blank.")  # Notify user that blank names are not allowed
        else:  # If name is not blank
            return name  # Return the valid name and exit the function

def get_valid_score():  # Define function to get a valid integer score within range
    while True:  # Start infinite loop for repeated input attempts
        score_input = input(f"Enter test score ({MIN_SCORE}–{MAX_SCORE}): ").strip()  # Prompt for score and strip whitespace
        try:  # Try to convert the input to an integer
            score = int(score_input)  # Convert string input to integer
            if MIN_SCORE <= score <= MAX_SCORE:  # Check if score is within the valid range
                return score  # Return the valid score and exit the function
            else:  # If score is outside the allowed range
                print(f"Score must be between {MIN_SCORE} and {MAX_SCORE}.")  # Inform user of range limits
        except ValueError:  # If conversion to int fails (non-integer input)
            print("Invalid input. Please enter a whole number.")  # Inform user of invalid input type

def add_student_data(records):  # Define function to add student data to records dictionary
    name = get_valid_name()  # Call function to get a valid student name
    score = get_valid_score()  # Call function to get a valid score
    if name in records:  # Check if the student name already exists in the records dictionary
        records[name].append(score)  # Add the new score to the existing student's list of scores
    else:  # If student name does not exist in records
        records[name] = [score]  # Create a new entry with the student's name and a list containing the score
    print(f"Added score for {name}. Total scores recorded: {len(records[name])}")  # Confirm addition and show total scores for student

def search_student(records):  # Define function to search for a student in records
    name = input("Enter student name to search: ").strip()  # Prompt user to enter student name and strip whitespace
    if name in records:  # Check if the entered name exists in the records dictionary
        print(f"{name} has scores: {records[name]}")  # Display the student's scores
    else:  # If student not found
        print(f"No records found for {name}.")  # Inform the user that no record was found

def display_all_records(records):  # Define function to display all student records
    if not records:  # Check if the records dictionary is empty
        print("No student records to display.")  # Inform the user that there are no records
        return  # Exit the function early
    print("\n--- All Student Records ---")  # Print header for records display
    for name, scores in records.items():  # Iterate over all students and their scores
        print(f"{name}: {scores}")  # Print the student name and list of scores

def save_data(records):  # Define function to save student records to file
    try:
        with open(DATA_FILE, "w") as file:  # Open file in write mode
            for name, scores in records.items():  # Iterate over all records
                scores_str = ",".join(map(str, scores))  # Convert scores list to comma-separated string
                file.write(f"{name}:{scores_str}\n")  # Write name and scores to file
        print("Data saved successfully.")  # Notify user of success
    except IOError:  # Catch file I/O errors
        print("Error saving data to file.")  # Notify user of failure

def load_data():  # Define function to load student records from file
    records = {}  # Create empty dictionary to hold data
    if not os.path.exists(DATA_FILE):  # Check if data file exists
        return records  # Return empty records if no file found
    try:
        with open(DATA_FILE, "r") as file:  # Open file in read mode
            for line in file:  # Read each line
                line = line.strip()
                if line:  # If line is not empty
                    name, scores_str = line.split(":")  # Split into name and scores string
                    scores = list(map(int, scores_str.split(",")))  # Convert scores back to list of ints
                    records[name] = scores  # Add to records dictionary
    except IOError:
        print("Error loading data from file.")  # Notify user if loading fails
    return records  # Return loaded records

def main():  # Define main program function
    records = load_data()  # Load existing records from file
    while True:  # Start main program loop
        show_menu()  # Display menu
        choice = input("Choose an option: ").strip()  # Get user choice
        if choice == "1":  # Add student data
            add_student_data(records)
        elif choice == "2":  # Display all records
            display_all_records(records)
        elif choice == "3":  # Search for student
            search_student(records)
        elif choice == "4":  # Exit program
            save_data(records)  # Save data before exiting
            print("Exiting program. Goodbye!")
            break  # Exit loop and end program
        else:
            print("Invalid option. Please enter 1, 2, 3, or 4.")  # Handle invalid input

if __name__ == "__main__":  # If this script is run directly
    main()  # Call main function to start program