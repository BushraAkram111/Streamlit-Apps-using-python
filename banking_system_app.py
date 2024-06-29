import streamlit as st

class Account:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"
        return "Invalid withdrawal amount or insufficient funds"

    def check_balance(self):
        return f"Current balance: ${self.balance:.2f}"

class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder):
        if account_number in self.accounts:
            return "Account number already exists"
        self.accounts[account_number] = Account(account_number, account_holder)
        return f"Account created for {account_holder} with account number {account_number}"

    def get_account(self, account_number):
        return self.accounts.get(account_number)

# Create an instance of the banking system
banking_system = BankingSystem()

st.title("Simple Banking System")

menu = ["Create Account", "Deposit Money", "Withdraw Money", "Check Balance"]
choice = st.sidebar.selectbox("Menu", menu)

account_number = st.text_input("Account Number")

if choice == "Create Account":
    st.subheader("Create Account")
    account_holder = st.text_input("Account Holder")
    if st.button("Create"):
        st.success(banking_system.create_account(account_number, account_holder))

elif choice in ["Deposit Money", "Withdraw Money"]:
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    if st.button("Deposit" if choice == "Deposit Money" else "Withdraw"):
        account = banking_system.get_account(account_number)
        if account:
            if choice == "Deposit Money":
                st.success(account.deposit(amount))
            else:
                st.success(account.withdraw(amount))
        else:
            st.error("Account not found")

elif choice == "Check Balance":
    if st.button("Check"):
        account = banking_system.get_account(account_number)
        if account:
            st.success(account.check_balance())
        else:
            st.error("Account not found")
