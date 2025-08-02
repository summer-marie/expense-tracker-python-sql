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
        """Add a new transaction"""
        amount = float(amount)
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Ask for notes (optional)
        notes = input(
            "Optional: Add a note for this transaction (press Enter to skip): "
        ).strip()

        # Update balance
        self.balance += amount
        self.save_balance()

        # Save transaction to CSV
        file_exists = os.path.exists(self.transactions_file)
        with open(self.transactions_file, "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                # Write header if file is new
                writer.writerow(["Date", "Description", "Amount", "Balance", "Notes"])
            writer.writerow([date, description, amount, self.balance, notes])

        transaction_type = "Income" if amount > 0 else "Expense"
        print(f"{transaction_type} added: {description} - ${abs(amount):.2f}")
        print(f"New balance: ${self.balance:.2f}")

    # VIEWING TRANSACTIONS METHOD - Like displaying a list in React
    def view_transactions(self):
        """View all transactions"""
        # Check if the CSV file exists (similar to checking if data exists)
        if not os.path.exists(self.transactions_file):
            print("No transactions found.")
            return  # Exit the function early (like early return in React)

        # PRETTY PRINTING - Like styling output in console
        # "\n" = new line character (like <br/> in HTML)
        # "="*60 = repeat "=" 60 times (creates a line separator)
        print("\n" + "=" * 60)
        print("TRANSACTION HISTORY")
        print("=" * 60)

        # CSV READING - Like fetching and parsing JSON data
        with open(self.transactions_file, "r") as f:
            reader = csv.reader(f)  # Creates a CSV reader object
            next(reader)  # Skip the first row (header row with column names)

            # Convert CSV reader to a list (like spreading data in React)
            transactions = list(reader)
            if not transactions:  # If list is empty (like checking array.length === 0)
                print("No transactions found.")
                return

            # FOR LOOP - Like .map() in React but for console output
            # for item in array: is like array.map((item) => { ... })
            for row in transactions:
                # DESTRUCTURING - Like const [date, desc, amount] = row in JS
                date, description, amount, balance, notes = row
                amount = float(amount)  # Convert string to number

                # TERNARY OPERATOR - Same as JavaScript ? : operator
                transaction_type = "+" if amount > 0 else "-"

                # F-STRING FORMATTING - Like template literals in JS
                # f"{variable}" is like `${variable}` in JavaScript
                # :<20 means left-align in 20 characters (like CSS text-align)
                # :>8.2f means right-align, 8 chars wide, 2 decimal places
                print(
                    f"{date} | {description:<20} | {transaction_type}${abs(amount):>8.2f} | Balance: ${float(balance):>8.2f}"
                )

                # CONDITIONAL PRINTING - Only show notes if they exist
                if notes:  # In Python, empty string is "falsy" (like in JS)
                    print(f"    Notes: {notes}")  # Indented for better formatting

    def get_balance(self):
        """Display current balance"""
        print(f"Current balance: ${self.balance:.2f}")
        return self.balance


# STANDALONE FUNCTION - Like a utility function outside of React components
# This is NOT inside the ExpenseTracker class (no 'self' parameter)
def show_menu():
    """Display the main menu"""
    # UI DISPLAY - Like rendering JSX but for console
    print("\n" + "=" * 40)  # New line + separator (like <hr/> in HTML)
    print("💰 EXPENSE TRACKER - PHASE 1")
    print("=" * 40)
    print("1. Set Balance")  # Menu options (like buttons in React)
    print("2. Add Income")
    print("3. Add Expense")
    print("4. View Transactions")
    print("5. Check Balance")
    print("6. Exit")
    print("-" * 40)  # Bottom separator


# MAIN FUNCTION - Like your App() component in React
# This is the entry point that runs everything
def main():
    """Main program loop"""
    # CREATE INSTANCE - Like const [tracker] = useState(new ExpenseTracker())
    tracker = ExpenseTracker()  # Create new expense tracker object

    # WELCOME MESSAGE - Like initial render in React
    print("Welcome to your Personal Expense Tracker!")
    print("This is Phase 1: Basic Balance & Transactions")

    # INFINITE LOOP - Like having an always-running React app
    # while True: = keep running forever until user chooses to exit
    while True:
        show_menu()  # Display menu (like rendering UI)

        # USER INPUT - Like handling form input in React
        # input() waits for user to type something and press Enter
        choice = input("Choose an option (1-6): ").strip()  # Remove extra spaces

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

        elif choice == "6":  # Exit option
            print("Thanks for using Expense Tracker!")
            break  # EXIT THE LOOP - Like closing a React app

        else:  # Invalid choice (user entered something other than 1-6)
            print("Invalid choice. Please try again.")
            # Loop continues, menu shows again


# PYTHON ENTRY POINT - Like ReactDOM.render() in React apps
# This is a Python idiom that means "only run this if file is executed directly"
# In React terms: this is like your index.js that starts the whole app
if __name__ == "__main__":
    main()  # Start the application by calling main function
