import streamlit as st

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance
        self.history = []  # Added history inside the class!

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            msg = f"➕ :green[Deposited Rs.{amount}. Balance: Rs.{self.__balance}]"
            self.history.append(msg)
            return msg, True
        return "Invalid amount.", False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            msg = f"➖ :red[Withdrew Rs.{amount}. Balance: Rs.{self.__balance}]"
            self.history.append(msg)
            return msg, True
        return "Insufficient funds or invalid amount.", False

    def get_balance(self):
        return self.__balance


# --- SESSION STATE CHECK ---
# If the account doesn't exist yet, create it once.
if "my_acc" not in st.session_state:
    st.session_state.my_acc = BankAccount("John Doe", 1000.0)

# Create a shorthand variable for easy typing
acc = st.session_state.my_acc

# --- THE UI ---
st.title(f"{acc.account_holder}'s Bank")
# st.metric("Total Balance", f"Rs. {acc.get_balance():,.2f}")

amount = st.number_input("Transaction Amount:", min_value=0.0, step=100.0)

col1, col2 = st.columns(2)

with col1:
    if st.button("Deposit"):
        msg, success = acc.deposit(amount)
        if success: 
            st.toast(msg)
        else: 
            st.error(msg)
        # st.rerun() # Refresh to update the metric at the top

with col2:
    if st.button("Withdraw"):
        msg, success = acc.withdraw(amount)
        if success: 
            st.toast(msg)
        else: 
            st.error(msg)
        # st.rerun()

# 3. DISPLAY UPDATED NUMBERS THIRD (This ensures the metric is always current)
st.metric("Total Balance", f"Rs. {acc.get_balance():,.2f}")

# --- DISPLAY HISTORY FROM THE CLASS ---
st.subheader("History")
with st.container(border=True):
    if not acc.history:
        st.write("No transactions yet.")
    for log in reversed(acc.history):
        st.markdown(log)