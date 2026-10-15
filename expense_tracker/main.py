def show_menu():
    print("1.Add expense") 
    print("2.View or filter expenses") 
    print("1.Add expense") 


def expense_entry():
    while True:
        show_menu()
        option = input("choice an option: ")
        if option == "1":
            diary.add_expense()
        elif option == "2":
            diary.view_or_filter_expenses()
        elif option == "3":
            print("Good bye")
            break
        else:
            print("Invalid option")
expense_entry()
