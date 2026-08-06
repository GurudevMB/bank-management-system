from exceptions import InvalidAmountError, InsufficientFundsError
from dataclasses import dataclass


@dataclass
class Account:
    account_number: int
    holder_name: str
    balance: float = 0

    def deposit(self, amount):

        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be greater than zero.")

        self.balance += amount
        print(f"₹{amount} deposited successfully.")
        print(f"Current Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be greater than zero.")

        if amount > self.balance:
            raise InsufficientFundsError("Insufficient Balance.")

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