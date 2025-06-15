import os
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

DATA_FILE = "data.txt"

def get_valid_name():
    # Prompt for a non-blank student name
    while True:
        name = input("Enter student name: ").strip()
        if name == "":
            print("Name cannot be blank.")
        else:
            return name

def get_subject_scores():
    # Collect subject-score pairs until blank subject entered
    subject_scores = []
    while True:
        subject = input("Enter subject name (or press Enter to finish): ").strip()
        if subject == "":
            break
        try:
            score = int(input(f"Enter score for {subject}: "))
            if 0 <= score <= 100:
                subject_scores.append(f"{subject}-{score}")
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid score, please enter a number.")
    return subject_scores

def add_student():
    # Add a new student and their subject scores to the data file
    name = get_valid_name()
    subjects = get_subject_scores()
    if subjects:
        with open(DATA_FILE, "a") as file:
            file.write(f"{name}:{','.join(subjects)}\n")
        print("Student data saved.")
    else:
        print("No subjects entered; student not saved.")

def load_data():
    # Read all scores from the file into a list
    if not os.path.exists(DATA_FILE):
        return []
    scores = []
    with open(DATA_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                try:
                    name, subj_scores = line.split(":")
                    for entry in subj_scores.split(","):
                        subject, score = entry.split("-")
                        scores.append(int(score))
                except ValueError:
                    continue  # Ignore malformed lines
    return scores

def categorize_scores(scores):
    # Categorize scores by NCEA standards
    categories = {"Not Achieved": 0, "Achieved": 0, "Merit": 0, "Excellence": 0}
    for score in scores:
        if 0 <= score <= 49:
            categories["Not Achieved"] += 1
        elif 50 <= score <= 64:
            categories["Achieved"] += 1
        elif 65 <= score <= 84:
            categories["Merit"] += 1
        elif 85 <= score <= 100:
            categories["Excellence"] += 1
    return categories

def print_student_data():
    # Print all student records from the file
    if not os.path.exists(DATA_FILE):
        print("No student data found.")
        return
    print("\n--- Student Records ---")
    with open(DATA_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                try:
                    name, subj_scores = line.split(":")
                    formatted_scores = subj_scores.replace(",", ", ")
                    print(f"{name}: {formatted_scores}")
                except ValueError:
                    continue

def search_student():
    # Search for a student by name and display their subjects and scores
    if not os.path.exists(DATA_FILE):
        print("No student data found.")
        return
    search_name = input("Enter the name to search for: ").strip().lower()
    found = False
    with open(DATA_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                try:
                    name, subj_scores = line.split(":")
                    if name.lower() == search_name:
                        print(f"{name}: {subj_scores.replace(',', ', ')}")
                        found = True
                except ValueError:
                    continue
    if not found:
        print("Student not found.")

def show_all_raw_scores():
    # Print all scores loaded from the file
    scores = load_data()
    if scores:
        print("All scores:", scores)
    else:
        print("No scores found.")

def show_graphs_side_by_side(categories):
    # Display bar and pie charts side-by-side in a Tkinter window
    root = tk.Tk()
    root.title("Score Distribution Charts")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    # Bar chart on the left
    ax1.bar(categories.keys(), categories.values(), color="skyblue")
    ax1.set_title("Score Distribution (Bar Chart)")
    ax1.set_ylabel("Number of Scores")

    # Pie chart on the right
    ax2.pie(categories.values(), labels=categories.keys(), autopct="%1.1f%%")
    ax2.set_title("Score Distribution (Pie Chart)")

    plt.tight_layout()

    # Embed matplotlib figure into Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    root.mainloop()

def main():
    print("Welcome to Student Gradebook Manager v4")
    while True:
        print("\nMenu:")
        print("1. Add student data")
        print("2. Show student records (print)")
        print("3. Search for a student")
        print("4. Show score distribution charts (popups)")
        print("5. Show score distribution charts (side by side window)")
        print("6. Show all raw scores")
        print("7. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            print_student_data()
        elif choice == "3":
            search_student()
        elif choice == "4":
            scores = load_data()
            if scores:
                categories = categorize_scores(scores)
                # Show charts in separate popup windows
                plt.figure(figsize=(6, 4))
                plt.bar(categories.keys(), categories.values(), color="skyblue")
                plt.title("Score Distribution (Bar Chart)")
                plt.ylabel("Number of Scores")
                plt.tight_layout()
                plt.show()

                plt.figure(figsize=(6, 4))
                plt.pie(categories.values(), labels=categories.keys(), autopct="%1.1f%%")
                plt.title("Score Distribution (Pie Chart)")
                plt.tight_layout()
                plt.show()
            else:
                print("No scores available to display.")
        elif choice == "5":
            scores = load_data()
            if scores:
                categories = categorize_scores(scores)
                show_graphs_side_by_side(categories)
            else:
                print("No scores available to display.")
        elif choice == "6":
            show_all_raw_scores()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
