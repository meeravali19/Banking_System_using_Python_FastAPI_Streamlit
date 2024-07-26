import streamlit as st
from streamlit_option_menu import option_menu
import requests
from datetime import datetime
import signup
import json


BASE_URL = "http://127.0.0.1:8000"

def show_admin_dashboard():
# Sidebar navigation
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",  # required
            options=["Dashboard", "Add New Users", "view User Information", "Delete Users","Exit"],  # required
            icons=["bar-chart", "person-add", "info-circle", "trash",  "door-closed"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
        )
    if selected == "Dashboard":
        st.title("Welcome to online banking")
        #st.title("admin Dashboard")
    
    # Access the cardnumber from session state
        if 'username' in st.session_state:
            username = st.session_state.username
            st.write(f"Welcome, {username}!")
    if selected=="Add New Users":
        signup.signup()
    if selected=="view User Information":
        st.title("View User Information")

        formno = st.text_input("Enter Form Number")

        if st.button("Fetch User Information"):
            response = requests.get(f"{BASE_URL}/user", json={"formno": formno})
            if response.status_code == 200:
                user_data = response.json()
            else:
                st.error("Failed to fetch user data")
                user_data = None
            
            if user_data:
                dob_str = user_data.get("dob", "")
                dob = datetime.strptime(dob_str, "%Y-%m-%d").date() if dob_str else None

                name = st.text_input("Name", user_data.get("name", ""))
                fname = st.text_input("Father's Name", user_data.get("fname", ""))
                dob = st.date_input("Date of Birth", dob)
                gender = st.selectbox("Gender", ["Male", "Female", "Other"], index=["Male", "Female", "Other"].index(user_data.get("gender", "Male")))
                email = st.text_input("Email", user_data.get("email", ""))
                marital_status = st.text_input("Marital Status", user_data.get("marital_status", ""))
                address = st.text_area("Address", user_data.get("address", ""))
                city = st.text_input("City", user_data.get("city", ""))
                state = st.text_input("State", user_data.get("state", ""))
                pincode = st.text_input("Pincode", user_data.get("pincode", ""))
                religion = st.text_input("Religion", user_data.get("religion", ""))
                category = st.text_input("Category", user_data.get("category", ""))
                income = st.text_input("Income", user_data.get("income", ""))
                education = st.text_input("Education", user_data.get("education", ""))
                occupation = st.text_input("Occupation", user_data.get("occupation", ""))
                pan = st.text_input("PAN", user_data.get("pan", ""))
                aadhar = st.text_input("Aadhar", user_data.get("aadhar", ""))
                senior_citizen = st.text_input("Senior Citizen", user_data.get("senior_citizen", ""))
                existing_account = st.text_input("Existing Account", user_data.get("existing_account", ""))
                accounttype = st.text_input("Account Type", user_data.get("accounttype", ""))
    
    
    if selected=="Delete Users":
        st.title("Delete User")

# Input for Form Number or User ID
        formno = st.text_input("Enter Form Number of the User to Delete")

        # Fetch User Information Button
        if st.button("Fetch User Information"):
            if formno:
                response = requests.get(f"{BASE_URL}/user", json={"formno": formno})
                if response.status_code == 200:
                    user_data = response.json()
                    st.write(f"User Information: {user_data}")
                else:
                    st.error("Failed to fetch user data or user not found.")
            else:
                st.error("Please enter a Form Number.")

        # Delete User Button
        if st.button("Delete User"):
            
            if formno:
                response = requests.delete(f"{BASE_URL}/user", json={"formno": formno})
                if response.status_code == 200:
                    st.success("User deleted successfully.")
                else:
                    st.error(f"Failed to delete user: {response.text}")
            else:
                st.error("Please enter a Form Number.")
    if selected=="Exit":
        st.session_state.admin_logged_in=False
        st.rerun()

                