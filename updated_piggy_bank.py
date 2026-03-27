import streamlit as st

st.title("The Pocket Piggy Bank")

if "balance" not in st.session_state:
    st.session_state.balance = 0.0

if "history" not in st.session_state:
    st.session_state.history = []


st.metric(label="Current Balance", value=f"${st.session_state.balance:.2f}")

amount = st.number_input("Enter an amount:" , value=0.0, step=1.0, key="amount_input")

col1, col2 = st.columns(2)

with col1:
    if st.button("Add to Piggy Bank"):
        st.session_state.balance += amount
        st.toast(f"Added ${amount:.2f} to the piggy bank!")
        st.session_state.history.append(f"📥 Added: ${amount:.2f}")
        st.rerun() 

with col2:
    if st.button("Withdraw from Piggy Bank"):
        if amount > st.session_state.balance:
            st.error("Insufficient funds in the piggy bank!")
        else:
            st.session_state.balance -= amount
            st.toast(f"Withdrew ${amount:.2f} from the piggy bank!")
            st.session_state.history.append(f"📤 Withdrew: ${amount:.2f}")
            st.rerun() 

# st.metric(label="Current Balance", value=f"${st.session_state.balance:.2f}")

st.subheader("📜 Transaction History")

for transaction in reversed(st.session_state.history):
    st.write(transaction)

if st.button("Clear History"):
    st.session_state.history = []
    st.rerun()