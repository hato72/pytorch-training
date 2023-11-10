class BankAccount:
    def __init__(self,name):
        self.name = name
        self.balance = 0
        self.interest_rete = 0.01
    
    def deposit(self,bal):
        self.balance += bal

    def withdraw(self,bal):
        self.balance -= bal        

    def get_balance(self):
        return self.balance

    def set_interest_rate(self,rate):
        self.interest_rete = rate

    def apply_interest(self):
        self.balance += self.balance*self.interest_rete