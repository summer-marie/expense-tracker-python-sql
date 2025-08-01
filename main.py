#!/usr/bin/env python3
"""
Expense Tracker - Phase 1: Basic Balance & Transactions
A simple command-line expense tracker for learning Python
"""

import csv
import os
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.balance_file = 'balance.txt'
        self.transactions_file = 'transactions.csv'
        self.balance = self.load_balance()
    
    def load_balance(self):
        """Load balance from file or set to 0 if file doesn't exist"""
        if os.path.exists(self.balance_file):
            with open(self.balance_file, 'r') as f:
                return float(f.read().strip())
        return 0.0
    
    def save_balance(self):
        """Save current balance to file"""
        with open(self.balance_file, 'w') as f:
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
        
        # Update balance
        self.balance += amount
        self.save_balance()
        
        # Save transaction to CSV
        file_exists = os.path.exists(self.transactions_file)
        with open(self.transactions_file, 'a', newline='') as f:
            writer = csv.writer(f)
            if not file_exists:
                # Write header if file is new
                writer.writerow(['Date', 'Description', 'Amount', 'Balance'])
            writer.writerow([date, description, amount, self.balance])
        
        transaction_type = "Income" if amount > 0 else "Expense"
        print(f"{transaction_type} added: {description} - ${abs(amount):.2f}")
        print(f"New balance: ${self.balance:.2f}")
    
    def view_transactions(self):
        """View all transactions"""
        if not os.path.exists(self.transactions_file):
            print("No transactions found.")
            return
        
        print("\n" + "="*60)
        print("TRANSACTION HISTORY")
        print("="*60)
        
        with open(self.transactions_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            
            transactions = list(reader)
            if not transactions:
                print("No transactions found.")
                return
            
            for row in transactions:
                date, description, amount, balance = row
                amount = float(amount)
                transaction_type = "+" if amount > 0 else "-"
                print(f"{date} | {description:<20} | {transaction_type}${abs(amount):>8.2f} | Balance: ${float(balance):>8.2f}")
    
    def get_balance(self):
        """Display current balance"""
        print(f"Current balance: ${self.balance:.2f}")
        return self.balance

def show_menu():
    """Display the main menu"""
    print("\n" + "="*40)
    print("💰 EXPENSE TRACKER - PHASE 1")
    print("="*40)
    print("1. Set Balance")
    print("2. Add Income")
    print("3. Add Expense")
    print("4. View Transactions")
    print("5. Check Balance")
    print("6. Exit")
    print("-"*40)

def main():
    """Main program loop"""
    tracker = ExpenseTracker()
    
    print("Welcome to your Personal Expense Tracker!")
    print("This is Phase 1: Basic Balance & Transactions")
    
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            try:
                amount = float(input("Enter initial balance: $"))
                tracker.set_balance(amount)
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '2':
            description = input("Enter income description: ")
            try:
                amount = abs(float(input("Enter income amount: $")))  # Make positive
                tracker.add_transaction(description, amount)
            except ValueError:
                print("Please enter a valid amount.")
        
        elif choice == '3':
            description = input("Enter expense description: ")
            try:
                amount = abs(float(input("Enter expense amount: $")))  # Make positive, then negative
                tracker.add_transaction(description, -amount)
            except ValueError:
                print("Please enter a valid amount.")
        
        elif choice == '4':
            tracker.view_transactions()
        
        elif choice == '5':
            tracker.get_balance()
        
        elif choice == '6':
            print("Thanks for using Expense Tracker!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
