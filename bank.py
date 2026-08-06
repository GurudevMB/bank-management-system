from exceptions import AccountNotFoundError
from account import Account 


class Bank:

    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1001


    def create_account(self, holder_name, initial_balance):
        account = Account(
            self.next_account_number,
            holder_name,
            initial_balance
        )

        self.accounts[self.next_account_number] = account

        print("\nAccount Created Successfully!")
        print(f"Account Number : {self.next_account_number}")

        self.next_account_number += 1


    def search_account(self, account_number):
        return self.accounts.get(account_number)

    

    def deposit(self, account_number, amount):
        account = self.search_account(account_number)

        if not account:
            raise AccountNotFoundError("Account not found.")

        account.deposit(amount)

    
    def withdraw(self, account_number, amount):
        account = self.search_account(account_number)

        if not account:
            raise AccountNotFoundError("Account not found.")

        account.withdraw(amount)

    def check_balance(self, account_number):
        account = self.search_account(account_number)

        if not account:
            raise AccountNotFoundError("Account not found.")

        account.check_balance()

    def view_all_accounts(self):
        if not self.accounts:
            print("No Accounts Available.")
            return

        for account in self.accounts.values():
            account.display_account()

    def delete_account(self, account_number):
        if account_number not in self.accounts:
            raise AccountNotFoundError("Account not found.")

        del self.accounts[account_number]
        print("Account deleted successfully.")
    
    