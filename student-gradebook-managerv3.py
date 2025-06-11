import os  # Used to check if a file exists

MIN_SCORE = 0           # Minimum allowed test score
MAX_SCORE = 100         # Maximum allowed test score
DATA_FILE = "data.txt"  # File to store student records

def show_menu():
    print("\n--- Gradebook Manager ---")
    print("1. Add student data")
    print("2. Display all student records")
    print("3. Search for a student")
    print("4. Exit")

def get_valid_name():
    while True:
        name = input("Enter student name: ").strip()
        if name == "":
            print("Student name cannot be blank.")
        else:
            return name

def get_valid_score():
    while True:
        score_input = input(f"Enter test score ({MIN_SCORE}–{MAX_SCORE}): ").strip()
        try:
            score = int(score_input)
            if MIN_SCORE <= score <= MAX_SCORE:
                return score
            else:
                print(f"Score must be between {MIN_SCORE} and {MAX_SCORE}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def add_student_data(records):
    name = get_valid_name()
    score = get_valid_score()
    if name in records:
        records[name].append(score)
    else:
        records[name] = [score]
    print(f"Added score for {name}. Total scores recorded: {len(records[name])}")

def search_student(records):
    name = input("Enter student name to search: ").strip()
    if name in records:
        print(f"{name} has scores: {records[name]}")
    else:
        print(f"No records found for {name}.")

def display_all_records(records):
    if not records:
        print("No student records to display.")
        return
    print("\n--- All Student Records ---")
    for name, scores in records.items():
        print(f"{name}: {scores}")

def save_data(records):
    try:
        with open(DATA_FILE, "w") as file:
            for name, scores in records.items():
                scores_str = ",".join(map(str, scores))  # Join scores as comma-separated string
                file.write(f"{name}:{scores_str}\n")     # Write in format name:score1,score2,...
        print("Data saved successfully.")
    except IOError:
        print("Error saving data to file.")

def load_data():
    records = {}
    if not os.path.exists(DATA_FILE):
        return records  # Return empty if file doesn't exist
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    name, scores_str = line.split(":")
                    scores = list(map(int, scores_str.split(",")))  # Convert string scores to integers
                    records[name] = scores
    except IOError:
        print("Error loading data from file.")
    return records

def main():
    records = load_data()  # Load records from file (if it exists)

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student_data(records)
        elif choice == "2":
            display_all_records(records)
        elif choice == "3":
            search_student(records)
        elif choice == "4":
            save_data(records)  # Save all records before exiting
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()  # Entry point: run main program loop if this file is executed