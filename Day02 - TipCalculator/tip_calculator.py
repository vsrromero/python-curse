"""Tip Calculator"""

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $\n"))
people = int(input("How many people to split the bill?\n"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))

print(f"Each person should pay: ${round((bill + (bill * (tip / 100))) / people, 2)}")
