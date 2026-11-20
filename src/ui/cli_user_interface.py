
def show_menu():
    print("1.Add expense")
    print("2.View all expenses")
    print("3.Filter expenses by category")
    print("4.Filter expenses by date")
    print("5.Export to CSV")
    print("6.Exit")


def expense_entry(expense):
    while True:
        show_menu()
        option = input("Choose an option: ")

        if option == "1":
            expense.add_expense()
        elif option == "2":
            expense.view_expenses()
        elif option == "3":
            expense.filter_expenses()
        elif option == "4":
            expense.filter_expenses_by_date()
        elif option == "5":
            expense.export_expenses()
        elif option == "6":
            print("Good bye")
            break
        else:
            print("Invalid option")
