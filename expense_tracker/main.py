import expense
def show_menu():
    print("1.Add expense") 
    print("2.View all expenses") 
    print("3.Filter expenses") 
    print("4.Export to CSV")
    print("5.Exit") 
    
    


def expense_entry():
    while True:
        show_menu()
        option = input("choose an option: ")
        if option == "1":
            expense.add_expense()
        elif option == "2":
            expense.view_expenses()
        elif option == "3":
            expense.filter_expenses()
        elif option == "4":
            expense.export_csv()
        elif option == "5":
            print("Good bye")
            break
        else:
            print("Invalid option")
expense_entry()
