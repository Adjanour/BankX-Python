import datetime

class Person:
    def __init__(self,name,age,gender,title):
        self._name = name
        self._age = age
        self._gender = gender
        self._title = title


class Customer(Person):
    def __init__(self,name,customer_id,gender,age,title,username,password):
        super().__init__(name,gender,age,title)
        self._customer_id = customer_id
        self._user_name = username
        self._password = password

    def get__customer_id(self):
        return self._customer_id
    
    def get_username_password(self):
        return self._user_name , self._password
    
    def get_name(self):
        return super()._name

class Employee(Person):
    def __init__(self, name, age, gender, title,employee_id,salary=None):
        super().__init__(name, age, gender, title)
        self.__employee_id = employee_id
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id
    
    def set_employee_id(self,new_employee_id):
        self.__employee_id = new_employee_id
        return f"Employee Id changed successfully"


class Account:
    Accounts = []
    def __init__(self,account_no,account_owner_id,account_owner_name,account_owner_gender,account_owner_age,account_owner_title,initial_deposit,account_type,account_pin,account_owner_username,account_owner_password,account_created_date = datetime.datetime.now):
        self.__account_no = account_no
        self.__initial_deposit = initial_deposit
        self.__account_balance = initial_deposit
        self.__account__type = account_type
        self.__account_owner = Customer(account_owner_name,account_owner_id,account_owner_gender,account_owner_age,account_owner_title,account_owner_password,account_owner_username)
        self.__account_created_date = account_created_date
        self.__account_pin = account_pin
        Account.Accounts.append([self.__account_owner,self.__account_no,self.__account_created_date,self.__account_pin,self,account_owner_name])

    def deposit(self,deposit_amount):
        available_balance = self.__account_balance
        self.__account_balance += deposit_amount
        return f"Deposit made succesfully. Current balance is {self.__account_balance}. Available balance is {available_balance}"
    
    def withdraw(self,withdrawal_ammount):
        assert self.__account_balance >= withdrawal_ammount, f"Withdrawal ammount cannot execeed your Balance"
        assert withdrawal_ammount >=0, f"Withdrawal ammount cannot be zero or less than zero"
        try:
            if withdrawal_ammount > self.__account_balance:
                self.__account_balance -= withdrawal_ammount
        except ValueError:
            print("Only positive values are allowed")

    def get_balance(self,inString=False):
        if inString == True:    
            return f"Your Account Balance is:{self.__account_balance}"
        else:
            return self.__account_balance
    
    def get_account_type(self):
        return self.__account__type
        
    def get_account_owner(self):
        return self.__account_owner
    
    def get_account_no(self):
        return self.__account_no
    
    def __del__(self):
        return f"Account with number: {self.__account_no} deleted successfully"
    
    @staticmethod
    def __list_accounts():
        for Class in Account.Accounts:
            print (f"{Class} => {Class.Value()[1]} ")

    