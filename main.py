from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List,Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import engine, SessionLocal
import models
import crud
from datetime import date

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Signup(BaseModel):
    formno: str
    name: str
    fname: str
    dob: date
    gender: str
    email: str
    marital_status: str
    address: str
    city: str
    state: str
    pincode: str

class Signup1(BaseModel):
    formno: str
    religion: str
    category: str
    income: str
    education: str
    occupation: str
    pan: str
    aadhar: str
    senior_citizen: str
    existing_account: str

class Signup2(BaseModel):
    formno: str
    accounttype: str
    services: str
    cardnumber: str
    pinnumber: str

class UserLogin(BaseModel):
    cardnumber: str
    pinnumber: str

class Deposit(BaseModel):
    pinnumber: str
    amount: float
    
class Withdraw(BaseModel):
    pinnumber: str
    amount: float
    
class PinNumber(BaseModel):
    pinnumber: str
class ChangePinRequest(BaseModel):
    current_pin: str
    new_pin: str
    
class BalanceInquiryRequest(BaseModel):
    pinnumber: str

class AdminLoginRequest(BaseModel):
    username: str
    password: str
class getuser(BaseModel):
    formno:str
class deleteuser(BaseModel):
    formno:str

class UserBase(BaseModel):
    formno: str
    name: Optional[str] = None
    fname: Optional[str] = None
    dob: Optional[str] = None
    gender: Optional[str] = None
    email: Optional[str] = None
    marital_status: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    pincode: Optional[str] = None
    religion: Optional[str] = None
    category: Optional[str] = None
    income: Optional[str] = None
    education: Optional[str] = None
    occupation: Optional[str] = None
    pan: Optional[str] = None
    aadhar: Optional[str] = None
    senior_citizen: Optional[str] = None
    existing_account: Optional[str] = None
    accounttype: Optional[str] = None
    services: Optional[str] = None
    cardnumber: Optional[str] = None
    pinnumber: Optional[str] = None
    balance: Optional[float] = None
    

    
@app.post("/signup", response_model=Signup)
def create_signup(signup: Signup):
    db = SessionLocal()
    try:
        return crud.create_signup(db=db, signup=signup)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()

@app.post("/signup1", response_model=Signup1)
def create_signup1(signup1: Signup1):
    db = SessionLocal()
    try:
        return crud.create_signup1(db=db, signup1=signup1)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()
        
@app.post("/signup2", response_model=Signup2)
def create_signup2(signup2: Signup2):
    db = SessionLocal()
    try:
        return crud.create_signup2(db=db, signup2=signup2)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()
        
@app.post("/userlogin", response_model=dict)
def user_login(userlogin: UserLogin):
    db = SessionLocal()
    try:
        user = crud.get_user_by_cardnumber(db, cardnumber=userlogin.cardnumber)
        if user is None or user.pinnumber != userlogin.pinnumber:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return {"message": "Login successful"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()

@app.post("/deposit")
def create_deposit(deposit: Deposit):
    db = SessionLocal()
    try:
        account = db.query(models.Signup2).filter(models.Signup2.pinnumber == deposit.pinnumber).first()
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")
        account.balance += deposit.amount
        transaction = models.Transaction(cardnumber=account.cardnumber,transaction_type='deposit', amount=deposit.amount)
        db.add(transaction)
        db.commit()
        db.refresh(account)
        return {"balance": account.balance}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()

@app.post("/withdraw")
def create_withdrawal(withdraw: Withdraw):
    db = SessionLocal()
    try:
        account = db.query(models.Signup2).filter(models.Signup2.pinnumber == withdraw.pinnumber).first()
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")
        if account.balance < withdraw.amount:
            raise HTTPException(status_code=400, detail="Insufficient funds")
        account.balance -= withdraw.amount
        transaction = models.Transaction(cardnumber=account.cardnumber,transaction_type='withdraw', amount=-withdraw.amount)
        db.add(transaction)
        db.commit()
        db.refresh(account)
        return {"balance": account.balance}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()
        
@app.post("/mini-statement")
def get_mini_statement(pin: PinNumber):
    db = SessionLocal()
    try:
        account = db.query(models.Signup2).filter(models.Signup2.pinnumber == pin.pinnumber).first()
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")
        
        transactions = db.query(models.Transaction).filter(models.Transaction.cardnumber == account.cardnumber).order_by(models.Transaction.timestamp.desc()).limit(10).all()
        transaction_list = [
            {
                "amount": t.amount,
                "transaction_type": t.transaction_type,  # Ensure this matches the column name in your model
                "timestamp": t.timestamp
            } for t in transactions
        ]
        
        return {"transactions": transaction_list}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        db.close()
        
@app.post("/change_pin")
async def change_pin(request: ChangePinRequest):
    db=SessionLocal()
    user = db.query(models.Signup2).filter(models.Signup2.pinnumber == request.current_pin).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="Current PIN is incorrect")
    
    user.pinnumber = request.new_pin
    try:
        db.commit()
        return {"message": "PIN change successful"}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error changing PIN")
    

@app.post("/balance_inquiry")
async def balance_inquiry(request: BalanceInquiryRequest):
    db=SessionLocal()
    pin_number = request.pinnumber
    user = db.query(models.Signup2).filter(models.Signup2.pinnumber == pin_number).first()
    if user:
        return {"balance": user.balance}
    else:
        raise HTTPException(status_code=404, detail="Account not found")
    
@app.post("/adminlogin", response_model=dict)
def admin_login(adminlogin: AdminLoginRequest):
    try:
        db=SessionLocal()
        # Fetch the admin record by username
        admin = crud.get_admin_by_username(db, username=adminlogin.username)
        
        if admin is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        # Directly compare plain text password
        if admin.password != adminlogin.password:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        return {"message": "Login successful"}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.get("/user", response_model=UserBase)
def read_user(getuser:getuser):
    db=SessionLocal()
    user = db.query(models.Signup).filter(models.Signup.formno == getuser.formno).first()
    user1 = db.query(models.Signup1).filter(models.Signup1.formno == getuser.formno).first()
    user2 = db.query(models.Signup2).filter(models.Signup2.formno == getuser.formno).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = {**user.__dict__, **user1.__dict__, **user2.__dict__}
    user_data = convert_dates_to_strings(user_data)
    user_data.pop('_sa_instance_state', None)
    return user_data

def convert_dates_to_strings(user_data):
    for key, value in user_data.items():
        if isinstance(value, date):
            user_data[key] = value.isoformat()
    return user_data




@app.delete("/user")
def delete_user(deleteuser:deleteuser):
    db = SessionLocal()
    user = db.query(models.Signup).filter(models.Signup.formno == deleteuser.formno).first()
    user1 = db.query(models.Signup1).filter(models.Signup1.formno == deleteuser.formno).first()
    user2 = db.query(models.Signup2).filter(models.Signup2.formno == deleteuser.formno).first()

    if not user or not user1 or not user2:
        db.close()
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.delete(user1)
    db.delete(user2)
    db.commit()
    db.close()

    return {"detail": "User deleted successfully"}