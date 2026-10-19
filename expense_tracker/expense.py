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

add_expense()
