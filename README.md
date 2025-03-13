# Expense Tracking System

## Overview
A CLI-based expense tracking system to help users manage their expenses efficiently. This system allows users to add, view, calculate total expenses, and remove expenses.

---

## Features & Functionalities
- **Add Expenses**: Record expenses with details like category, amount, and date.
- **View Expenses**: Display all recorded expenses in a structured format.
- **Calculate Total Expenses**: Compute the total amount spent across all categories.
- **Remove Expenses**: Delete specific expenses from the record.

---

## Technologies & Concepts Used
- **Data Structures**: Lists and dictionaries for storing and managing expenses.
- **File Handling**: Save and load expenses using JSON for persistent storage.
- **Error Handling**: Input validation for expense details (e.g., amount as a number).
- **Functions**: Modular and reusable functions for each operation (add, view, calculate, remove).

---

## Code Structure
- **`main.py`**: Manages the menu and user interaction.
- **`expense_operations.py`**: Implements expense logic (add, view, calculate, remove).
- **`file_handler.py`**: Saves and loads expenses to/from a file.

---

## Challenges & Learnings
1. **Understanding Generator Expressions**: Example like line 25   total = sum(expense["amount"] for expense in expenses), t is similar to a list comprehension but uses parentheses () instead of square brackets []. Unlike a list comprehension, which creates a list in memory, a generator expression generates values on-the-fly (lazily) and does not store them in memory.
3. **Enumerator Functions**: I was astonished see  use this loop over an iterable (like a list) while keeping track of both the index and the value of each time.

---

## Future Improvements
- **Expense Categorization**: Allow users to categorize expenses and view summaries by category.
- **Data Visualization**: Add visual representations (e.g., charts) of expense data.
- **GUI Development**: Create a graphical user interface for easier interaction and improved usability.

---

*** Author Name *** Dhawa Dorje Ghising(DhawaDG)


## License
This project is licensed under the MIT License. See the file  LICENSE  for details.