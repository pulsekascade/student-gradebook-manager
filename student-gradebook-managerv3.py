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
