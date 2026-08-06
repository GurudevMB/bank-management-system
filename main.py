from bank import Bank

bank = Bank()

# -----------------------------
# Create Accounts
# -----------------------------
bank.create_account("Guru", 5000)
bank.create_account("Rahul", 7000)

# -----------------------------
# View All Accounts
# -----------------------------
print("\n===== VIEW ALL ACCOUNTS =====")
bank.view_all_accounts()

# -----------------------------
# Search Account
# -----------------------------
print("\n===== SEARCH ACCOUNT =====")
account = bank.search_account(1001)

if account:
    account.display_account()
else:
    print("Account not found.")

# -----------------------------
# Deposit
# -----------------------------
print("\n===== DEPOSIT =====")
bank.deposit(1001, 2000)

# -----------------------------
# Withdraw
# -----------------------------
print("\n===== WITHDRAW =====")
bank.withdraw(1002, 1000)

# -----------------------------
# Check Balance
# -----------------------------
print("\n===== CHECK BALANCE =====")
bank.check_balance(1001)

# -----------------------------
# Delete Account
# -----------------------------
print("\n===== DELETE ACCOUNT =====")
bank.delete_account(1002)

# -----------------------------
# View All Accounts Again
# -----------------------------
print("\n===== VIEW ALL ACCOUNTS AFTER DELETE =====")
bank.view_all_accounts()