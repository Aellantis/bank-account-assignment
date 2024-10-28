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
    