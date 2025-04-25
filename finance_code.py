import csv
import os

def display_user_menu():
    print("\n******** User Management Menu ********".center(82))
    print("1. Display all members")
    print("2. Create a New account")
    print("3. View User details")
    print("4. Back to main menu")

def create_user_account():
    #Get user details
    name = input("Enter your Full name: ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    email = input("Enter your email address: ")
    joindate = input("Enter the date joined: ")

    #Create a new dictionary with input data 
    newUser = [name, dob, email, joindate]

    #generate user code
    new_code = "U001"
    if os.path.exists("users.csv"):
        with open("users.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
            if len(rows) > 1:  # File has header + users
                last_code = rows[-1][0]
                number = int(last_code[1:]) + 1
                new_code = "U" + str(number).zfill(3)

    #Save this new user account
    newUser.insert(0, new_code) #This adds user at the start of the list
    
    file_exists = os.path.exists("users.csv")
    with open("users.csv", "a", newline="") as file:
        writer = csv.writer(file)

        # Write header if file is empty or doesn't exist
        if not file_exists or os.stat("users.csv").st_size == 0:
            writer.writerow(["User ID", "Full Name", "DOB", "Email", "Join Date"])
        
        writer.writerow(newUser)


    print("\n ---------------------- Registration Successful --------------------")
    print(f"Welcome to the system,  {name}. Your User Id is  {new_code}")
    print(f"You have successfully created an account.")



def display_all_users():
    try:
        with open("users.csv", "r") as file:
            reader = csv.reader(file)
            headers = next(reader)  # skip header

            print("{:<10} {:<20} {:<12} {:<30} {:<15}".format("UserID", "Name", "DOB", "Email", "Join Date"))
            print("-" * 90)

            for user in reader:
                if len(user) < 5:  # ensure the row has all expected fields
                    continue
                print("{:<10} {:<20} {:<12} {:<30} {:<15}".format(
                    user[0], user[1], user[2], user[3], user[4]
                ))

    except FileNotFoundError:
        print("Error: users.csv file not found.")

def display_user_details_format(user):
    print("+" + "-"*50 + "+")
    print("|          USER DETAILS          |")
    print("+" + "-"*50 + "+")
    print(f"ID        : " + user[0] + " |")
    print(f"Name      : " + user[1] + " |")
    print(f"DOB       : " + user[2] + " |")
    print(f"Email     : " + user[3] + " |")
    print(f"Join date : " + user[4] + " |")

def display_user_details(userId):
    with open('users.csv', 'r') as usersFromFile:
        reader = csv.reader(usersFromFile)
        next(reader)
        for user in reader:
            if user[0] == userId:
                display_user_details_format(user)
                break
        else:
            print ("User Id not found! Please create a User Id before proceeding!!")
    




#MAIN PROGRAM STARTS

def user_management():

    while True:
        display_user_menu()

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            display_all_users()
        elif choice == 2:
            create_user_account()
        elif choice == 3:
            #Ask the user for User Id, and show user details
            userId = input("Enter your User Id: ")
            display_user_details(userId)
        elif choice == 4:
            break
        else:
            print("Invalid option! Choose a valid number and Try again.")
