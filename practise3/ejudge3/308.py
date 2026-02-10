class Account:
    def __init__(self,owner, balance):
        self.balance = balance
        self.owner = owner
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        self.balance -=amount
        return self.balance

a,b = map(int, input().split())
account = Account("User", a)
print(account.withdraw(b))

