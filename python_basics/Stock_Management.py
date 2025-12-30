import os
import time
import sys

from colorama import init, Fore


DARK_GREEN = '\033[38;5;22m'  
DARK_BLACK = '\033[38;5;232m'
DARK_RED = '\033[38;5;124m'
DARK_GREEN = '\033[38;5;22m'
DARK_YELLOW = '\033[38;5;178m'
DARK_BLUE = '\033[38;5;32m'
DARK_MAGENTA = '\033[38;5;125m'
DARK_CYAN = '\033[38;5;44m'
DARK_WHITE = '\033[38;5;231m'
RESET = '\033[0m'

DARK_BLACK_BG = '\033[48;5;232m'   # Dark Black
DARK_RED_BG = '\033[48;5;124m'     # Dark Red
DARK_GREEN_BG = '\033[48;5;22m'    # Dark Green
DARK_YELLOW_BG = '\033[48;5;178m'   # Dark Yellow
DARK_BLUE_BG = '\033[48;5;32m'     # Dark Blue
DARK_MAGENTA_BG = '\033[48;5;125m'  # Dark Magenta
DARK_CYAN_BG = '\033[48;5;44m'     # Dark Cyan
DARK_WHITE_BG = '\033[48;5;231m'   # Dark White


UNDERLINE = '\033[4m'



def clear():
    _=os.system("clear")

def current_balance():
    print (f"\nYour current balance is {balance:.2f}FRW ")

def get_current_time():
    return time.strftime("%d/%m/%Y %H:%M:%S")


def print_uppercase(message):
    print(f"\n{message.upper()}\n")

def Start_business():
    global message
    global balance
    global stock
    global name_of_business
    balance = 0
    message = []
    stock = []


    print_uppercase("\nWelcome to business zone! we help you to start your business You should start by naming your business.")
    
    while True:
        name_of_business = input(f"\nName your business: ").strip()
        
        if not name_of_business:
            clear()
            print(f"Business must have a name!")
            continue  # Restart the loop

        message.append(f"{get_current_time()} You created a business called {name_of_business}.")
        add_goods()
        break  # Exit the loop once the business is named

def add_goods():
    clear()
    while True:
        list_items = input(f"\nWhat would you like to add in {name_of_business}'s stock?: ").strip().upper()
        if not list_items:
             clear()
             print(f"Item cannot be empty. Please add a valid item.")
             continue
        
        if list_items in stock:
            clear()
            print(f"\n{list_items} already exist!")
            continue
        
        if list_items:  # Check if input is not empty
            stock.append(list_items)
            message.append(f"{get_current_time()} You added '{list_items}' to the stock.")
        else:
            print(f"Item cannot be empty. Please add a valid item.")
        clear()
        while True:

            
            choice = input(f"\nDo you want to add more items to stock? (Y/N): ").lower()
            if choice == "y":
                clear()
                break # Stay in the loop to add more items
            elif choice == "n":
                clear()
                goods()  # Call the menu function to proceed
                return  # Exit the loop
            else:
                clear()
                print(f"\nInvalid choice! Please enter Y or N.")



def stocks():
    clear()
    while True:
        print(f"{UNDERLINE}\nStock statement:{RESET}\n")
        if stock:
            for index, entry in enumerate(stock, start=1):  # Start numbering from 1
                print(f"{index}. {entry}")
            choice = input("\nDo you want to clear Stock Y/N?  Press 'A' to add item in the stock. Press 'R' to remove item in stock: ").lower()
            if choice == "y":
                if stock:
                    stock.clear()
                    clear()
                    choice = input(f"\nStock cleared succefully. would you like to add items in stock? Y/N or 'M' back to menu: ").lower()   
                    message.append(f"{get_current_time()} Stock cleared .")                 
                    if choice == "y":
                        add_goods()
                    elif choice== "m":
                        clear()
                        menu()  
                    else:
                        clear()
                        goods()
                else:
                    choice = input(f"\nNothing to  clear. would you like to add items in stock? Y/N: ").lower()

                    if choice == "y":
                        add_goods()
                    else:
                        clear()
                        goods()            
            elif choice == "n":
                    clear()
                    menu()
            elif choice == "a":
                add_goods()
            elif choice =="r":
                remove_item()
            else:
                clear()
                print(f"Invalid input!")     
        else:
            choice = input(f"\nNo items in stock. would you like to add items in stock? Y/N: ").lower()
            if choice == "y":
                add_goods()
            else:
                clear()
                goods()  

