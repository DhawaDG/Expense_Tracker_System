#add functions
def add_expense(expenses):
    #input from user
    category = input("Enter Expense Category (Food, Rent, Travel, etc.): ").capitalize().strip() 
    amount = input("Enter Amount: ") 
    date = input("Enter Date (YYYY-MM-DD): ")
    #exception jandling
    try:
        amount = float(amount) #typecaste
        expense = {"category": category, "amount": amount, "date": date} #creating dict
        expenses.append(expense)  #add to file
        print(" Expense Added Successfully!")
    except ValueError:
        print(" Invalid amount. Please enter a number.")
#view functions
def view_expenses(expenses):
    if not expenses: #view empty file
        print("No expenses recorded.")
        return

    print("\n Expense List:")
    for index, expense in enumerate(expenses, start=1): #enumerate functions
        print(f"{index}. {expense['date']} | {expense['category']} | ${expense['amount']}")
#sum functions
def get_total_expense(expenses):
    total = sum(expense["amount"] for expense in expenses) #get total amount
    print(f" Total Expense: ${total:.2f}")
#remove functions
def remove_expense(expenses):
    view_expenses(expenses)
    try:
        expense_index = int(input("Enter expense number to remove: ")) - 1 #get index no from user while -1 secure actual array placing  of data 0,1,2,3...
        if 0 <= expense_index < len(expenses): # ensure expense index  must o to actual n index of expense dict
            removed_expense = expenses.pop(expense_index) #remove the dict a user want to have removed
            print(f" Expense '{removed_expense['category']}' removed.") #print removed category using concept of garbage collections
        else:
            print(" Invalid expense number.")
    except ValueError:
        print(" Please enter a valid number.")
 
