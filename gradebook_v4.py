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
