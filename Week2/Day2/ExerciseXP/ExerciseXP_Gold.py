class BankAccount:
    def __init__(self, balance, username, password, authenticated=False):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = authenticated
  
    def authenticate(self, username, password):
        if username == self.username and password == self.password:
            self.authenticated = True
            print("Authentication granted")
            return True
        else:
            print("something went wrong")

    def deposit(self, montant):
        if self.authenticate(input("Username svp: "), input("password svp:")):
            if isinstance(montant, int):
                if 0 < montant:
                    self.balance += montant
                    print(f"vous avez deposé {montant}")
                    return (self.balance)
                else:
                    raise Exception("le montant doit être positif.")
            else:
                raise ValueError("this is not a number")
        else:
            raise Exception("Wrong Username or Password")
    

    def withdraw(self, montant):
        if self.authenticate(input("Username svp: "), input("password svp:")):
            if isinstance(montant, int):
                if 0 < montant < self.balance:
                    self.balance -= montant
                    print(f"vous avez retiré {montant}")
                    return (self.balance)
                else:
                    raise Exception("le montant doit être positif et inférieur a votre balance.")
            else:
                raise ValueError("this is not a number")
        else:
            raise Exception("Wrong Username or Password")
    

    def show_balance(self):
        print(f"Votre balance: {self.balance}")

    # def authenticate(self, username, password):
    #     if username == self.username and password == self.password:
    #         self.authenticate = True
    #         print("Authentication granted")
    #         return True
    #     else:
    #         print("something went wrong")



class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=40,minimum_balance=10):
        super().__init__(balance, username="John", password="password", authenticated=False)
        self.minimum_balance = minimum_balance

    def withdraw(self, montant):
        if self.authenticate(input("Username svp: "), input("password svp:")):
            if montant > 0:
                if self.balance - montant >= self.minimum_balance:
                    self.balance-=montant
                    return f'vous avez retiré: {montant}\nbalance: {self.balance}'
                else:
                    raise ValueError("Desole le minimum balance n'est pas respecté")
            else:
                raise ValueError("The value need to be positive")





my_account = BankAccount(10, "John", "password")
# my_account.show_balance()
# my_account.withdraw(5)
# my_account.show_balance()
# my_account.deposit(10)
# my_account.show_balance()
my_account = MinimumBalanceAccount()
# print(my_account.withdraw(5))
