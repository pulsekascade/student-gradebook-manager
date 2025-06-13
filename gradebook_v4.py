import os
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

DATA_FILE = "data.txt"

def get_valid_name():
    while True:
        name = input("Enter student name: ").strip()
        if name == "":
            print("Name cannot be blank.")
        else:
            return name

def get_subject_scores():
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
    name = get_valid_name()
    subjects = get_subject_scores()
    if subjects:
        with open(DATA_FILE, "a") as file:
            file.write(f"{name}:{','.join(subjects)}\n")
        print("Student data saved.")
    else:
        print("No subjects entered; student not saved.")

def load_data():
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
                    continue  # Skip malformed lines
    return scores

def categorize_scores(scores):
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

def show_bar_chart(categories):
    plt.figure(figsize=(6, 4))
    plt.bar(categories.keys(), categories.values(), color="skyblue")
    plt.title("Score Distribution (Bar Chart)")
    plt.ylabel("Number of Scores")
    plt.tight_layout()
    plt.show()

def show_pie_chart(categories):
    plt.figure(figsize=(6, 4))
    plt.pie(categories.values(), labels=categories.keys(), autopct="%1.1f%%")
    plt.title("Score Distribution (Pie Chart)")
    plt.tight_layout()
    plt.show()

def print_student_data():
    if not os.path.exists(DATA_FILE):
        print("No student data found.")
        return

    with open(DATA_FILE, "r") as file:
        print("\n--- Student Records ---")
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
    scores = load_data()
    if scores:
        print("All scores:", scores)
    else:
        print("No scores found.")

def main():
    print("Welcome to Student Gradebook Manager v4")
    while True:
        print("\nMenu:")
        print("1. Add student data")
        print("2. Show score distribution charts (single)")
        print("3. Exit")
        print("4. Show student records only")
        print("5. Search for a student")
        print("6. Show all raw scores")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            scores = load_data()
            if scores:
                print_student_data()
                categories = categorize_scores(scores)
                show_bar_chart(categories)
                show_pie_chart(categories)
            else:
                print("No scores available to display.")
        elif choice == "3":
            print("Goodbye!")
            break
        elif choice == "4":
            print_student_data()
        elif choice == "5":
            search_student()
        elif choice == "6":
            show_all_raw_scores()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
