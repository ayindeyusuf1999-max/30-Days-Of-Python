import csv
import os

FILENAME = "expenses.csv"


def load_data():
    data = {"income": 0, "fixed": [], "general": []}
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == "income":
                    data["income"] = float(row[1])
                elif row[0] == "fixed":
                    data["fixed"].append(
                        {"name": row[1], "amount": float(row[2])})
                elif row[0] == "general":
                    data["general"].append(
                        {"name": row[1], "amount": float(row[2])})
    return data


def save_data(income, fixed, general):
    with open(FILENAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["income", income])
        for e in fixed:
            writer.writerow(["fixed", e["name"], e["amount"]])
        for e in general:
            writer.writerow(["general", e["name"], e["amount"]])


def show_summary(income, fixed, general):
    total_fixed = sum(e["amount"] for e in fixed)
    total_general = sum(e["amount"] for e in general)
    balance = income - total_fixed - total_general
    print("\n========= MONTHLY SUMMARY =========")
    print("Monthly Income:           $" + str(income))
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


# Load existing data
data = load_data()
income = data["income"]
fixed_expenses = data["fixed"]
general_expenses = data["general"]

print("Welcome to your Monthly Expense Tracker!")
print("-----------------------------------------")
print("1. Add income")
print("2. Add fixed expense")
print("3. Add general expense")
print("4. Show summary")
print("5. Exit")

while True:
    choice = input("\nChoose an option (1-5): ")

    if choice == "1":
        income = float(input("Enter your monthly income: "))
    elif choice == "2":
        name = input("Enter fixed expense name: ")
        amount = float(input("Enter amount: "))
        fixed_expenses.append({"name": name, "amount": amount})
    elif choice == "3":
        name = input("Enter general expense name: ")
        amount = float(input("Enter amount: "))
        general_expenses.append({"name": name, "amount": amount})
    elif choice == "4":
        show_summary(income, fixed_expenses, general_expenses)
    elif choice == "5":
        save_data(income, fixed_expenses, general_expenses)
        print("Data saved! Goodbye!")
        break
    else:
        print("Invalid option, please choose 1-5")
