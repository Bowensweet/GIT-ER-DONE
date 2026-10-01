expenses = []

# Collect expenses until the user enters 0
while True:
    amount = float(input("Enter an expense or 0 to finish: $"))
    if amount > 0:
        expenses.append(amount)
    elif amount == 0:
        break
    else:
        print("Expense cannot be negative. Please enter a valid amount.")
        

small_count = 0
moderate_count = 0
large_count = 0

    # Classify each expense
for expense in expenses:
    if expense < 25:
            category = "Small expense"
            small_count += 1
    elif expense <= 100:
            category = "Moderate expense"
            moderate_count += 1
    else:
            category = "Large expense"
            large_count += 1

    # Calculations
count = len(expenses)
total = sum(expenses)
average = total / count
smallest = min(expenses)
largest = max(expenses)

    # Print results
print()
print("Expense summary:")
print("----------------")
print(f"Total number of expenses: {count}")
print(f"Total expenses: ${total:,.2f}")
print(f"Average expense: ${average:,.2f}")
print(f"Smallest expense: ${smallest:,.2f}")
print(f"Largest expense: ${largest:,.2f}")
print(f"Small expenses: {small_count}")
print(f"Moderate expenses: {moderate_count}")
print(f"Large expenses: {large_count}")