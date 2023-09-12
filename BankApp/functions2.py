from Classes import *
import uuid
import bcrypt

running = True

# Create dictionaries to store user data (for simplicity)
customer_database = {}
employee_database = {}

def chooseWhoYouAre():
    print("Who are you? ")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    userInput = int(input("What is your choice: "))
    return userInput

def initial_display(user_type=None):
    global running
    print("*____________________________*")
    
    if user_type is None:
        print("Hello, Welcome to Salem Bank")
        user_type = chooseWhoYouAre()
        if user_type == 1:
            while running:
                customer_display()
        elif user_type == 2:
            admin_display()
        else:
            running = False
    else:
        if user_type == 1:
            print(f"Hello Customer, Welcome!")
            while running:
                customer_display()
        elif user_type == 2:
            admin_display()
        else:
            running = False

def customer_display():
    global running
    print("Hello Customer, Welcome to Salem Bank")
    print("Please select an option from the menu below:")
    print("1. Sign Up")
    print("2. Login")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. View Balance")
    print("6. Delete Account")
    print("7. Exit")
    
    user_input = int(input("What are you doing today: "))
    
    if user_input == 1:
        sign_up()
    elif user_input == 2:
        login_interface(customer_database)
    elif user_input == 3:
        name = input("Please Enter your Name: ")
        deposit_ammount = int(input("Please Enter Your Deposit Amount: "))
        pin = int(input("Please Enter Your Pin: "))
        deposit_money(name,deposit_ammount,pin)
    elif user_input == 4:
        withdraw_money()
    elif user_input == 5:
        retrieve_balance()
    elif user_input == 6:
        delete_account()
    elif user_input == 7:
        running = False

def admin_display():
    global running
    print("Hello Admin, Welcome to Salem Bank")
    print("Please select an option from the menu below:")
    print("1. Display all Accounts")
    print("2. Display all Customers")
    print("3. Display all Employees")
    
    user_input = int(input("What are you doing today: "))
    
    if user_input == 1:
        retrieve_accounts()
    elif user_input == 2:
        retrieve_customers()
    elif user_input == 3:
        retrieve_employees()

def generate_id():
    unique_id = uuid.uuid4()
    id_str = str(unique_id)
    return id_str

def sign_up_interface():
    name = input("Enter your full name: ")
    gender = input("Enter your gender: ")
    age = input("Enter your age: ")
    title = input("Enter your title: ")
    username = input("Enter your Username: ")
    
    # Validate or obtain a strong password
    password = input("Enter your Password: ")
    while len(password) < 6:
        print("Enter a password with a length greater than Six characters")
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
    
    return [name, gender, age, title, pin, account_type, initial_deposit, username, password]

def sign_up():
    global customer_database
    user_input = sign_up_interface()
    name, gender, age, title, pin, account_type, initial_deposit, username, password = user_input
    
    # Generate unique customer and account IDs
    customer_id = generate_id()
    account_no = generate_id()
    
    # Create a new customer account
    account = Account(account_no, customer_id, name, gender, age, title, initial_deposit, account_type, pin, username, password)
    
    # Store user data in the customer database (for simplicity)
    customer_database[username] = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    
    print("Registration successful!")

def get_user_credentials():
    username = input("Username: ")
    password = input("Password: ")
    return username, password

def login(username, password, user_database):
    if username in user_database.keys():
        hashed_password = user_database[username]
        if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
            return True
    return False

def login_interface(user_database):
    while True:
        print("Please Enter your Credentials")
        username, password = get_user_credentials()
        if login(username, password, user_database):
            print("Login successful!")
            break
        else:
            print("Login failed. Please try again.")

def retrieve_accounts():
    # Implement logic to retrieve and display all accounts
    pass

def retrieve_customers():
    # Implement logic to retrieve and display all customers
    pass

def retrieve_employees():
    # Implement logic to retrieve and display all employees
    pass

def deposit_money(account_owner_name,deposit_amount,pin):
    # Find the account by account_number, update its balance
    if account_owner_name == Account.Accounts[0][5]:
        account = Account.Accounts.values()[0][4]
        pin = int(input("Please Enter Your Pin"))
        if pin == int(Account.Accounts[0][3]):
            account.deposit(deposit_amount)

def withdraw_money():
    # Implement logic for withdrawing money
    pass

def retrieve_balance():
    # Implement logic for retrieving account balance
    pass

def delete_account():
    # Implement logic for deleting an account
    pass

def main():
    initial_display()