def remove_item():
    clear()
    while True:
        print(f"\n{UNDERLINE}{DARK_RED}Deletion process:\n{RESET}")
        if stock:
            for index, entry in enumerate(stock, start=1):
                print(f"{index}. {entry}")
            choice = input("\nEnter item you want to remove. Press 'B' to back: ").upper()

            if choice.isdigit():
                index = int(choice) - 1  # Convert to zero-based index
                if 0 <= index < len(stock):
                    choice = stock[index]  # Get the actual item from stock
                    stock.remove(choice)
                    clear()
                    print(f"\n'{choice}' Removed succefully!")
                    message.append(f"{get_current_time()} '{choice}' was removed from stock.")
                    break
            
                else:
                    clear()
                    print("Item doesn't Exist!")
                    continue
            elif choice == "B":
                stocks()
            else:
                clear()
                print(f"\nInavild Value! Please select a valid number.")

def messages():
    clear()
    while True:
         print(f"\n{UNDERLINE}Messages:\n{RESET}")
         if message:
             for entry in message:
                 print(entry)
             choice = input(f"\n1. Back\n2. Creal messages\n\n> ").lower()
             if choice == "1":  
                clear()             
                menu()
             elif choice == "2":
                message.clear()
                clear()
                print(f"\nMessage cleared succefully!")
            
                continue
             else:
                 clear()
                 print(f"{DARK_RED}Invalid input!{RESET}")
         else:
                clear()
                choice =input("No messages available press 'M' back to menu: ").lower()
                if choice == "m":
                   clear()
                   menu()


def edit_name():
     clear()
     global name_of_business
     while True:
        print(f"\n{UNDERLINE} Bussiness Rename.\n{RESET}")
        new_bussiness_name = input(f" \nEnter new name of your business: ").strip()
        if not new_bussiness_name:
            clear()
            print("Please write something!\n")
            continue
            
        if new_bussiness_name == name_of_business:
            clear()
            choice = input(f"{new_bussiness_name} was already the name of you business! do you want  keep it Y/N: ").lower()
            if choice =="y":
                clear()
                menu()
            else:
                continue
        else:
            name_of_business = new_bussiness_name
            message.append(f"{get_current_time()} Name of business changed to '{new_bussiness_name}'.")
            clear()
            print(f"Name changed successfully!")
            menu()
                    
def menu():
    
    while True:
        print(f"\n{UNDERLINE}{name_of_business} Status: {RESET}\n")
        choice = input(f"1. Stock\n2. Message\n3. Edit name of your business\n4. Back to your goods.\n5. Balance\n\n> ").strip().lower()
        
        if choice == "1":
            stocks()
        elif choice == "2":
            messages()
        elif choice == "3":
            edit_name()    
        elif choice == "4":
            clear()
            goods()
        elif choice=="5":
            clear()
            current_balance()
            continue
        else:
            clear()
            print(f"\n Wrong choice! Please select a valid option.\n")

def goods():
    global balance
    while True:
        print(f"\n{UNDERLINE}{name_of_business}'s Business available goods.{RESET}\n")
        if stock:
            for index, item in enumerate(stock, start=1):  # Start numbering from 1
                print(f"{index}. {item}")
                
            choice = input(f"\nSelect an item by number or check Menu by pressing 'M': ").strip()
            
            if choice.upper() == "M":
                clear()
                menu()
                continue
            if choice.upper() =="Q" or choice.upper() =="E":
                print(f"\n Business Exited by '{choice}'...\n")
                sys.exit()
            
            # Check if the input is a digit and within range
            if choice.isdigit():
                index = int(choice) - 1  # Convert to zero-based index
                if 0 <= index < len(stock):
                    choice = stock[index]  # Get the actual item from stock
                else:
                    clear()
                    print(f"\nItem does not exist! Please select a valid number.")
                    continue
            else:
                clear()
                print(f"\nInvalid input! Please enter a valid input.")
                continue
            
            # Now we can proceed with selling the item
    
            while True:
                try:

                    cost = float(input(f"\nHow much is {choice} per Kilo?: "))
                    if cost <= 0:
                        clear()
                        print(f"Cost must be greater than 0!")
                        continue
                except ValueError:
                        clear()
    
                        print(f"\nInvalid input! Please enter numeric values.")
                        continue

                while True:
                    try:
                        kg = float(input(f"\nHow many kilos of {choice} do you want?: "))
                        if kg <= 0:
                            clear()
                            print(f"\nKilos cannot be less than or equal to 0!")
                            continue
                        else:
                            total = cost * kg
                            balance += total
                            clear()
                            print(f"\n{get_current_time()} You sold {kg} kilos of {choice} at a cost of {cost} per Kg Total cost was {total}. Your new balance is {balance:.2f} FRW.")
                            message.append(f"{get_current_time()} You sold {kg} kilos of {choice} at a cost of {cost} FRW per Kg. Your new balance is {balance:.2f} FRW.")
                            goods()  # Exit the inner selling loop
                    except ValueError:
                        clear()
                        print(f"\nInvalid input! Please enter numeric values.")
                        continue

           

        else:
            choice = input(f"No goods available. Would you like to add some goods (Y/N): ").lower()
            if choice == "y":
                add_goods()
            else:
                clear()
                print("You don't have goods in stock!")


Start_business()