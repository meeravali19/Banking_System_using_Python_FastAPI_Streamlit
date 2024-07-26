from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace 'your_password' with the actual password for the 'postgres' user
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:9490@localhost/vali"

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for our classes definitions
Base = declarative_base()
