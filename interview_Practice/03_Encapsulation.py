class BankAccount:
    def __init__(self, name, balance):
        self.name = name                    # public
        self.__balance = balance            # private variable

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, new_balance):
        self.__balance = new_balance

acc1 = BankAccount("Wali", 100_000)
acc1.set_balance(200_000)

print(acc1.name, acc1.get_balance())