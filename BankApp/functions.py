from Classes import *
import uuid 
import bcrypt

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
    print("2.Login")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. View Balance")
    print("6. Delete Account")
    print("7. Exit")
    userInput = int(input("What are you doing Today: "))
    if userInput == 1:
            sign_up()
    elif userInput == 2:
           login_interface()
    elif userInput == 3:
            DepositMoney()
    elif userInput== 4:
            WithdrawMoney()
    elif userInput== 5:
            RetrieveBalance
    elif userInput == 6:
            DeleteAccount()
    elif userInput == 7:
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
    username = input("Enter your Username: ")
    # Validate or obtain a strong password
    password = input("Enter your Password: ")
    while len(password)  < 6:
        print("Enter a password with length greater than Six characters")
        password = input("Enter your Password: ")
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
    
    return [name, gender, age, title, pin, account_type, initial_deposit,username,password]

def sign_up():
    user_input = sign_up_interface()
    name, gender, age, title, pin, account_type, initial_deposit,username,password= user_input
    
    # Generate unique customer and account IDs 
    customer_id = Generate_Id()
    account_no = Generate_Id()
    
    # Create a new customer account
    account = Account(account_no, customer_id, name, gender, age, title, initial_deposit, account_type, pin,username,password)
    
    print("Registration successful!")
     #return account
    return account.get_account_owner().get_username_password()


def get_user_credentials():
    username = input("Name: ")
    password = input("Pin: ")
    return username, password

def login(username, password,user_database):
    if username in user_database.keys():
        hashed_password = user_database[username]
        if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
            return True
    return False

def login_interface():
    while True:
        print("Please Enter your Credentials")
        username, password = get_user_credentials()
        if login(username, password):
            print("Login successful!")
            break
        else:
            print("Login failed. Please try again.")


def RetrieveAccounts():
    return Account.Accounts

def RetrieveCustomers():
    return Customer.Customers

def RetrieveEmployees():
    return Employee.Employees

def DepositMoney(account_number,deposit_amount,pin):
    # Find the account by account_number, update its balance
    if account_number == Account.Accounts.values()[0]:
        account = Account.Accounts.values()[3]
        pin = int(input("Please Enter Your Pin"))
        if pin == int(Account.Accounts.values()[2]):
            account.deposit(deposit_amount)

def WithdrawMoney(account_number,deposit_amount,pin):
     if account_number == Account.Accounts.values()[0]:
        account = Account.Accounts.values()[3]
        pin = int(input("Please Enter Your Pin"))
        if pin == int(Account.Accounts.values()[2]):
            account.withdraw(deposit_amount)
def RetrieveBalance(account_number,pin):
    if account_number == Account.Accounts.values()[0]:
        account = Account.Accounts.values()[3]
        pin = int(input("Please Enter Your Pin"))
        if pin == int(Account.Accounts.values()[2]):
            account.get_balance()

def DeleteAccount(account_number):
    if account_number == Account.Accounts.values()[0]:
        account = Account.Accounts.values()[3]
        pin = int(input("Please Enter Your Pin"))
        if pin == int(Account.Accounts.values()[2]):
            del account



def Exit(var,value):
    var = value 
    return var









    
