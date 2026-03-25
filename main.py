import streamlit as st

# 1. Your Original Class (No changes needed to logic)
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited Rs.{amount}. Balance available: Rs.{self.__balance}", True
        return "Invalid deposit amount.", False

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                return f"Withdrew Rs.{amount}. Balance available: Rs.{self.__balance}", True
            return "Insufficient funds!", False
        return "Invalid withdrawal amount.", False

    def get_balance(self):
        return self.__balance

# 2. Setup Session State (This replaces your first 'while True' loop)
st.title("🏦 Custom Bank Simulator")

if 'user_account' not in st.session_state:
    st.subheader("Create New Account")
    name = st.text_input("Enter account holder's name:")
    initial_dep = st.number_input("Enter initial deposit:", min_value=0.0, step=100.0)
    
    if st.button("Open Account"):
        if name:
            # Save the class instance into session state
            st.session_state.user_account = BankAccount(name, initial_dep)
            st.rerun()
        else:
            st.warning("Please enter a name.")
else:
    # 3. The App Interface (This replaces your second 'while True' loop)
    acc = st.session_state.user_account
    
    st.sidebar.header(f"Welcome, {acc.account_holder}")
    st.sidebar.metric("Current Balance", f"Rs.{acc.get_balance():,.2f}")
    
    choice = st.radio("Choose an Action:", ["Deposit", "Withdraw", "Check Balance"])

    if choice == "Deposit":
        amount = st.number_input("Amount to Deposit:", min_value=0.0, step=50.0)
        if st.button("Submit Deposit"):
            msg, success = acc.deposit(amount)
            if success: st.success(msg)
            else: st.error(msg)
            st.rerun()

    elif choice == "Withdraw":
        amount = st.number_input("Amount to Withdraw:", min_value=0.0, step=50.0)
        if st.button("Submit Withdrawal"):
            msg, success = acc.withdraw(amount)
            if success: st.warning(msg)
            else: st.error(msg)
            st.rerun()

    elif choice == "Check Balance":
        st.info(f"Account Holder: **{acc.account_holder}**")
        st.write(f"Total Funds Available: **Rs.{acc.get_balance()}**")

    # Option to Reset/Exit
    if st.sidebar.button("Close/Reset Session"):
        del st.session_state.user_account
        st.rerun()
