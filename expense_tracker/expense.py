import json
def add_expense():
    Date = input("Add date: ")
    Category = input("Add Category: ")
    Description = input("what was the espense: ")
    Amount = input("Add Amount: ")

    new_expense = {
        "date" : Date,
        "category" : Category,
        "description" : Description,
        "amount" : float(Amount)
    }
    print(new_expense)
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

    expenses.append(new_expense)

    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
