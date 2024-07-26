from sqlalchemy.orm import Session
from models import Signup, Signup1, Signup2 , Admin
from schemas import Signup as SignupSchema, Signup1 as Signup1Schema, Signup2 as Signup2Schema
from sqlalchemy.orm.exc import NoResultFound

def create_signup(db: Session, signup: SignupSchema):
    db_signup = Signup(
        formno=signup.formno,
        name=signup.name,
        fname=signup.fname,
        dob=signup.dob,
        gender=signup.gender,
        email=signup.email,
        marital_status=signup.marital_status,
        address=signup.address,
        city=signup.city,
        state=signup.state,
        pincode=signup.pincode,
    )
    db.add(db_signup)
    db.commit()
    db.refresh(db_signup)
    return db_signup

def create_signup1(db: Session, signup1: Signup1Schema):
    db_signup1 = Signup1(
        formno=signup1.formno,
        religion=signup1.religion,
        category=signup1.category,
        income=signup1.income,
        education=signup1.education,
        occupation=signup1.occupation,
        pan=signup1.pan,
        aadhar=signup1.aadhar,
        senior_citizen=signup1.senior_citizen,
        existing_account=signup1.existing_account,
    )
    db.add(db_signup1)
    db.commit()
    db.refresh(db_signup1)
    return db_signup1

def create_signup2(db: Session, signup2: Signup2Schema):
    db_signup2 = Signup2(
        formno=signup2.formno,
        accounttype=signup2.accounttype,
        services=signup2.services,
        cardnumber=signup2.cardnumber,
        pinnumber=signup2.pinnumber
    
    )
    db.add(db_signup2)
    db.commit()
    db.refresh(db_signup2)
    return db_signup2

# crud.py

def get_user_by_cardnumber(db, cardnumber: str):
    # Replace with your actual query logic
    return db.query(Signup2).filter(Signup2.cardnumber == cardnumber).first()

    

def get_admin_by_username(db: Session, username: str):
    try:
        return db.query(Admin).filter(Admin.username == username).first()
    except NoResultFound:
        return None