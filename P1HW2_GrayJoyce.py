# Joyce Gray
# April 6, 2026
# P1HW2
# Planning a budget usin addition and subtraction

print("------Travel Budget------")
print()
budget = int(input("Enter Budget Amount: "))
Travel = input("Travel Destination: ")

gas = int(input("Enter amount spent on gas: "))
lodging = int(input("Enter amount spent on lodging: "))
food = int(input("Enter amount spent on food: "))

# Calculate Total Expenses
total_expenses = gas + lodging + food
cash_leftover = budget - total_expenses

print("total_expenses =", gas, "+", lodging, "+", food, "is equal to", total_expenses, "!!!") 
print("cash_leftover =", budget, "-", total_expenses, "is equal to", cash_leftover, "YOU ARE BROKE")


# Pseudocode Block
# Destination and budget for trip
# Start with entering a budget
# Insert destination
# Estimate cost for gas, loding and food.
