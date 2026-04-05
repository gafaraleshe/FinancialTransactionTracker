# Financial Transaction Tracker
# By Gafar Aleshe
# This program allows users to track income and expenses,
# view transaction summaries, and manage their finances.

# --- Data Structure ---
# Transactions are stored as a list of dictionaries.
# Each dictionary holds the type, amount, category, and date of a transaction.
transactions = []

# --- Predefined Categories ---
# These lists define valid categories the user can choose from.
income_categories = ["salary", "freelance", "investment", "gift", "other"]
expense_categories = ["rent", "groceries", "utilities", "transport", "entertainment", "other"]


# --- Functions ---

def add_transaction():
    """Prompts the user to enter a new income or expense transaction."""
    print("\n--- Add Transaction ---")

    # Step 1: Choose transaction type
    while True:
        trans_type = input("Type (income/expense): ").strip().lower()
        if trans_type in ["income", "expense"]:
            break
        print("Invalid type. Please enter 'income' or 'expense'.")

    # Step 2: Choose a category based on the transaction type
    if trans_type == "income":
        categories = income_categories
    else:
        categories = expense_categories

    print("Categories:", ", ".join(categories))
    while True:
        category = input("Choose a category: ").strip().lower()
        if category in categories:
            break
        print("Invalid category. Please choose from the list above.")

    # Step 3: Enter the amount with validation
    while True:
        try:
            amount = float(input("Enter amount (£): "))
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Step 4: Enter the date with basic validation
    while True:
        date = input("Enter date (DD/MM/YYYY): ").strip()
        if len(date) == 10 and date[2] == "/" and date[5] == "/":
            break
        print("Invalid format. Please use DD/MM/YYYY.")

    # Step 5: Create the transaction dictionary and add it to the list
    transaction = {
        "type": trans_type,
        "category": category,
        "amount": amount,
        "date": date
    }
    transactions.append(transaction)
    print(f"\n{trans_type.capitalize()} of £{amount:.2f} added under '{category}'.")


def view_transactions():
    """Displays all transactions or filters them by category."""
    print("\n--- View Transactions ---")

    # Check if there are any transactions to display
    if len(transactions) == 0:
        print("No transactions recorded yet.")
        return

    # Ask the user if they want to filter by category
    filter_choice = input("Filter by category? (yes/no): ").strip().lower()

    if filter_choice == "yes":
        # Collect and display all categories currently used in transactions
        used_categories = []
        for t in transactions:
            if t["category"] not in used_categories:
                used_categories.append(t["category"])
        print("Available categories:", ", ".join(used_categories))

        category = input("Enter category name: ").strip().lower()
        # Use a loop to find matching transactions
        filtered = []
        for t in transactions:
            if t["category"] == category:
                filtered.append(t)

        if len(filtered) == 0:
            print(f"No transactions found under '{category}'.")
            return
        display_list = filtered
    else:
        display_list = transactions

    # Display each transaction in a readable format
    print(f"\n{'Type':<10} {'Category':<15} {'Amount (£)':<12} {'Date':<12}")
    print("-" * 49)
    for t in display_list:
        print(f"{t['type']:<10} {t['category']:<15} {t['amount']:<12.2f} {t['date']:<12}")


def delete_transaction():
    """Allows the user to delete a transaction by selecting its number."""
    print("\n--- Delete Transaction ---")

    # Check if there are any transactions to delete
    if len(transactions) == 0:
        print("No transactions to delete.")
        return

    # Display all transactions with numbered indices
    for i in range(len(transactions)):
        t = transactions[i]
        print(f"{i + 1}. {t['type']} | {t['category']} | £{t['amount']:.2f} | {t['date']}")

    # Ask the user which transaction to delete
    while True:
        try:
            choice = int(input("Enter the number of the transaction to delete: "))
            if 1 <= choice <= len(transactions):
                break
            else:
                print(f"Please enter a number between 1 and {len(transactions)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Remove the selected transaction from the list
    removed = transactions.pop(choice - 1)
    print(f"Deleted: {removed['type']} | {removed['category']} | £{removed['amount']:.2f}")


def calculate_total_income():
    """Calculates and returns the total of all income transactions."""
    total = 0
    for t in transactions:
        if t["type"] == "income":
            total += t["amount"]
    return total


def calculate_total_expenses():
    """Calculates and returns the total of all expense transactions."""
    total = 0
    for t in transactions:
        if t["type"] == "expense":
            total += t["amount"]
    return total


def calculate_balance():
    """Calculates the remaining balance (total income minus total expenses)."""
    return calculate_total_income() - calculate_total_expenses()


def highest_expense_category():
    """Finds and returns the expense category with the highest total spending."""
    # Dictionary to accumulate totals per category
    category_totals = {}
    for t in transactions:
        if t["type"] == "expense":
            if t["category"] in category_totals:
                category_totals[t["category"]] += t["amount"]
            else:
                category_totals[t["category"]] = t["amount"]

    if len(category_totals) == 0:
        return None, 0

    # Find the category with the maximum total
    highest_cat = ""
    highest_amount = 0
    for category, amount in category_totals.items():
        if amount > highest_amount:
            highest_cat = category
            highest_amount = amount

    return highest_cat, highest_amount


def lowest_expense_category():
    """Finds and returns the expense category with the lowest total spending."""
    # Dictionary to accumulate totals per category
    category_totals = {}
    for t in transactions:
        if t["type"] == "expense":
            if t["category"] in category_totals:
                category_totals[t["category"]] += t["amount"]
            else:
                category_totals[t["category"]] = t["amount"]

    if len(category_totals) == 0:
        return None, 0

    # Find the category with the minimum total
    lowest_cat = ""
    lowest_amount = float("inf")
    for category, amount in category_totals.items():
        if amount < lowest_amount:
            lowest_cat = category
            lowest_amount = amount

    return lowest_cat, lowest_amount


def display_summary():
    """Displays a financial summary including totals, balance, and category insights."""
    print("\n--- Financial Summary ---")

    total_income = calculate_total_income()
    total_expenses = calculate_total_expenses()
    balance = calculate_balance()

    print(f"Total Income:   £{total_income:.2f}")
    print(f"Total Expenses: £{total_expenses:.2f}")
    print(f"Balance:        £{balance:.2f}")

    # Display highest and lowest expense categories if expenses exist
    highest_cat, highest_amount = highest_expense_category()
    lowest_cat, lowest_amount = lowest_expense_category()

    if highest_cat:
        print(f"\nHighest Expense: {highest_cat} (£{highest_amount:.2f})")
        print(f"Lowest Expense:  {lowest_cat} (£{lowest_amount:.2f})")
    else:
        print("\nNo expense data available yet.")


# --- Main Menu ---
# This loop keeps the program running until the user chooses to exit.

def main():
    """Main function that runs the menu-driven program loop."""
    print("=" * 40)
    print("   Financial Transaction Tracker")
    print("=" * 40)

    while True:
        # Display the menu options
        print("\n--- Main Menu ---")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Delete Transaction")
        print("4. View Summary")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        # Control flow to direct the user to the correct function
        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            delete_transaction()
        elif choice == "4":
            display_summary()
        elif choice == "5":
            print("\nThank you for using the Financial Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5.")


# Run the program
main()