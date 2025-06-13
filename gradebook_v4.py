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