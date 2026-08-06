from account import Account 
print("bank.py loaded")


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

        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    
    def withdraw(self, account_number, amount):
        account = self.search_account(account_number)

        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def check_balance(self, account_number):
        account = self.search_account(account_number)

        if account:
            account.check_balance()
        else:
            print("Account not found.")

    def view_all_accounts(self):
        if not self.accounts:
            print("No Accounts Available.")
            return

        for account in self.accounts.values():
            account.display_account()

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print("Account deleted successfully.")
        else:
            print("Account not found.")

    
    