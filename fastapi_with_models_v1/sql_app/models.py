from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from databasesconnector import Base




""" __tablename__ is used to name the table 
we use the colum to decribe what is suppose to be in the a session to the table 
the relationship is used to connect two or more tables together """
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key= True , index=True)
    email = Column (String(50),unique=True, index=True)
    hashed_password = Column(String(50))
    is_active = Column(Boolean, default= True)
    
    items= relationship("Item", back_populates="owner")
    
class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True , index=True)
    title= Column(String(50), index=True)
    description = Column(String(50), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User",back_populates="items")
    
    