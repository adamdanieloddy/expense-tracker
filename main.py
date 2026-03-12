# Expense Tracker - Main Program
# Now with delete feature and file saving!

import json
import os

EXPENSES_FILE = "expenses.json"

def load_expenses():
    """Load expenses from file"""
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, "r") as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    """Save expenses to file"""
    with open(EXPENSES_FILE, "w") as file:
        json.dump(expenses, file, indent=2)
    print("✓ Expenses saved!")

def main():
    expenses = load_expenses()
    
    while True:
        print("\n" + "="*40)
        print("Welcome to Expense Tracker!")
        print("="*40)
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. Delete an expense")
        print("4. Exit")
        print("="*40)
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
            save_expenses(expenses)
        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice! Please try again.")

def add_expense(expenses):
    """Add a new expense"""
    amount = input("Enter amount: $")
    category = input("Enter category (e.g., Food, Transport, Entertainment): ")
    description = input("Enter description: ")
    
    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }
    
    expenses.append(expense)
    print(f"✓ Expense added: ${amount} - {category}")

def view_expenses(expenses):
    """View all expenses"""
    if not expenses:
        print("No expenses recorded yet!")
        return
    
    print("\n" + "="*40)
    print("YOUR EXPENSES")
    print("="*40)
    total = 0
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. ${expense['amount']} - {expense['category']}")
        print(f"   Description: {expense['description']}")
        try:
            total += float(expense['amount'])
        except:
            pass
    print("="*40)
    print(f"TOTAL: ${total:.2f}")
    print("="*40)

def delete_expense(expenses):
    """Delete an expense"""
    if not expenses:
        print("No expenses to delete!")
        return
    
    view_expenses(expenses)
    
    try:
        index = int(input("Enter the number of expense to delete: ")) - 1
        if 0 <= index < len(expenses):
            deleted = expenses.pop(index)
            print(f"✓ Deleted: ${deleted['amount']} - {deleted['category']}")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number!")

if __name__ == "__main__":
    main()