import json
import os

file_path = "Account's_Data.json"

print("\n\t\t\t\t\t\t%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
      "\n\t\t\t\t\t\t%%%%%%%%%%%%% Welcome to the Banking System %%%%%%%%%%%%%%%"
      "\n\t\t\t\t\t\t%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

class Account:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Amount: ${amount}. New Balance is: ${self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Your balance is low.")
        else:
            self.balance -= amount
            print(f"Withdrawn: ${amount}. Current Balance: ${self.balance}")

    def check_balance(self):
        print(f"Your Current Balance: ${self.balance}.")

def delete_account(accounts):
    account_number = input("Enter account number to delete: ")
    for account in accounts:
        if account.account_number == account_number:
            accounts.remove(account)
            print("Account deleted!")
            return
    print("Account not found.")

def create_account(accounts):
    name = input("Enter account holder's name: ")
    name = name.upper()
    account_number = input("Enter account number: ")
    balance = float(input("Enter initial balance: "))
    account = Account(name, account_number, balance)
    accounts.append(account)
    print("Account created successfully!")

def find_account(accounts):
    account_number = input("Enter account number to search: ")
    for account in accounts:
        if account.account_number == account_number:
            print("\nAccount Details:")
            print(f"Name: {account.name}")
            print(f"Account Number: {account.account_number}")
            print(f"Balance: ${account.balance}")
            return account
    print("Account not found.")
    return None

def save_accounts(accounts):
    with open(file_path, "w") as file:
        json.dump([account.__dict__ for account in accounts], file, indent=4)


def load_accounts():
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            accounts_data = json.load(file)
            return [Account(**account) for account in accounts_data]
    return []

accounts = load_accounts()

while True:
    print("\n1. Create Account"
          "\n2. Deposit Money"
          "\n3. Withdraw Money"
          "\n4. Check Balance"
          "\n5. Delete Account"
          "\n6. Show Account Details"
          "\n7. Exit")

    action = input("Choose an option: ")

    if action == "1":
        create_account(accounts)
        save_accounts(accounts)

    elif action == "2":
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))
        for account in accounts:
            if account.account_number == account_number:
                account.deposit(amount)
                save_accounts(accounts)
                break
        else:
            print("Account not found")

    elif action == "3":
        account_number = input("Enter Account Number: ")
        amount = float(input("Enter withdraw amount: "))
        for account in accounts:
            if account.account_number == account_number:
                account.withdraw(amount)
                save_accounts(accounts)
                break
        else:
            print("Account not found.")

    elif action == "4":
        account_number = input("Enter account number: ")
        for account in accounts:
            if account.account_number == account_number:
                account.check_balance()
                break
        else:
            print("Account not found")

    elif action == "5":
        delete_account(accounts)
        save_accounts(accounts)

    elif action == "6":
        find_account(accounts)

    elif action == "7":
        print("\n\t\tGoodbye!")
        break

    else:
        print("Wrong option. Please select the correct choice.")









