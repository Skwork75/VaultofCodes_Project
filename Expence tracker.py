import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

def load_expenses():
    """Load expenses from the CSV file and return a list of expense dictionaries."""
    expenses = []
    try:
        with open(FILE_NAME, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append({
                    "amount": float(row["amount"]),
                    "category": row["category"],
                    "date": row["date"]
                })
    except FileNotFoundError:
        pass
    return expenses


def save_expenses(expenses):
    """Save all expenses to the CSV file."""
    with open(FILE_NAME, mode="w", newline="") as file:
        fieldnames = ["amount", "category", "date"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for exp in expenses:
            writer.writerow(exp)


def add_expense(expenses):
    """Prompt user to add a new expense and save it to the file."""
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (Food, Transport, etc.): ").strip()
        if not category:
            category = "Uncategorized"
        date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")
        
        expense = {"amount": amount, "category": category, "date": date}
        expenses.append(expense)
        save_expenses(expenses)
        print("\n-----------------------------")
        print("Expense added successfully")
        print("-----------------------------\n")
    except ValueError:
        print("\nInvalid amount. Please enter a number.\n")


def overall_summary(expenses):
    """Display the total spending of all recorded expenses."""
    if not expenses:
        print("\nNo expenses recorded yet.\n")
        return
    total = sum(exp["amount"] for exp in expenses)
    print("\n====== Total Spending ======")
    print(f"Total Spending: ₹{total:.2f}")
    print("============================\n")


def category_summary(expenses):
    """Display the total spending for a specific category."""
    category = input("Enter category to check: ").strip()
    total = sum(exp["amount"] for exp in expenses if exp["category"].lower() == category.lower())
    print("\n====== Category Summary ======")
    print(f"Total spent on {category}: ₹{total:.2f}")
    print("================================\n")


def daily_summary(expenses):
    """Display expenses grouped by each day."""
    daily = {}
    for exp in expenses:
        daily[exp["date"]] = daily.get(exp["date"], 0) + exp["amount"]

    print("\n====== Daily Summary ======")
    for day, amt in sorted(daily.items()):
        print(f"{day}: ₹{amt:.2f}")
    print("============================\n")


def monthly_summary(expenses):
    """Display expenses grouped by each month."""
    monthly = {}
    for exp in expenses:
        month = exp["date"][:7]   
        monthly[month] = monthly.get(month, 0) + exp["amount"]

    print("\n====== Monthly Summary ======")
    for month, amt in sorted(monthly.items()):
        print(f"{month}: ₹{amt:.2f}")
    print("==============================\n")


def view_all(expenses):
    """Display a detailed list of all recorded expenses."""
    if not expenses:
        print("\nNo expenses recorded yet.\n")
        return

    expenses.sort(key=lambda x: x["date"])  
    print("\n====== All Expenses ======")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['date']} - {exp['category']} - ₹{exp['amount']:.2f}")
    print("===========================\n")


def delete_expense(expenses):
    """Allow the user to delete an expense by selecting its number."""
    view_all(expenses)
    if not expenses:
        return
    try:
        choice = int(input("Enter expense number to delete: "))
        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1)
            save_expenses(expenses)
            print("\n-----------------------------")
            print(f"Deleted: {removed['category']} - ₹{removed['amount']}")
            print("-----------------------------\n")
        else:
            print("\nInvalid choice.\n")
    except ValueError:
        print("\nPlease enter a valid number.\n")


def summary_menu(expenses):
    """Display the summary menu and handle user choices."""
    if not expenses:
        print("\nNo expenses recorded yet.\n")
        return
    
    while True:
        print("\n--- Summary Menu ---")
        print("1. Detailed Summary")
        print("2. Categorical expenses")
        print("3. Daily expenses")
        print("4. Monthly expenses")
        print("5. Total spending")
        print("6. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            view_all(expenses)
        elif choice == "2":
            category_summary(expenses)
        elif choice == "3":
            daily_summary(expenses)
        elif choice == "4":
            monthly_summary(expenses)
        elif choice == "5":
            overall_summary(expenses)    
        elif choice == "6":
            break
        else:
            print("\nInvalid choice, try again.\n")


def main():
    """Main function to run the Personal Expense Tracker."""
    expenses = load_expenses()

    while True:
        print("=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. Summary")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            summary_menu(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            print("\nExited successfully\n")
            break
        else:
            print("\nInvalid choice, try again.\n")

if __name__ == "__main__":
    main()

