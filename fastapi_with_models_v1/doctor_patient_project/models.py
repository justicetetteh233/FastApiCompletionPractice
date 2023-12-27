from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from databaseconnector import Base
from sqlalchemy.orm import relationship


class Categories(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(50), unique=True, index=True)
    description = Column(String(50))

    patients = relationship("Patient", back_populates="category", uselist=False, cascade="all, delete-orphan")
    doctor = relationship("Doctor", back_populates="category", uselist=False, cascade="all, delete-orphan")


class Patient(Base):
    __tablename__ = "patients"

    first_name = Column(String(50))
    second_name = Column(String(50))
    date_of_birth = Column(String(50))
    location = Column(String(50))
    profession = Column(String(50))
    other_personal_details = Column(String(50))

    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"))
    category = relationship("Categories", back_populates="patients")

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    treatment_status = Column(String(50))


class Doctor(Base):
    __tablename__ = "doctor"

    first_name = Column(String(50))
    second_name = Column(String(50))
    date_of_birth = Column(String(50))
    location = Column(String(50))
    profession = Column(String(50))
    other_personal_details = Column(String(50))

    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"))
    category = relationship("Categories", back_populates="doctor")

    id = Column(Integer, primary_key=True, index=True ,autoincrement=True )
    hospital_of_work = Column(String(50))
