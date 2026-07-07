# Project 2: Expense Tracker - DecodeLabs
# By: Yasra Shabir

expenses = []
total = 0  # Accumulator - loop se BAHAR!

def add_expense():
    global total
    while True:
        entry = input("\nEnter expense amount (or 'quit' to stop): ")
        if entry.lower() == 'quit':
            break
        try:
            amount = float(entry)
            expenses.append(amount)
            total += amount  # Accumulator pattern
            print(f"✅ Added: Rs.{amount:.2f} | Running Total: Rs.{total:.2f}")
        except ValueError:
            print("❌ Invalid! Please enter a number.")

def view_expenses():
    if len(expenses) == 0:
        print("📊 No expenses recorded!")
    else:
        print("\n📊 Expense List:")
        for index, exp in enumerate(expenses, start=1):
            print(f"  {index}. Rs.{exp:.2f}")
        print(f"\n💰 TOTAL SPENT: Rs.{total:.2f}")

def main():
    print("🚀 Welcome to DecodeLabs Expense Tracker!\n")
    while True:
        print("1. Add Expenses")
        print("2. View All Expenses")
        print("3. Exit")
        choice = input("\nEnter choice (1/2/3): ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print(f"\n💰 Final Total: Rs.{total:.2f}")
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()