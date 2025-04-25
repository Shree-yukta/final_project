import csv
import os
from datetime import datetime

#Function that displays main menu
def display_transactions_menu():
    print("\n --------- Transactions Management Menu ----------")
    print("1. View all Transactions")
    print("2. Add transaction")
    print("3. View financial summary")
    print("4. Back to main menu")

def add_new_transaction():
    #Ask user to add details
    uid = input("Enter User ID: ")
    date = input("Enter the date of the transaction: ")

    #Setting the correct date if no date given
    if not date:
        date = datetime.now().strftime('%Y-%m-%d')

    type = input("Enter type of transaction (Income/Expense): ")
    category = input("Enter the category: ")

    #Handling Invalid amount input
    while True:
        try:
            amt = float(input("Enter Amount: "))
            break
        except ValueError:
            print("Invalid amount! Please enter a numeric value.")

    des = input("Add description...: ")

    with open('transactions.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([uid, date, type, category, amt, des])

    #Once the user ADDS it all, display: 
    print("\nTransaction is Saved!")
    
    

def display_all_transactions(): 
    print("{:<8} {:<15} {:<12} {:<12} {:<12} {:<40}".format(
        "UserId", "Date", "Type", "Category", "Amount", "Description"
    ))
    print("-"*80)

    #Opening file
    with open('transactions.csv', 'r') as transactionsFile:
        reader = csv.reader(transactionsFile)
        next(reader, None)

        for row in reader:
            if len(row) < 6:
                continue

            uid, date, type, category, amt, des = row
            print("{:<9} {:<15} {:<13} {:<13} {:<13} {:<40}".format(
                uid, date, type, category, amt, des
            ))



def display_financial_summary(userId):

    try:
        with open("transactions.csv", "r") as file:
            reader = csv.reader(file)
            headers = next(reader)

            user_transactions = [row for row in reader if len(row) >=6 and row[0] == userId]

            if not user_transactions:
                print(f"No transactions found for user ID {userId}.")
                return
            
            print("\n-------------------- Financial Summary ---------------------")
            print("{:<12} {:<10} {:<15} {:<10} {:<30}".format(
                "Date", "Type", "Category", "Amount", "Description"))
            print("-" * 85)

            total_income = 0.0
            total_expense = 0.0

            for transaction in user_transactions:
                date = transaction[1]
                t_type = transaction[2]
                category = transaction[3]
                amount = float(transaction[4])
                description = transaction[5]
            
            #tallying income and expense
                if t_type.lower() == "income":
                    total_income += amount
                elif t_type.lower() == "expense":
                    total_expense += amount
            
            #Display each transaction
            print("{:<12} {:<10} {:<15} {:<10} {:<30}".format(
                    date, t_type, category, amount, description
                ))

            net_balance = total_income - total_expense

            #Summary section
            print("\n-------------------- Totals ---------------------")
            print(f"Total Income:   Rs. {total_income}")
            print(f"Total Expense:  Rs. {total_expense}")
            print(f"Net Balance:    Rs. {net_balance}")

    except FileNotFoundError:
        print("Error: transactions.csv file not found.")

            
   #Main program
def transaction_management():
     
    while True:
        display_transactions_menu()


        # Ask the user to choose an option: (1-4)
        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            display_all_transactions()
        elif choice == 2:
            add_new_transaction()
        elif choice == 3:
            #Ask user Id and display details
            userId = input("Enter User Id: ")
            display_financial_summary(userId)
        elif choice == 4:
            break
        else:
            print("Invalid Choice! Please try again!!")
