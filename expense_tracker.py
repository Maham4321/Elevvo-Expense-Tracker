import json
import os

DATA_FILE = "expenses.json"

def load_expenses():
    """Load existing expenses from the local JSON file on startup."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_expenses(expenses):
    """Save expenses list to the local JSON file for persistence."""
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    """Accept user input and add a new expense entry."""
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (e.g., Food, Transport, Bills): ").strip()
        date = input("Enter date (YYYY-MM-DD): ").strip()
        
        expense = {
            "amount": amount,
            "category": category,
            "date": date
        }
        expenses.append(expense)
        save_expenses(expenses)
        print("✅ Expense added successfully and saved to file!")
    except ValueError:
        print("❌ Invalid input for amount. Please enter a valid number.")

def view_expenses(expenses):
    """Display all recorded expenses."""
    if not expenses:
        print("ℹ️ No expenses recorded yet.")
        return
    
    print("\n--- All Expenses ---")
    for idx, exp in enumerate(expenses, 1):
        print(f"{idx}. Date: {exp['date']} | Category: {exp['category']} | Amount: ${exp['amount']:.2f}")

def monthly_summary(expenses):
    """Bonus: Generate a monthly summary report with sum and average per category using f-strings."""
    if not expenses:
        print("ℹ️ No expenses available for summary.")
        return
        
    month = input("Enter month to summarize (YYYY-MM): ").strip()
    filtered = [exp for exp in expenses if exp['date'].startswith(month)]
    
    if not filtered:
        print(f"ℹ️ No expenses found for {month}.")
        return

    total_sum = sum(exp['amount'] for exp in filtered)
    categories = {}
    
    for exp in filtered:
        cat = exp['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(exp['amount'])

    print(f"\n--- Monthly Summary Report ({month}) ---")
    print(f"Total Spent: ${total_sum:.2f}")
    print("Category Breakdown:")
    for cat, amounts in categories.items():
        cat_total = sum(amounts)
        cat_avg = cat_total / len(amounts)
        print(f"  * {cat}: Total = ${cat_total:.2f} | Average = ${cat_avg:.2f}")

def main():
    expenses = load_expenses()
    while True:
        print("\n=== CLI Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Monthly Summary Report (Bonus)")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            monthly_summary(expenses)
        elif choice == '4':
            print("👋 Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please choose between 1 and 4.")

if __name__ == "__main__":
    main()