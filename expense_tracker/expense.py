import json
import csv
def add_expense():
    Date = input("Add date: ")
    Category = input("Add Category(Food, Rent, Transportation, Bills, Others): ")
    Description = input("What did you buy or pay for? ")
    Amount = input("What was the Amount: ")

    new_expense = {
        "date" : Date,
        "category" : Category,
        "description" : Description,
        "amount" : float(Amount)
    }
    print("Date:", new_expense["date"])
    print("Category:", new_expense["category"])
    print("Description:", new_expense["description"])
    print("Amount:", new_expense["amount"])
    
    
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

    expenses.append(new_expense)

    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def view_expenses():
    
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

    if expenses:
        print(expenses)
    else:
        print("No expenses found.")


def filter_expenses():
    category_to_find= input("Which category do you want to find (Food, Rent, Transportation, Bills, Others)?: ")
    
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

    matching_expenses = []

    for saved_expense in expenses:
        if saved_expense["category"] == category_to_find:
            matching_expenses.append(saved_expense)

    
    if matching_expenses:
        for saved_expense in matching_expenses:
            print("Date:", saved_expense["date"])
            print("Category:", saved_expense["category"])
            print("Description:", saved_expense["description"])
            print("Amount:", saved_expense["amount"])
            print()
    else:
        print("No expenses found for that category.")
    

def export_expenses():
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

    if expenses:
        with open("expenses.csv", "w", newline="") as file:
            exporter = csv.writer(file)

            exporter.writerow(["date", "category", "description", "amount"])

            for saved_expense in expenses:
                exporter.writerow([
                    saved_expense["date"],
                    saved_expense["category"],
                    saved_expense["description"],
                    saved_expense["amount"]
                ])

        print("Expenses exported to expenses.csv.")
    else:
        print("No expenses to export.")