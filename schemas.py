from pydantic import BaseModel
from datetime import date


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

    class Config:
        orm_mode = True

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

    class Config:
        orm_mode = True
        
class Signup2(BaseModel):
    formno: str
    accounttype: str
    services: str
    cardnumber: str
    pinnumber: str
    balance:float
    
    class Config:
        orm_mode = True
        
class Bank(BaseModel):
    id: int
    cardnumber: str
    date:date
    transaction_type:str
    balance:float
    
    class Config:
        orm_mode=True
    
class Trasaction(BaseModel):
    id:str
    
class AdminLogin(BaseModel):
    username: str
    password: str
