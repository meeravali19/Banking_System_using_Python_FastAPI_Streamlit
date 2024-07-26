import streamlit as st
from streamlit_option_menu import option_menu
import requests
from userdashboard import show_user_dashboard
from admindashboard import show_admin_dashboard
from faq import faq

API_URL = "http://localhost:8000"

# Define the navigation menu

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'admin_logged_in' not in st.session_state:
    st.session_state.admin_logged_in = False
    
def main_menu():
    with st.sidebar:
        selected = option_menu(
            "Main Menu",
            ["Login", "Signup","About-Us","FAQ"],
            icons=["box-arrow-in-right", "person-plus", "info-circle", "question-circle"],
            menu_icon="cast",
            default_index=0,
        )
    return selected

def login_page():
    # Initialize session state if not already present
    if 'login_type' not in st.session_state:
        st.session_state.login_type = 'user'

    # Define function to switch login type
    def switch_login_type(login_type):
        st.session_state.login_type = login_type

    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .login-container {
            background: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 10px;
            max-width: 400px;
            margin: auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Login Page")

    # Display buttons side by side using columns
    col1, col2 = st.columns(2)

    with col1:
        if st.button("User Login"):
            switch_login_type('user')

    with col2:
        if st.button("Admin Login"):
            switch_login_type('admin')

    # Login form container
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    if st.session_state.login_type == 'user':
        st.header("User Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            # Sending the login request to your API
            response = requests.post(f"{API_URL}/userlogin", json={
                "cardnumber": username,
                "pinnumber": password
            })
            
            # Checking the response status
            if response.status_code == 200:
                st.session_state.logged_in = True
                st.session_state.cardnumber = username # Set the login status
                st.experimental_rerun()  # Refresh to show dashboard
            else:
                st.error("Login failed. Please check your username and password.")
    else:
        st.header("Admin Login")
        admin_username = st.text_input("Admin Username")
        admin_password = st.text_input("Admin Password", type="password")
        if st.button("Login"):
            # Sending the login request to your API
            response = requests.post(f"{API_URL}/adminlogin", json={
                "username": admin_username,
                "password": admin_password
            })
            
            # Checking the response status
            if response.status_code == 200:
                st.session_state.username = admin_username
                st.session_state.admin_logged_in = True  # Set admin login status
                st.experimental_rerun()  # Refresh to show dashboard
            else:
                st.error("Login failed. Please check your username and password.")
    st.markdown('</div>', unsafe_allow_html=True)

# Main logic


if st.session_state.logged_in:
    show_user_dashboard()
elif st.session_state.admin_logged_in:
    show_admin_dashboard()
else:
    selected = main_menu()
    if selected == "Login":
        login_page()
    elif selected == "Signup":
        exec(open("signup.py").read())  # Note: Consider refactoring for better security and maintainability
    elif selected=="About-Us":
        st.title("About Us")

        st.write(
            """
            Welcome to our online banking application!

            **Our Mission**:
            To provide a seamless and secure banking experience for all users. We are committed to delivering innovative solutions that cater to your financial needs and simplify your banking tasks.

            **Our Features**:

            - **Dashboard**:
            The central hub of our application where users can view their account summary, recent transactions, and other important information at a glance.

            - **Deposit**:
            A convenient feature that allows users to deposit funds into their accounts quickly and securely. Simply enter your PIN and the amount you wish to deposit, and the transaction will be processed promptly.

            - **Withdraw**:
            Withdraw funds from your account with ease. Enter your PIN and the amount you wish to withdraw, and the application will handle the rest. Keep track of your withdrawals with real-time updates on your balance.

            - **Mini Statement**:
            Get a snapshot of your recent transactions with the Mini Statement feature. View details of your latest activities, including the transaction amount, date, and method, helping you keep track of your spending.

            - **Pin Change**:
            Update your PIN securely through our Pin Change feature. Enter your current PIN and the new PIN you wish to set, and the application will ensure your new PIN is updated securely.

            - **Balance Enquiry**:
            Check your account balance anytime. Enter your PIN to view your current balance, ensuring you are always informed of your financial status.

            - **Admin Dashboard**:
            For administrators, our Admin Dashboard offers comprehensive management tools. Admins can add new users, view user information, and delete users as needed. It provides an easy interface for managing user accounts and monitoring application activity.

            - **User Management**:
            Admins can add new users, view detailed user profiles, and delete user accounts. This feature allows for efficient management of user data and ensures smooth operation of the application.

            - **Security Measures**:
            Our application employs advanced security protocols to protect your personal and financial information. We use encryption to secure your data, and our systems are regularly updated to safeguard against potential threats.

            **Our Team**:
            We are a dedicated team of professionals with extensive experience in banking and technology. Our goal is to make banking easier and more accessible through our user-friendly platform. We strive to continuously improve our services based on user feedback and technological advancements.

            **Contact Us**:
            If you have any questions or feedback, please reach out to us at:
            - **Email**: support@onlinebanking.com
            - **Phone**: +123 456 7890
            - **Address**: 123 Bank Street, FinCity, FC 12345

            Thank you for choosing our service. We look forward to serving you!
            """
        )
    elif selected=="FAQ":
        faq()
        
    