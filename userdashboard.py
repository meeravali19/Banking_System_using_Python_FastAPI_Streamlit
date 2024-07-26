import streamlit as st
from streamlit_option_menu import option_menu
import requests
from datetime import datetime

# Set up page layout
st.set_page_config(page_title="Bank User Dashboard", layout="wide")
def show_user_dashboard():
# Sidebar navigation
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",  # required
            options=["Dashboard", "Deposit", "Withdraw", "Mini Statement", "Pin Change", "Balance Enquiry", "Exit"],  # required
            icons=["house", "arrow-down-circle", "arrow-up-circle", "file-earmark-text", "key", "info-circle", "box-arrow-right"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
        )
    if selected == "Dashboard":
        st.title("Welcome to online banking")
        st.title("User Dashboard")
    
    # Access the cardnumber from session state
        if 'cardnumber' in st.session_state:
            cardnumber = st.session_state.cardnumber
            st.write(f"Welcome, User {cardnumber}")
        
    if selected =="Deposit":
        st.title("Banking System - Deposit")

        pinnumber = st.text_input("Pin Number", type="password")
        amount = st.number_input("Deposit Amount", min_value=0.0, format="%.2f")

        if st.button("Deposit"):
            response = requests.post(
                "http://localhost:8000/deposit",
                json={"pinnumber": pinnumber, "amount": amount}
            )
            if response.status_code == 200:
                st.success(f"Deposit successful! New balance: ${response.json()['balance']:.2f}")
            else:
                st.error(f"Error: {response.json()['balance']}")
    if selected=='Withdraw':
        st.title("Banking System - Withdrawal")

        pinnumber = st.text_input("Pin Number", type="password")
        amount = st.number_input("Withdrawal Amount", min_value=0.0, format="%.2f")

        if st.button("Withdraw"):
            response = requests.post(
                "http://localhost:8000/withdraw",
                json={"pinnumber": pinnumber, "amount": amount}
            )
            if response.status_code == 200:
                st.success(f"Withdrawal successful! New balance: ${response.json()['balance']:.2f}")
            else:
                st.error(f"Error: {response.json()['detail']}")
    if selected=='Mini Statement':
        st.title("Banking System - Mini Statement")

        pinnumber = st.text_input("Pin Number", type="password")

        if st.button("Get Mini Statement"):
            response = requests.post(
                "http://localhost:8000/mini-statement",
                json={"pinnumber": pinnumber}
            )
            if response.status_code == 200:
                transactions = response.json()['transactions']
                if transactions:
                    st.write("Recent Transactions:")
                    for txn in transactions:
                        amount = txn['amount']
                # Convert timestamp string to datetime object
                        method=txn['transaction_type']
                        timestamp = datetime.strptime(txn['timestamp'], '%Y-%m-%dT%H:%M:%S')
                        st.write(f"Amount: ${amount:.2f}, Date: {timestamp.strftime('%Y-%m-%d %H:%M:%S')},Method: {method}")
                else:
                    st.write("No recent transactions.")
            else:
                st.error(f"Error: {response.json()['detail']}")
    if selected=='Pin Change':
        st.title("Banking System - Change PIN")

        current_pin = st.text_input("Current PIN Number", type="password")
        new_pin = st.text_input("New PIN Number", type="password")

        if st.button("Change PIN"):
            response = requests.post(
                "http://localhost:8000/change_pin",
                json={"current_pin": current_pin, "new_pin": new_pin}
            )
            if response.status_code == 200:
                st.success("PIN change successful!")
            else:
                st.error(f"Error: {response.json()['message']}")
    if selected=='Balance Enquiry':
        st.title("Banking System - Balance Inquiry")

# Input field for PIN number
        pin_number = st.text_input("PIN Number", type="password")

        # Button to trigger the balance inquiry
        if st.button("Check Balance"):
            # Sending a POST request to the balance inquiry endpoint
            response = requests.post(
                "http://localhost:8000/balance_inquiry",
                json={"pinnumber": pin_number}
            )
            
            # Handling the response
            if response.status_code == 200:
                balance = response.json().get('balance', 'N/A')
                st.success(f"Your balance is: {balance}")
            else:
                st.error(f"Error: {response.json()['detail']}")
    if selected=='Exit':
        st.session_state.logged_in=False
        st.experimental_rerun()