items=[]
def add_item() :
    item=input("enter the item name you want to add: ")
    items.append(item)
def remove_item() :
    r_item=input("enter the item name you want to remove: ")
    if r_item not in items :
        print(f"the item {r_item} not in list")
    else :
        items.remove(r_item)
def display_items() :
    if not items :
        print("no item in list yet")
    else:
        print(items)
def total_items() :
    if not items :
        print("no item in list yet")
    else:
        print(len(items))
def menu() :
    while True:
        choice = input("enter 1) to add , 2) to remove , 3) to display , 4) to show the number of items , 5) to exit: ")
        
        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            display_items()
        elif choice == "4":
            total_items()
        elif choice == "5":
            break
        else:
            print("invalid choice")
menu()
