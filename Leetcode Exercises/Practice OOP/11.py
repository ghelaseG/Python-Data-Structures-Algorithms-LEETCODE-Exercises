"""
Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.
"""

class Bank:
    #initialise the bank with an empty dict for customer accounts and balance
    def __init__(self):
        self.customers = {}

    #create a new account with a given account number and an optional initial balance
    def create_account(self, account_number, initial_balance = 0):
        if account_number in self.customers:
            print("Account number already exists.")
        else:
            self.customers[account_number] = initial_balance
            print("Account created successfully")

    #make a deposit to the account with the given account number
    def make_deposit(self, account_number, amount):
        if account_number in self.customers:
            self.customers[account_number] += amount
            print("Deposit successful.")
        else:
            print("Account number does not exist.")
    
    def make_withdrawal(self, account_number, amount):
        if account_number in self.customers:
            if self.customers[account_number] >= amount:
                self.customers[account_number] -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
        else:
            print("Account number does not exist.")

    def check_balance(self, account_number):
        if account_number in self.customers:
            balance = self.customers[account_number]
            print(f"Account balance: {balance} for the account number {account_number}")
        else:
            print("Account number does not exist.")