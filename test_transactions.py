#!/usr/bin/env python3
"""
Quick test script to check view_transactions functionality
"""

from main import ExpenseTracker

# Create tracker instance
tracker = ExpenseTracker()

print("Testing view_transactions method:")
print("=" * 50)

# Call view_transactions directly
tracker.view_transactions()

print("\n" + "=" * 50)
print("Test complete!")
