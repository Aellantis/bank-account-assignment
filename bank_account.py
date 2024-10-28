import random
class BankAccount: 
    def __init__(self, full_name, account_number = None, balance = 0): 
    #Makes account_number optional if not hard coded, and balance starts at 0
        self.name = full_name
        self.account = account_number if account_number not in [None, ''] else self.random_account_number()
        # If the account_number is None or an empty string, generate a random 8 digit number
        self.balance = balance

    #Generates an 8 digit random account number
    @staticmethod
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
            print(f'INSUFFICIENT FUNDS.') 
            print(f'{self.name} will be charged a $10 overdraft fee.\nWithdrawing ${amount:,.2f}...')
            return f'New Balance: -${abs(self.balance -10):,.2f}'
        else:
            return f'Amount Withdrawn: ${amount:,.2f}\nNew Balance: ${self.balance:,.2f}'
    
    #Get Balance Printing the Current Balance
    def get_balance(self):
        return f'Current Balance: ${self.balance:,.2f}'
    
    #Add Interest w/ Monthly and Annual Interest
    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest
        annual_interest = self.balance * (1 + 0.00083) * 12
        print (f'Interest added after one month: ${interest:,.2f}')
        print (f'New Balance: ${self.balance:,.2f}')
        return f'Estimated Annual Balance w/ Interest: ${annual_interest:,.2f}'
    
    def print_statement(self):
        return f'Name: {self.name}\nAccount No.:{self.last_four_digits()}\nBalance: ${self.balance:,.2f}'

Mitchell = BankAccount('Mitchell Hudson', "03141592", 0)
Ashley = BankAccount('Ashley Yung','', 1487)
Ben = BankAccount('Benjamin Kim', '', 5908)

### Testing ####
# Example w/ Mitchell
print(Mitchell.print_statement())
print(Mitchell.deposit(400000))
print(Mitchell.add_interest())
print(Mitchell.withdraw(150))
print(Mitchell.get_balance())
print ("")

#Testing 1
print(Ben.print_statement())
print(Ben.withdraw(6000))
print(Ben.deposit(10000))
print(Ben.add_interest())
print(Ben.get_balance())
print ("")

#Testing 2
print(Ashley.print_statement())
print(Ashley.deposit(7000))
print(Ashley.add_interest())
print(Ashley.withdraw(2050))
print(Ashley.get_balance())