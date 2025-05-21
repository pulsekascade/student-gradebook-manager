"""
Version 2 – Student Gradebook Manager

Upgrades from Version 1:
- Introduced input validation loop in a reusable function
- Used constants for score range (MIN_SCORE, MAX_SCORE)
- Enhanced user feedback
- Improved output formatting
- More modular code for maintainability
"""

# Constants for minimum and maximum valid scores
MIN_SCORE = 0
MAX_SCORE = 100

# Function to display the main menu
def show_menu():
    print("\n--- Gradebook Manager ---")  # Title
    print("1. Add student data")         # Option 1
    print("2. Display all student records")  # Option 2
    print("3. Exit")                     # Option 3
