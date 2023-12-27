from sqlalchemy  import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm  import sessionmaker

database_url = "mysql+pymysql://justice:jaycode-233@localhost:3306/PDTEST3"
engine = create_engine(database_url)
sessionLocal = sessionmaker(autocommit= False, autoflush= False, bind=engine)
Base = declarative_base()

# Base.metadata.create_all(bind=engine)

def init_db():
    # Additional initialization logic if needed
    pass

# Call init_db() when starting your application
init_db()