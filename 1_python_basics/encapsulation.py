class BankAcc:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance
    
acc=BankAcc(1000)
acc.deposit(500)
print(acc.get_balance())
