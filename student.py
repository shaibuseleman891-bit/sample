class Wallet:
    def __init__(self,balance):
        self.__balance = balance
    def __validate(self,amount):
        if amount < 0:
            raise ValueError("the amount must be positive")    
    def deposit(self,amount):
        if amount > 0 :
            self.__balance += amount
    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            
    def get_balance(self):
        return self.__balance
account = Wallet(500)
print(account.get_balance())
                
        
        