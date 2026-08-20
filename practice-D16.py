class bank:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    #to check total balance
    def check_balance(self):
        print(F"total balane: {self.balance}")

class person(bank):
    def __init__(self, balance, name):
        super().__init__(balance)
        self.__name = name

    @property
    def name(self):
        return self.__name
    #to check user profile
    def check_profile(self):
        print(f"account name: {self.name}")

person1 = person(20000, "theary")
person1.check_profile()
person1.check_balance()
bank = bank(30000)
bank.check_balance()     
    
