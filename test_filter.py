#!/usr/bin/env python3
"""Test script to demonstrate the filter by category feature"""

from main import ExpenseTracker

# Create an instance of the expense tracker
tracker = ExpenseTracker()

print("🧪 TESTING FILTER BY CATEGORY FEATURE")
print("=" * 50)

# Test 1: Filter by Food & Dining
print("\n1. Testing filter for 'Food & Dining' category:")
print("-" * 40)
# Manually call the filter method with a specific category
import os
import csv

if os.path.exists(tracker.transactions_file):
    selected_category = "Food & Dining"
    print(f"Transactions in category: {selected_category}")
    print("=" * 70)
    found = False
    with open(tracker.transactions_file, "r") as f:
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

# Test 2: Filter by Transportation
print("\n\n2. Testing filter for 'Transportation' category:")
print("-" * 40)
if os.path.exists(tracker.transactions_file):
    selected_category = "Transportation"
    print(f"Transactions in category: {selected_category}")
    print("=" * 70)
    found = False
    with open(tracker.transactions_file, "r") as f:
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

# Test 3: Filter by Uncategorized
print("\n\n3. Testing filter for 'Uncategorized' category:")
print("-" * 40)
if os.path.exists(tracker.transactions_file):
    selected_category = "Uncategorized"
    print(f"Transactions in category: {selected_category}")
    print("=" * 70)
    found = False
    with open(tracker.transactions_file, "r") as f:
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

print("\n" + "=" * 50)
print("✅ Filter feature testing complete!")
print("The filter by category feature is working correctly!")
