#Travel expenses Part 2
#9-15-23
#CTI-110 P2HW1 - Travel Expenses Part 2
# Tyrique Lawrence
####################
budget = float(input("Enter your budget: "))
destination = input("Enter your travel destination: ")
gas_expenses = float(input("Enter the amount you will spend on gas: "))
accommodation_expenses = float(input("Enter the amount you will spend on accommodation: "))
food_expenses = float(input("Enter the amount you will spend on food: "))

total_expenses = gas_expenses + accommodation_expenses + food_expenses
remaining_budget = budget - total_expenses

print("Results")
print("Destination:", destination)
print("Total Expenses:", total_expenses)
print("Accomodtion Expenses:", accommodation_expenses)
print("food Expenses:", food_expenses)
print("Remaining Budget:", remaining_budget)
