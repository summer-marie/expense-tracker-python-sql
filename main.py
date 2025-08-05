#!/usr/bin/env python3
"""
This is called a "docstring" - like JSDoc comments in JavaScript
It describes what this file does at the top level
Expense Tracker - Phase 1: Basic Balance & Transactions
A simple command-line expense tracker for learning Python
"""

# IMPORTS - Similar to "import React from 'react'" in JSX
# These bring in built-in Python modules (like importing libraries)
import csv  # For reading/writing CSV files (like a spreadsheet)
import os  # For file system operations (checking if files exist)
from datetime import datetime  # For getting current date/time


# CLASS DEFINITION - Similar to creating a React component
# In React: const ExpenseTracker = () => { ... }
# In Python: class ExpenseTracker:
class ExpenseTracker:
    # CONSTRUCTOR - Like useState hooks in React for initial setup
    # This runs automatically when you create a new ExpenseTracker
    # In React: const [balance, setBalance] = useState(0)
    def __init__(self):
        # These are instance variables (like state in React)
        # self.variable_name is like this.variableName in JavaScript classes
        self.balance_file = "balance.txt"  # Filename to store balance
        self.transactions_file = "transactions.csv"  # Filename to store transactions
        self.balance = self.load_balance()  # Load existing balance or start at 0

        # PHASE 2: CATEGORIES - Like having a predefined array in React
        # LIST DATA STRUCTURE - Similar to const categories = [...] in JavaScript
        self.categories = [
            "Food & Dining",  # Restaurants, groceries, takeout
            "Transportation",  # Gas, parking, public transit
            "Entertainment",  # Movies, games, hobbies
            "Bills & Utilities",  # Rent, electricity, phone
            "Shopping",  # Clothes, household items
            "Healthcare",  # Doctor visits, pharmacy
            "Income",  # Salary, freelance, gifts received
            "Other",  # Miscellaneous expenses
        ]

    # PHASE 2: RESET FUNCTION - Like clearing all state in React
    def reset_tracker(self):
        """Reset balance to 0 and delete all transactions"""
        # Reset balance to 0 (like setBalance(0) in React)
        self.balance = 0.0
        self.save_balance()  # Save the reset balance to file

        # DELETE TRANSACTIONS FILE - Like clearing an array in React
        # os.path.exists() checks if file exists before trying to delete
        if os.path.exists(self.transactions_file):
            os.remove(self.transactions_file)  # Delete the CSV file completely

        print("✅ Tracker reset! Balance: $0.00, All transactions deleted.")

    # METHOD DEFINITION - Like a function inside a React component
    # def = "define function" (like const functionName = () => {} in JSX)
    # self = similar to "this" in JavaScript classes
    def load_balance(self):
        """Load balance from file or set to 0 if file doesn't exist"""

        # IF STATEMENT - Same logic as JavaScript if/else
        # os.path.exists() checks if file exists (like checking if a variable exists)
        if os.path.exists(self.balance_file):
            # FILE READING - Like fetch() in JavaScript but for local files
            # with open() automatically closes the file when done (good practice)
            with open(self.balance_file, "r") as f:  # 'r' = read mode
                # Read the file content and convert string to number
                # .strip() removes whitespace (like .trim() in JavaScript)
                # float() converts string to decimal number (like parseFloat() in JS)
                return float(f.read().strip())

        # If file doesn't exist, return 0 (default balance)
        return 0.0  # The .0 makes it explicitly a decimal number

    # PHASE 2: CATEGORY SELECTION METHOD - Like a dropdown component in React
    def show_categories(self):
        """Display available categories and get user selection"""
        print("\n" + "=" * 30)
        print("📁 SELECT CATEGORY")
        print("=" * 30)

        # ENUMERATE FUNCTION - Like .map() with index in React
        # enumerate(list) gives you (index, item) pairs
        # In React: categories.map((cat, index) => ...)
        for index, category in enumerate(self.categories, 1):  # Start numbering from 1
            print(f"{index}. {category}")
        print("-" * 30)

        # INPUT VALIDATION LOOP - Like form validation in React
        while True:
            try:
                # Get user choice and convert to integer
                choice = int(input("Choose category (number): "))

                # CHECK IF VALID CHOICE - Like validating form input
                # Python lists are 0-indexed, but we showed 1-indexed to user
                if 1 <= choice <= len(self.categories):
                    selected_category = self.categories[
                        choice - 1
                    ]  # Convert back to 0-indexed
                    print(f"✅ Selected: {selected_category}")
                    return selected_category  # Return the chosen category string
                else:
                    print(
                        f"❌ Please enter a number between 1 and {len(self.categories)}"
                    )

            except ValueError:  # If user enters non-number (like "abc")
                print("❌ Please enter a valid number")
                # Loop continues, asking again

    def save_balance(self):
        """Save current balance to file"""
        # This method writes the current balance to the balance file
        # 'w' = write mode (overwrites existing file)
        with open(self.balance_file, "w") as f:
            # Write the balance as a string to the file
            # str() converts the number to a string (like toString() in JS)
            f.write(str(self.balance))

    def set_balance(self, amount):
        """Set initial balance"""
        self.balance = float(amount)
        self.save_balance()
        print(f"Balance set to ${self.balance:.2f}")

    def add_transaction(self, description, amount):
        """Add a new transaction with category selection"""
        amount = float(amount)
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # PHASE 2: CATEGORY SELECTION - Like calling a dropdown component in React
        # Call our show_categories method to get user's choice
        print("\n🏷️  Please select a category for this transaction:")
        selected_category = self.show_categories()  # Returns the chosen category string

        # Ask for notes (optional)
        notes = input(
            "Optional: Add a note for this transaction (press Enter to skip): "
        ).strip()

        # Update balance
        self.balance += amount
        self.save_balance()

        # PHASE 2: UPDATED CSV STRUCTURE - Now includes Category column
        # Save transaction to CSV with category
        file_exists = os.path.exists(self.transactions_file)
        with open(self.transactions_file, "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                # UPDATED HEADER - Now includes "Category" column
                # Like adding a new field to a database table
                writer.writerow(
                    ["Date", "Description", "Amount", "Balance", "Category", "Notes"]
                )

            # UPDATED ROW DATA - Now includes the selected category
            # In React terms: saving {...transaction, category: selectedCategory}
            writer.writerow(
                [date, description, amount, self.balance, selected_category, notes]
            )

        transaction_type = "Income" if amount > 0 else "Expense"
        # ENHANCED OUTPUT - Show category in confirmation message
        print(f"{transaction_type} added: {description} - ${abs(amount):.2f}")
        print(f"Category: {selected_category}")  # Show which category was selected
        print(f"New balance: ${self.balance:.2f}")

    # VIEWING TRANSACTIONS METHOD - Like displaying a list in React
    def view_transactions(self):
        """View all transactions with categories"""
        # Check if the CSV file exists (similar to checking if data exists)
        if not os.path.exists(self.transactions_file):
            print("No transactions found.")
            return  # Exit the function early (like early return in React)

        # PRETTY PRINTING - Like styling output in console
        # "\n" = new line character (like <br/> in HTML)
        # "="*70 = repeat "=" 70 times (wider for category column)
        print("\n" + "=" * 70)
        print("TRANSACTION HISTORY")
        print("=" * 70)

        # CSV READING - Like fetching and parsing JSON data
        with open(self.transactions_file, "r") as f:
            reader = csv.reader(f)  # Creates a CSV reader object
            header = next(reader)  # Read the first row (header row)

            # BACKWARDS COMPATIBILITY - Handle old CSV format without categories
            # Check if this is old format (5 columns) or new format (6 columns)
            has_categories = len(header) == 6  # New format has 6 columns

            # Convert CSV reader to a list (like spreading data in React)
            transactions = list(reader)
            if not transactions:  # If list is empty (like checking array.length === 0)
                print("No transactions found.")
                return

            # FOR LOOP - Like .map() in React but for console output
            # for item in array: is like array.map((item) => { ... })
            for row in transactions:
                # CONDITIONAL DESTRUCTURING - Handle both old and new CSV formats
                # Like handling optional props in React components
                if has_categories and len(row) == 6:
                    # NEW FORMAT: Date, Description, Amount, Balance, Category, Notes
                    date, description, amount, balance, category, notes = row
                else:
                    # OLD FORMAT: Date, Description, Amount, Balance, Notes (no category)
                    date, description, amount, balance, notes = row[
                        :5
                    ]  # Take first 5 elements
                    category = "Uncategorized"  # Default category for old transactions

                amount = float(amount)  # Convert string to number

                # TERNARY OPERATOR - Same as JavaScript ? : operator
                transaction_type = "+" if amount > 0 else "-"

                # ENHANCED F-STRING FORMATTING - Now includes category
                # f"{variable}" is like `${variable}` in JavaScript
                # :<15 means left-align in 15 characters (like CSS text-align)
                print(
                    f"{date} | {description:<15} | {category:<12} | {transaction_type}${abs(amount):>7.2f} | Balance: ${float(balance):>8.2f}"
                )

                # CONDITIONAL PRINTING - Only show notes if they exist
                if notes:  # In Python, empty string is "falsy" (like in JS)
                    print(f"    Notes: {notes}")  # Indented for better formatting

    def get_balance(self):
        """Display current balance"""
        print(f"Current balance: ${self.balance:.2f}")
        return self.balance

    def filter_transactions_by_category(self):
        """Display only transactions matching a selected category"""
        selected_category = self.show_categories()
        if not os.path.exists(self.transactions_file):
            print("No transactions found.")
            return

        print(f"\nTransactions in category: {selected_category}")
        print("=" * 70)
        found = False
        with open(self.transactions_file, "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            has_categories = len(header) == 6
            for row in reader:
                if has_categories and len(row) == 6:
                    date, description, amount, balance, category, notes = row
                else:
                    date, description, amount, balance, notes = row[:5]
                    category = "Uncategorized"
                if category == selected_category:
                    found = True
                    amount = float(amount)
                    transaction_type = "+" if amount > 0 else "-"
                    print(f"{date} | {description:<15} | {category:<12} | {transaction_type}${abs(amount):>7.2f} | Balance: ${float(balance):>8.2f}")
                    if notes:
                        print(f"    Notes: {notes}")
        if not found:
            print("No transactions found for this category.")


# STANDALONE FUNCTION - Like a utility function outside of React components
# This is NOT inside the ExpenseTracker class (no 'self' parameter)
def show_menu():
    """Display the main menu"""
    # UI DISPLAY - Like rendering JSX but for console
    print("\n" + "=" * 40)  # New line + separator (like <hr/> in HTML)
    print("💰 EXPENSE TRACKER - PHASE 2")
    print("=" * 40)
    print("1. Set Balance")  # Menu options (like buttons in React)
    print("2. Add Income")
    print("3. Add Expense")
    print("4. View Transactions")
    print("5. Check Balance")
    print("6. Reset Tracker")  # NEW: Reset option
    print("7. Filter by Category")  # NEW: Filter option
    print("8. Exit")
    print("-" * 40)  # Bottom separator


# MAIN FUNCTION - Like your App() component in React
# This is the entry point that runs everything
def main():
    """Main program loop"""
    # CREATE INSTANCE - Like const [tracker] = useState(new ExpenseTracker())
    tracker = ExpenseTracker()  # Create new expense tracker object

    # WELCOME MESSAGE - Like initial render in React
    print("Welcome to your Personal Expense Tracker!")
    print("This is Phase 2: Categories & Organization")

    # INFINITE LOOP - Like having an always-running React app
    # while True: = keep running forever until user chooses to exit
    while True:
        show_menu()  # Display menu (like rendering UI)

        # USER INPUT - Like handling form input in React
        # input() waits for user to type something and press Enter
        choice = input("Choose an option (1-8): ").strip()  # Remove extra spaces

        # SWITCH-LIKE LOGIC - Like switch statement or if/else chain in JS
        # Python uses if/elif/else instead of switch/case

        if choice == "1":  # Set Balance option
            # TRY/CATCH BLOCK - Same concept as JavaScript try/catch
            try:
                amount = float(input("Enter initial balance: $"))  # Get user input
                tracker.set_balance(amount)  # Call method on our tracker object
            except ValueError:  # If user enters invalid number (like "abc")
                print("Please enter a valid number.")  # Error handling

        elif choice == "2":  # Add Income option
            description = input("Enter income description: ")  # Get description first
            try:
                # abs() makes sure amount is positive (remove negative sign if user enters it)
                amount = abs(float(input("Enter income amount: $")))
                tracker.add_transaction(description, amount)  # Positive amount = income
            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "3":  # Add Expense option
            description = input("Enter expense description: ")
            try:
                # Get positive number, then make it negative for expense
                amount = abs(float(input("Enter expense amount: $")))
                tracker.add_transaction(
                    description, -amount
                )  # Negative amount = expense
            except ValueError:
                print("Please enter a valid amount.")

        elif choice == "4":  # View Transactions
            tracker.view_transactions()  # Call method to display all transactions

        elif choice == "5":  # Check Balance
            tracker.get_balance()  # Display current balance

        elif choice == "6":  # Reset Tracker option
            # CONFIRMATION - Like a confirm dialog in React
            confirm = (
                input("⚠️  Are you sure you want to reset all data? (y/N): ")
                .strip()
                .lower()
            )
            if confirm == "y" or confirm == "yes":
                tracker.reset_tracker()
            else:
                print("Reset cancelled.")

        elif choice == "7":  # Filter by Category option
            print("\n" + "=" * 50)
            tracker.filter_transactions_by_category()  # Call method to filter transactions by category

        elif choice == "8":  # Exit option
            print("Thanks for using Expense Tracker!")
            break  # EXIT THE LOOP - Like closing a React app

        else:  # Invalid choice (user entered something other than 1-7)
            print("Invalid choice. Please try again.")
            # Loop continues, menu shows again


# PYTHON ENTRY POINT - Like ReactDOM.render() in React apps
# This is a Python idiom that means "only run this if file is executed directly"
# In React terms: this is like your index.js that starts the whole app
if __name__ == "__main__":
    main()  # Start the application by calling main function
