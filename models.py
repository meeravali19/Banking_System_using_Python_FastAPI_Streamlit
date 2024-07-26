from sqlalchemy import Column, String, Date,Integer,DateTime,Float,Text,TIMESTAMP
from database import Base
from datetime import datetime

class Signup(Base):
    __tablename__ = "signup"
    formno = Column(String(20), primary_key=True, index=True)  
    name = Column(String(100))  # Specify length
    fname = Column(String(100))  # Specify length
    dob = Column(Date)
    gender = Column(String(10))  # Specify length
    email = Column(String(100))  # Specify length
    marital_status = Column(String(20))  # Specify length
    address = Column(String(255))  # Specify length
    city = Column(String(100))  # Specify length
    state = Column(String(100))  # Specify length
    pincode = Column(String(10))  # Specify length

class Signup1(Base):
    __tablename__ = "signup1"
    formno = Column(String(20), primary_key=True, index=True)  # Specify length
    religion = Column(String(50))  # Specify length
    category = Column(String(50))  # Specify length
    income = Column(String(50))  # Specify length
    education = Column(String(50))  # Specify length
    occupation = Column(String(50))  # Specify length
    pan = Column(String(20))  # Specify length
    aadhar = Column(String(20))  # Specify length
    senior_citizen = Column(String(10))  # Specify length
    existing_account = Column(String(10))  # Specify length

class Signup2(Base):
    __tablename__="signup2"
    formno=Column(String(20),primary_key=True,index=True)
    accounttype=Column(String(100))
    services=Column(String(200))
    cardnumber=Column(String(200))
    pinnumber=Column(String(50))
    balance = Column(Float, default=0.0)
    
    
    
    




class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    cardnumber = Column(String(200), index=True)
    amount = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    transaction_type = Column(String(50))
    
class Admin(Base):
    __tablename__ = 'admin'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password = Column(String(50))  # Store hashed password
    