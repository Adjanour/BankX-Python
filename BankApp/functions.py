from Classes import *
import uuid 
runing = 1

def chooseWhoYouAre():
    print("Who are you? ")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    userInput = int(input("What is your choice: "))
    return userInput

def initital_display(user_type=None):
    print("*____________________________*")
    if user_type == None:
          print("Hello Welcome to Salem Bank")
          type = chooseWhoYouAre() 
    else:
        if type == 1:
            print(f"Hello{user_type} Welcome!")
            running = True
            while running == True:
                  CustomerDisplay()
        elif type == 2:
            adminDisplay()
        else:
            running == False 


def CustomerDisplay():
    print("Hello Customer, Welcome to Salem Bank")
    print("Please select an option from the menu below")
    print("1. SignUp")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Balance")
    print("5. Delete Account")
    print("6. Exit")
    userInput = int(input("What are you doing Today: "))
    if userInput == 1:
            SignUp()
    elif userInput == 2:
            DepositMoney()
    elif userInput== 3:
            WithdrawMoney()
    elif userInput== 4:
            RetrieveBalance
    elif userInput == 5:
            DeleteAccount()
    elif userInput == 6:
            Exit(runing,False)
    

def adminDisplay():
    print("Hello Admin, Welcome to CinemaHouseX2")
    print("Please select an option from the menu below")
    print("1. Display all Accounts")
    print("2. Display all Customers")
    print("3. Display all Employees ")
    userInput = int(input("What are you doing today: "))
    if userInput == 1:
        RetrieveAccounts()
    elif userInput == 2:
        RetrieveCustomers()
    elif userInput == 3:
        RetrieveEmployees()
    
def Generate_Id():
    # Generate a unique ID using UUID (Universally Unique Identifier)
    unique_id = uuid.uuid4()
    # Convert the UUID to a string 
    id_str = str(unique_id)
    return id_str

# def SignUp_Interface():
#     # Get user input for registration information (e.g., name, age, gender, etc.)
#     name = input("Please Enter Your Name: ")
#     gender = input("Please Enter Your Gender: ")
#     age = input("Please Enter Your Age: ")
#     title = input("Please Enter Your Title: ")
#     correct = False
#     while correct == False:
#         pin = input("Please Enter A four-digit Pin: ")
#         if len(pin) >= 4:
#             pin = int(pin)
#             correct = True
#         else:
#             correct = False
#     try:
#         account_type = input("""  
# Please Select An account Type
# 1.Saving
# 2.Current
# 3.Student
# Note!: Please type in the name of the account type: """)
#     except ValueError:
#         print("Only character input allowed")
#     initial_deposit = int(input("Please Enter Your Initital Deposit: "))

#     return [name,gender,age,title,pin,account_type,initial_deposit]
    
# def SignUp():
#     user_input = SignUp_Interface()
#     name = user_input[0]
#     gender = user_input[1]
#     age = user_input[2]
#     title = user_input[3]
#     pin = user_input[4]
#     account_type = user_input[5]
#     initial_deposit = user_input[6]
#     customer_id = Generate_Id()
#     account_no = Generate_Id()
#     # Create a new customer account 
#     account = Account(account_no,customer_id,name,gender,age,title,initial_deposit,account_type,pin)
#     print("Registration successful!")

def sign_up_interface():
    # Get user input for registration information
    name = input("Enter your full name: ")
    gender = input("Enter your gender: ")
    age = input("Enter your age: ")
    title = input("Enter your title: ")
    
    # Validate and obtain a four-digit PIN
    pin = input("Enter a four-digit PIN: ")
    while not pin.isdigit() or len(pin) != 4:
        print("Invalid PIN. Please enter a valid four-digit PIN.")
        pin = input("Enter a four-digit PIN: ")
    pin = int(pin)
    
    # Validate and obtain the account type
    valid_account_types = ["Saving", "Current", "Student"]
    while True:
        account_type = input("Select an account type (Saving, Current, Student): ")
        if account_type in valid_account_types:
            break
        else:
            print("Invalid account type. Please choose from the provided options.")

    initial_deposit = int(input("Enter your initial deposit: "))
    
    return [name, gender, age, title, pin, account_type, initial_deposit]

def sign_up():
    user_input = sign_up_interface()
    name, gender, age, title, pin, account_type, initial_deposit = user_input
    
    # Generate unique customer and account IDs 
    customer_id = Generate_Id()
    account_no = Generate_Id()
    
    # Create a new customer account
    account = Account(account_no, customer_id, name, gender, age, title, initial_deposit, account_type, pin)
    
    print("Registration successful!")
    
def RetrieveAccounts():
     pass
def RetrieveCustomers():
     pass
def RetrieveEmployees():
     pass
def DepositMoney():
     pass
def WithdrawMoney():
     pass
def RetrieveBalance():
     pass
def DeleteAccount():
     pass


def Exit(var,value):
    var = value 
    return var









    
