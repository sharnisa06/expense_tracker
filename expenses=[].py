expenses=[]

def add_expense():
    category=input("enter the category")
    amount=float(input("enter the amount"))
    expense={"category":category,"amount":amount}
    expenses.append(expense)
    print("expense added successfully")

def view_all():
    if not expenses:
        print("no responses recorded yet")
        return
    print("all expenses")
    for i, expense in enumerate(expenses,start=1):
        print(f"{i}. {expense['category']} - ${expense['amount']}")
    print()

def total_spent():
    total=sum(exp["amount"]for exp in expenses)
    print(f"total:${total}")

def highest_expense():
    if not expenses:
        print("no response recorded")
        return
    max_exp=max(expenses,lambda x:x["amount"])
    print(f"highest expennse : {max_exp['category']}- $ {max_exp['amount']}")

def view_by_category():
    category=input("enter category to filter")
    filter=[exp for exp in expenses if exp["category"].lower()==category.lower()]
    if not filter:
        print("no expenses")
    else:
        print(f"expenses in {category.title()}")
        for exp in filter:
            print(f"{exp['category']-  {exp['amount']}}")
        print()

    
while True:
    print("=== PERSONAL EXPENSE TRACKER ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spent")
    print("4. View Highest Expense")
    print("5. View Expenses by Category")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_all()
    elif choice == '3':
        total_spent()
    elif choice == '4':
        highest_expense()
    elif choice == '5':
        view_by_category()
    elif choice == '6':
        print("👋 Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice! Try again.\n")
