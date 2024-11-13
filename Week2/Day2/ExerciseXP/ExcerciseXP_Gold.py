class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, num):
        if int(num) and num > 0:
            deposit = num
            self.balance += deposit
        elif int(num) and num < 0:
            raise Exception("The deposit need to be positive.")
    
    def withdraw(self, num):
        if isinstance(num, int) and num > 0:
            if num <= self.balance:
                self.balance -= num
            else:
                raise Exception("Insufficient balance.")
        else:
            raise Exception("The amount to withdraw must be a positive integer.")
    
    def show_balance(self):
        print(self.balance)

class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance, minimum_balance = 0):
        super().__init__(balance)
        self.minimum_balance = minimum_balance
    def withdraw(self, num):
        if isinstance(num, int) and num > 0:
            if self.balance - num >= self.minimum_balance:
                self.balance -= num
            else:
                raise Exception("Withdrawal would take balance below minimum balance.")
        else:
            raise Exception("The amount to withdraw must be a positive integer.")
        


my_account = BankAccount(10)
my_account.deposit(5)
my_account.show_balance()
my_account.deposit(5)
my_account.show_balance()
my_account.deposit(0)
my_account.show_balance()
my_account.withdraw(0)
my_account.show_balance()

min_balance_account = MinimumBalanceAccount(50, minimum_balance=20)
min_balance_account.withdraw(25)
min_balance_account.show_balance()
