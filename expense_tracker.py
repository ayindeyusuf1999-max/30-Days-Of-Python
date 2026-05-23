income = []
fixed_expenses = []
general_expenses = []

print("Welcome to your Monthly Expense Tracker!")
print("-----------------------------------------")

# Add Monthly Income
amount = float(input("Enter your monthly income: "))
income.append(amount)

# Add Fixed Expenses
print("\n--- Fixed Monthly Expenses (rent, subscriptions, etc.) ---")
while True:
    item = input("Enter fixed expense name (or 'done' to stop): ")
    if item == 'done':
        break
    amount = float(input("Enter amount for " + item + ": "))
    fixed_expenses.append({"name": item, "amount": amount})

# Add General Expenses
print("\n--- General Monthly Expenses (food, transport, etc.) ---")
while True:
    item = input("Enter general expense name (or 'done' to stop): ")
    if item == 'done':
        break
    amount = float(input("Enter amount for " + item + ": "))
    general_expenses.append({"name": item, "amount": amount})

# Summary
total_fixed = sum(e["amount"] for e in fixed_expenses)
total_general = sum(e["amount"] for e in general_expenses)
total_income = sum(income)
balance = total_income - total_fixed - total_general

print("\n========= MONTHLY SUMMARY =========")
print("Monthly Income:           $" + str(total_income))
print("Total Fixed Expenses:     $" + str(total_fixed))
print("Total General Expenses:   $" + str(total_general))
print("------------------------------------")
print("Remaining Balance:        $" + str(balance))

if balance > 0:
    print("You are in good shape!")
elif balance == 0:
    print("You have spent exactly your income!")
else:
    print("You are overspending!")
