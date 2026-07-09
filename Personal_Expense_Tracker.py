expenses={
    "food":1200,
    "travel":800,
    "shopping":2500,
    "medicines":500
}
user_expenses={}
def add_expense():
    category=input("enter the category")
    amount=int(input("enter amount"))
    if category in user_expenses:
        user_expenses[category]+=amount
    else:
        user_expenses[category]=amount
           
def show_expense():
    for category,amount  in user_expenses.items():
        print(category,":",amount)

def total_expense():
    tot=sum(user_expenses.values())
    print("total expenses",tot)

def highest_expense():
    if not user_expenses:
        print("no expenses found")
        return
    max_value=max(user_expenses.values())
    for category in user_expenses:
        if user_expenses[category]==max_value:
            print("category is",category)
            print("max price or expense is",max_value)
            break
while True:
    print("personal expenses tracker")
    print("1.add expenses")
    print("2.show expenses")
    print("3.tot expenses")
    print("4.highest expenses")
    print("5.exit")
    n=int(input("enter your choice"))
    match n:
        case 1:
            add_expense()
        case 2:
            show_expense()
        case 3:
            total_expense()
        case 4:
            highest_expense()
        case 5:
            print("thank you")
            break
        case _:
            print("invalid choice")
