class BankAccount:
    def __init__(self, initial_balance=0):
      self.account_balance = initial_balance
    
    def deposit(self,amount):
      self.account_balance += amount
      print(f"Deposited: ${amount:.2f}")

    
    def withdraw(self,amount):
      if self.account_balance >= amount :
        self.account_balance -= amount
        print(f"Withdrew: ${amount:.2f}")
        return True
      elif self.account_balance <= amount:
         print("Insufficient funds.")
         return False
    
    def display_balance(self):
      print(f"Current balance: ${self.account_balance:.2f}")

account = BankAccount(100)
account.display_balance()
account.deposit(50)
account.withdraw(30)
account.withdraw(120)
account.display_balance()