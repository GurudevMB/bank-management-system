

from bank import Bank
from exceptions import (
    InvalidAmountError,
    InsufficientFundsError,
    AccountNotFoundError
)

def display_menu():
    print("\n" + "=" * 40)
    print("      BANK MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. View All Accounts")
    print("6. Search Account")
    print("7. Delete Account")
    print("8. Exit")


def main():
    bank = Bank()

    while True:
        display_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            holder_name = input("Enter Account Holder Name: ")
            initial_balance = float(input("Enter Initial Balance: "))

            bank.create_account(holder_name, initial_balance)

            input("\nPress Enter to continue...")


        elif choice == "2":
            try:
                account_number = int(input("Enter Account Number: "))
                amount = float(input("Enter Deposit Amount: "))

                bank.deposit(account_number, amount)

            except InvalidAmountError as e:
                print(e)

            except AccountNotFoundError as e:
                print(e)

            except ValueError:
                print("Please enter a valid number.")

            input("\nPress Enter to continue...")


        elif choice == "3":
            try:
                account_number = int(input("Enter Account Number: "))
                amount = float(input("Enter Withdraw Amount: "))

                bank.withdraw(account_number, amount)

            except InvalidAmountError as e:
                print(e)

            except InsufficientFundsError as e:
                print(e)

            except ValueError:
                print("Please enter a valid number.")
            except AccountNotFoundError as e:
                print(e)

            input("\nPress Enter to continue...")



        elif choice == "4":
            try:
                account_number = int(input("Enter Account Number: "))
                bank.check_balance(account_number)

            except AccountNotFoundError as e:
                print(e)

            except ValueError:
                print("Please enter a valid account number.")

            input("\nPress Enter to continue...")



        elif choice == "5":
            bank.view_all_accounts()
            input("\nPress Enter to continue...")



        elif choice == "6":
            try:
                account_number = int(input("Enter Account Number: "))

                account = bank.search_account(account_number)

                if not account:
                    raise AccountNotFoundError("Account not found.")

                account.display_account()

            except AccountNotFoundError as e:
                print(e)

            except ValueError:
                print("Please enter a valid account number.")

            input("\nPress Enter to continue...")

        elif choice == "7":
            try:
                account_number = int(input("Enter Account Number: "))
                bank.delete_account(account_number)

            except AccountNotFoundError as e:
                print(e)

            except ValueError:
                print("Please enter a valid account number.")

            input("\nPress Enter to continue...")



        
        elif choice == "8":
            print("\nThank you for using Bank Management System!")
            break

        else:
            print("\nInvalid Choice! Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()