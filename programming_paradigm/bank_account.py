
class BankAccount:
    def init(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited: ${amount:.1f}")  # Print deposited amount with one decimal place
        return self.account_balance

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds")  # Print message if there are not enough funds
            return False
        self.account_balance -= amount
        print(f"Withdrew: ${amount:.1f}")  # Print withdrawn amount with one decimal place
        return True

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
               
# Testing the class
account1 = BankAccount(200)
print(account1.deposit(100))    # This will print the deposit message and return the new balanc
