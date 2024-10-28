import random
class BankAccount: 
    def __init__(self, full_name, account_number = None, balance = 0): 
    #Makes account_number optional if not hard coded, and balance starts at 0
        self.name = full_name
        self.account = account_number if account_number else self.random_account_number()
        self.balance = balance

    #Generates an 8 digit random account number
    def random_account_number():
        return random.randint(10000000, 99999999)
    
    #Hides the first 4 numbers to print only the last 4 digits
    def last_four_digits(self):
        account_str = str(self.account)
        return '*' * (len(account_str) - 4) + account_str[-4:]
    
    #Deposit Function
    def deposit(self,amount):
        self.balance += amount
        return f'Amount Deposited: ${amount:,.2f}\nNew Balance: ${self.balance:,.2f}'

    #Withdraw Function w/ logic for insufficient funds
    def withdraw(self, amount):
        self.balance -= amount
        if amount > self.balance:
            return f'INSUFFICIENT FUNDS. You will be charged a $10 overdraft fee.\nWithdrawing ${amount:,.2f}...\nNew Balance: -${abs(self.balance - 10):,.2f}'
        return f'Amount Withdrawn: ${amount:,.2f}\nNew Balance: ${self.balance:,.2f}'
    
    def get_balance(self):
        return f'Current Balance: ${self.balance:,.2f}'