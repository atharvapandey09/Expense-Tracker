from datetime import date
import json
import os

FILENAME = "expenses.json"


# ---------- File Handling ----------

def load_expenses():
    """
    
    """

    try:
        with open(FILENAME) as f:
            expenses_data = json.load(f)
        return expenses_data
    except(FileNotFoundError,json.JSONDecodeError):
        return []
        
def save_expenses(expenses):
    """
    
    """
    try:
        with open(FILENAME,"w") as f:
            json.dump(expenses,f)
    except(TypeError):
        print("types dont match in expenses")
    
def generate_id(expenses):
    """
    
    """
    if len(expenses)==0:
        return 1
    max_id =1
    for data in expenses:
        max_id = max(max_id,data["id"])
    return (max_id +1)

def add_expense(expenses: list) -> list:
    """
    

    Create expense as a dict:
    {
        "id": <int>,
        "amount": <float>,
        "category": <string>,
        "date": <string>,
        "note": <string>
    }

   
    """
    new_expense ={}
    new_expense["id"]=generate_id(expenses)
    # Takes amount input
    while True:
        try:
            in_amount = float(input("Enter amount of your expense: "))
        except(TypeError,ValueError):
            print("Enter valid amount")
        else:
            new_expense["amount"] = in_amount
            break

        # Takes category input
    while True:
        try:
            in_category = input("Enter type of expense(Food/Transport/Rent etc.): ")
            if not in_category:
                raise ValueError
        except(ValueError):
            print("Enter valid category")
        else:
            new_expense["category"]=in_category
            break
    
    # Takes date input
    in_date = input("Enter date (YYYY-MM-DD) or press Enter to submit today's date")
    if not in_date:
        in_date = str(date.today())
    new_expense["date"] = in_date

    # Takes note input
    in_note = input("Enter note about this expense or Press Enter to skip: ")
    # if notes is empty dont show it
    if not in_note:
        in_note = "NONE"
    new_expense["note"] = in_note

    expenses.append(new_expense)
    return expenses

        
def view_all(expenses:list)->None:
   '''
    Example format:
    [1] 2024-01-15 | Food       | Rs. 150.00 | dinner with friends
    [2] 2024-01-16 | Transport  | Rs. 50.00  | auto to college
    '''
   print("\n")
   print("====="*11)
   if not expenses:
       print("No expense added !")
   else:
       for data in expenses:
           print(f'[{data["id"]}] {data["date"]} | {data["category"]} | {data["amount"]} | {data["note"]}')
   
   print("====="*11)   

def view_by_category(expenses:list)->None:
    while True:
        try:
            search_category = input("Enter category to filter: ")
            if not search_category:
                raise ValueError
        except ValueError:
            print("Enter valid category type!")
        else:
            break
    
    search_category = search_category.lower()
    filtered_categ = [data for data in expenses if data["category"].lower()==search_category]
    
    if len(filtered_categ)>0:
        view_all(filtered_categ)
    else:
        print("No such category exists!")


def delete_expense(expenses:list)->list:
    while True:
        try:
            id_to_del = int(input("Enter an ID to delete: "))
            if id_to_del<=0:
                raise ValueError
        except ValueError:
            print("Enter valid ID number!")
        else:
            break
    found = False
    for data in expenses:
        if data["id"]==id_to_del:
            confirm = input("Are you sure to delete (y/n)").strip().lower()
            found = True
            if confirm=='y':
                print("deleting....")
                expenses.remove(data)
                break
            elif confirm =='n':
                break
            else:
                print("Invalid input entered by user!")
    
    if not found:
        print("No such ID is found in the expenses")
                   
    return expenses

    
def summary(expenses:list)->None:
    #  ================================
    # Total Expenses : 12
    # Total Spent    : Rs. 3450.00
    # --------------------------------
    # Food           : Rs. 1200.00
    # Transport      : Rs. 800.00
    # Entertainment  : Rs. 1450.00
    # ================================

    total_expenses = len(expenses)
    total_spent= sum(data["amount"] for data in expenses)

    categ_amt = {}
    for data in expenses:
        categ_name = data["category"]
        if categ_amt.get(categ_name):
            categ_amt[categ_name]+=data["amount"]
        else:
            categ_amt[categ_name]= data["amount"]

  
    middle = "-----"
    footer = "====="
  
    print("\n==============================")
    print("       SUMMARY        ")
    print("==============================")
    print(f' Total Expenses : {total_expenses}\n Total Spent : {total_spent}')
    print(middle*5)
    for key,val in categ_amt.items():
        print(f' {key} : {val}')
    print(footer*5)



def sort_and_view(expenses):
    """
    Ask user to sort by:
    1. Amount
    2. Date
    3. Category
    """
    while True:
        try:
            to_sort = input("Sort by ?? Type - a for Amount | d for Date | c for category: ").strip().lower()
            if to_sort not in ["a","d","c"]:
                raise ValueError
        except ValueError:
            print("Please Enter valid input to sort")
        else:
            break

    if to_sort=="a":            # sort by amount
        ans_lst = sorted(expenses,key=lambda x:x["amount"])
    elif to_sort=="d":          # sort by date
        ans_lst = sorted(expenses,key=lambda x: x["date"])
    else:                        #sort by category
        ans_lst  = sorted(expenses,key=lambda x:x["category"])
    
    view_all(ans_lst)

        




def main():
    expenses = load_expenses()

    while True:
        print("\n==============================")
        print("       Expense Tracker        ")
        print("==============================")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. View by category")
        print("4. Delete expense")
        print("5. Summary")
        print("6. Sort expenses")
        print("7. Exit")
        print("==============================")

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            expenses = add_expense(expenses)
            save_expenses(expenses)
        elif choice == "2":
            view_all(expenses)
        elif choice == "3":
            view_by_category(expenses)
        elif choice == "4":
            expenses = delete_expense(expenses)
            save_expenses(expenses)
        elif choice == "5":
            summary(expenses)
        elif choice == "6":
            sort_and_view(expenses)
        elif choice == "7":
            print("Bye!")
            break
        else:
            print("Invalid option. Enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
