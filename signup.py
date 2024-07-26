import streamlit as st
import requests
import random
import datetime

API_URL = "http://localhost:8000"

def signup():
    st.title("Application Form")

    if "step" not in st.session_state:
        st.session_state.step = 1

    if st.session_state.step == 1:
        signup_page1()
    elif st.session_state.step == 2:
        signup_page2()
    elif st.session_state.step == 3:
        signup_page3()

def signup_page1():
    st.subheader("Page 1: Personal Details")

    random_long = random.randint(-9223372036854775808, 9223372036854775807)
    random_number = abs((random_long % 9000) + 1000)
    st.session_state.formno = str(random_number)
    st.write(f"Application Form NO. {random_number}")

    st.session_state.name = st.text_input("Name")
    st.session_state.fname = st.text_input("Father Name")
    st.session_state.dob = st.date_input("Date Of Birth", datetime.date(2000, 1, 1))
    st.session_state.gender = st.radio("Gender", ("Male", "Female"))
    st.session_state.email = st.text_input("E-mail")
    st.session_state.marital_status = st.radio("Marital Status", ("Married", "Unmarried", "Others"))
    st.session_state.address = st.text_input("Address")
    st.session_state.city = st.text_input("City")
    st.session_state.state = st.text_input("State")
    st.session_state.pincode = st.text_input("Pin Code")

    if st.button("Next"):
        if not st.session_state.name:
            st.error("Name is required")
        else:
            response = requests.post(f"{API_URL}/signup", json={
                "formno": st.session_state.formno,
                "name": st.session_state.name,
                "fname": st.session_state.fname,
                "dob": st.session_state.dob.isoformat(),
                "gender": st.session_state.gender,
                "email": st.session_state.email,
                "marital_status": st.session_state.marital_status,
                "address": st.session_state.address,
                "city": st.session_state.city,
                "state": st.session_state.state,
                "pincode": st.session_state.pincode,
            })
            if response.status_code == 200:
                st.session_state.step = 2
                st.rerun()
            else:
                st.error("An error occurred")

def signup_page2():
    st.subheader("Page 2: Additional Details")

    st.session_state.religion = st.selectbox("Religion", ["Hindu", "Muslim", "Sikh", "Christian", "Others"])
    st.session_state.category = st.selectbox("Category", ["General", "OBC", "SC", "ST", "Others"])
    st.session_state.income = st.selectbox("Income", ["NULL", "< 1,50,000", "< 2,50,000", "< 3,50,000", "< 5,00,000", "upto 10,00,000"])
    st.session_state.education = st.selectbox("Educational Qualification", ["Non-Graduation", "Graduation", "Post-Graduation", "PHD", "Others"])
    st.session_state.occupation = st.selectbox("Occupation", ["Salaried", "Self-Employed", "Business", "Student", "Retired"])
    st.session_state.pan = st.text_input("Pan Number")
    st.session_state.aadhar = st.text_input("Aadhar Number")
    st.session_state.senior_citizen = st.radio("Senior Citizen", ["Yes", "No"])
    st.session_state.existing_account = st.radio("Existing Account", ["Yes", "No"])

    if st.button("Next"):
        if not st.session_state.religion:
            st.error("Religion is required")
        else:
            response = requests.post(f"{API_URL}/signup1", json={
                "formno": st.session_state.formno,
                "religion": st.session_state.religion,
                "category": st.session_state.category,
                "income": st.session_state.income,
                "education": st.session_state.education,
                "occupation": st.session_state.occupation,
                "pan": st.session_state.pan,
                "aadhar": st.session_state.aadhar,
                "senior_citizen": st.session_state.senior_citizen,
                "existing_account": st.session_state.existing_account,
            })
            if response.status_code == 200:
                st.session_state.step = 3
                st.rerun()
            else:
                st.error("An error occurred")

    if st.button("Back"):
        st.session_state.step = 1
        st.experimental_rerun()

def signup_page3():
    st.subheader("Page 3: Account Details")

    st.session_state.account_type = st.radio(
        "Account Type",
        ["Saving Account", "Fixed Deposit Account", "Current Account", "Recurring Deposit Account"]
    )
    st.session_state.services = st.multiselect(
        "Services Required",
        ["ATM CARD", "Internet Banking", "Mobile Banking", "Email & Sms Alerts", "Cheque Book", "E-Statement"]
    )
    st.session_state.declaration = st.checkbox("I hereby declare that the above entered details are to the best of my knowledge.")

    if st.button("Submit"):
        if not st.session_state.account_type:
            st.error("Account Type is required")
        elif not st.session_state.declaration:
            st.error("Please check the Declaration box")
        else:
            random_long = random.randint(-9223372036854775808, 9223372036854775807)
            card_number = str(abs((random_long % 90000000) + 5040936000000000))
            pin_number = str(abs((random_long % 9000) + 1000))
            serives=str(st.session_state.services)
            response = requests.post(f"{API_URL}/signup2", json={
                "formno": st.session_state.formno,
                "accounttype":st.session_state.account_type,
                "services":serives,
                "cardnumber":card_number,
                "pinnumber":pin_number,
            })
            
            
            
            if response.status_code == 200:
                st.success(f"Form submitted successfully!\nCard Number: {card_number}\nPIN: {pin_number}")
            else:
                st.error(response.json())
                

            
    


    if st.button("Back"):
        st.session_state.step = 2
        st.rerun()

if __name__ == "__main__":
    signup()
