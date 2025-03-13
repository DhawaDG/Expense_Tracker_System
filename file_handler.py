import json
import os
#global variable
FILE_PATH="data/expense.txt"
##file handling
def save_expenses_to_file(expenses):
    try:
        with open("FILE_PATH", "w") as file:
            json.dump(expenses, file)
        print("Expenses saved to file.")
    except Exception as e:
        print(f" Error saving expense: {e}")

def load_expenses_from_file():

    try:
        if not os.path.exists(FILE_PATH):
            return[]
        with open("FILR_NAME", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
