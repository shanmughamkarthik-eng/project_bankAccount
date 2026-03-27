import streamlit as st

st.title("The Pocket Piggy Bank")

if "balance" not in st.session_state:
    st.session_state.balance = 0.0

st.header(f"Current Balance: ${st.session_state.balance:.2f}")

amount = st.number_input("Enter an amount to add or withdraw:", value = 0.0, step = 1.0)

if st.button("Add to Piggy Bank"):
    st.session_state.balance += amount
    st.success(f"Added ${amount:.2f} to the piggy bank!")
    st.rerun()

if st.button("Withdraw from Piggy Bank"):
    if amount > st.session_state.balance:
        st.error("Insufficient funds in the piggy bank!")
    else:
        st.session_state.balance -= amount
        st.success(f"Withdrew ${amount:.2f} from the piggy bank!")
        st.rerun()