from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# u have to create a database url to connect to your database
URL_DATABASE = "mysql+pymysql://justice:jaycode-233@localhost:3306/PDTEST2"# suppose we where using postgress creating an engine to connect ourt database toe the our fast api models will look like so 
# engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False})
# but other databases do not require the connec_args aguement 
engine = create_engine(URL_DATABASE)

# we will use session local when dealing with crud of the database 

sessionLocal = sessionmaker(autocommit= False , autoflush =False, bind = engine)

# all our database models  will inherit form  to make them connected or recognises by the sql as part of the database 
Base = declarative_base()

