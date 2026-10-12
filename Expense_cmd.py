expenses=[]

while True:
    print("1.Add Expense. ")
    print("2.View Expenses. ")
    print("3.Delete Expense. ")
    print("4.Total Expense. ")
    print("5.Category Summary.")
    print("6.Exit.")

    try:
        choice = int(input("Enter your choice"))
    except ValueError:
        print("Please Enter a number!")
        continue

    if choice == 1:
        name=input("Enter expense name:- ")
        amount=float(input("Enter the amount:-"))
        category=input("Enter the category")

        expense={
            "name":name,
            "amount":amount,
            "category":category
        }

        expenses.append(expense)
        print("Expense added Successfully!")

    elif choice == 2:
        if not expenses:
            print("No expenses available")
        else :
            print("Your Expenses:")
            for i,expense in enumerate(expenses,start=1):
                print(f"{i}.{expense['name']} - ₹{expense['amount']} - {expense['category']}")