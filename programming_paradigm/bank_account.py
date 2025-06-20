class BankAccount:
    def __init__(self, initial_balance=0):
      self.account_balance = initial_balance
    
    def deposit(self,amount):
      self.account_balance += amount

    
    def withdraw(self,amount):
      if self.account_balance >= amount :
        self.account_balance -= amount
        return True
      elif self.account_balance <= amount:
         print("Insufficient funds.")
         return False
    
    def display_balance(self):
      print(f"Current Balance: ${self.account_balance}")

# account = BankAccount(100)
# account.display_balance()
# account.deposit(50)
# account.withdraw(30)
# account.withdraw(30)
# account.display_balance()