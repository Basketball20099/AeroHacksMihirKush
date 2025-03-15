from abc import ABC, abstractmethod

class Accounts(ABC):  # Abstract class, template for other classes basically evertyhing inherits from this.
    def __init__(self, account_name, balance=0, type=None): #Initiliaze our account names and the balance
        self.account_name = account_name
        self.balance = float(balance)
        self.accounttype = type
   
    @abstractmethod
    def account_type(self): #type of account, correlates with the name cuz yeah
        pass
    
    #down here r our  superclass main functions that can will be accessed by the other classes, basically the template/frame for the entire program.
    def deposit(self, amount):
        if amount > 0: #cannot deposit nothing
            self.balance += amount
            print(f"You deposited ${amount:.2f} into your {self.account_name} account. Your new balance is ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")
        
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance: #cant withdraw more than your balance
                self.balance -= amount
                print(f"You withdrew ${amount:.2f} from your {self.account_name} account. Your new balance is ${self.balance:.2f}")
            else: 
                print("Withdrawal amount must be positive.")  
        else:
            ("Insufficient funds, :( damn bro you broke.")

    def check_balance(self):
        print(f"Account: {self.account_name}. Balance: ${self.balance}.") #checks balance, displays account name and the amount remaining

    def account_info(self):
        return f"{self.account_name}: ({self.accounttype}) account, Balance: ${self.balance:.2f}" #all account info

#down here are our account types :)
class Savings(Accounts):
    def account_type(self):
        return "Savings"

class Checking(Accounts):
    def account_type(self):
        return "Checking"
    
class Business(Accounts):
    def account_type(self):
        return "Business"

class Banking(): #Banking class in which the main functions of the code happens
    def __init__(self):
        self.accounts = [] #empty list which will contain all user accounts
# creation of user accounts
    #specifies account type and calls account type class and fills in attributes that the user decides.
    def create_accounts(self, account_type, account_name, balance):
        if account_type == "savings":
            account = Savings(account_name, balance, account_type)
        elif account_type == "checking":
            account = Checking(account_name, balance, account_type)          
        elif account_type == "business":
            account = Business(account_name, balance, account_type)
        else:
            print("Invalid Account Type")
            return None
        
        self.accounts.append(account)
        print(f"{account_type.capitalize()} account created successfully")
        return account
    #finds specific account from list with all user accounts
    
    def find_account(self, account_name):
        for account in self.accounts:
            if account.account_name == account_name: #search by account name
                return account
        print("Account not found")
        return None
            #the functions which can be done in the accounts, we use if statement to check if the account exists
    
    #our functions for the users to do
    def deposit(self, account_name, amount):
        account = self.find_account(account_name)  #finds account based on name, selection for which to deposit to, same for the rest
        if account: #if is just to check if it exists or not
            account.deposit(amount) #calls deposit function from the superclass, same for the rest

    def withdraw(self, account_name, amount):
        account = self.find_account(account_name)
        if account:
            account.withdraw(amount)

    def check_balance(self, account_name):
        account = self.find_account(account_name)
        if account:
            account.check_balance()

    def list_all_accounts(self):
        if self.accounts: #checks if the list exists with the accounts
            print("\nAll Accounts: ")
            for account in self.accounts: #checks every account in the list
              print(account.account_info()) #returns info for all accounts
        
    #this is all the user stuff
    def main(self):
        while True:
            print("\n Welcome to Skibidi Bank")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Check account info")
            print("6. Exit")

            choice = input("Enter your choice: ").lower()

            if choice == "1":
                account_type = input("select an account type(savings/checking/business): ").lower()
                account_name = input(f"Enter a name for your {account_type} account: ").lower()
                balance = float(input("Enter your initial balance: "))
                self.create_accounts(account_type, account_name, balance) #creates account witht he users attributes
            
            elif choice == "2":
                account_name = input("Which account would you like to deposit to?: ")
                amount = float(input("Enter the amount to deposit: "))
                self.deposit(account_name, amount) #calls deposit function, same for rest with their own function

            elif choice == "3":
                account_name = input("Which account would you like to withdraw from?: ")
                amount = float(input("Enter the amount to withdraw: "))
                self.withdraw(account_name, amount)

            elif choice == "4":
                account_name = input("which acount would you like to check your balance?: ")
                self.check_balance(account_name)

            elif choice == "5":
                self.list_all_accounts()
            elif choice == "6":
                print("Thanks for visiting Skibidi bank!")
                break

bank = Banking() #instance of class, just runs the whole thing
bank.main()
    
    