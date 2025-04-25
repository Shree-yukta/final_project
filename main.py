import finance_code
import transactions

def display_main_welcome_screen():
    print("*"*50)
    print("--", "Welcome to Money Management System", '--')
    print("*"*50)

def display_main_menu():
    print("\n****** MAIN MENU ******")
    print("1. Manage Users")
    print("2. Manage transactions")
    print("3. Exit the Application")

def main():

    display_main_welcome_screen()

    #Main PROGRAM LOOP
    while True:
        display_main_menu()

        try:
            choice = int(input("Enter choice (1-3): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 3.")
            continue

        if choice == 1:
            finance_code.user_management()
        elif choice == 2:
            transactions.transaction_management()
        elif choice == 3:
            print("\n Thankyou for using the system! See you soon...")
            break
        else:
            print("Invalid choice! Choose a valid number and TRY AGAIN!")

#For running the main function 
main()
