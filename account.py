print("account.py loaded")
class Account:

    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        self.balance += amount
        print(f"₹{amount} deposited successfully.")
        print(f"Current Balance: ₹{self.balance}")
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return

        if amount > self.balance:
            print("Insufficient Balance.")
            return

        self.balance -= amount
        print(f"₹{amount} withdrawn successfully.")
        print(f"Current Balance: ₹{self.balance}")
    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")
    def display_account(self):
        print("\n" + "=" * 30)
        print("      ACCOUNT DETAILS")
        print("=" * 30)
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.holder_name}")
        print(f"Balance         : ₹{self.balance}")
        print("=" * 30)