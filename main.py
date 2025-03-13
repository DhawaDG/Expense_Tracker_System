from expense_operations import add_expense, view_expenses, get_total_expense, remove_expense
from file_handler import save_expenses_to_file, load_expenses_from_file

# Load expenses when the program starts
expenses = load_expenses_from_file()

def show_menu():
    print("\n Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Get Total Expense")
    print("4. Remove Expense")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_expense(expenses)
    elif choice == "2":
        view_expenses(expenses)
    elif choice == "3":
        get_total_expense(expenses)
    elif choice == "4":
        remove_expense(expenses)
    elif choice == "5":
        save_expenses_to_file(expenses)
        print("Expenses saved. Exiting Expense Tracker.")
        break
    else:
        print(" Invalid option. Try again.")


