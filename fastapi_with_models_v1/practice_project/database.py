# to create an engine for database to communicate with our application
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# we now need a connection to our database 
URL_DATABASE = "mysql+pymysql://justice:jaycode-233@localhost:3306/PDTEST"

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit = False,autoflush = False , bind = engine)

Base = declarative_base()