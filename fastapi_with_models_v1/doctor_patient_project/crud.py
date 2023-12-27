from sqlalchemy.orm import Session
import models, schemas

def get_patient_by_id(db : Session , patient_id : int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()


def get_all_patients(db: Session, skip: int = 0 , limit: int =100):
    return db.query(models.Patient).offset(skip).limit(limit).all()


def get_doctor_by_id(db : Session , doctor_id : int):
    return db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()


def get_all_doctors(db: Session, skip: int = 0 , limit: int =100):
    return db.query(models.Doctor).offset(skip).limit(limit).all()


def get_category_by_id(db : Session , category_id : int):
    return db.query(models.Categories).filter(models.Categories.id ==category_id).first()


def get_all_categories(db: Session, skip: int = 0 , limit: int =100):
    return db.query(models.Categories).offset(skip).limit(limit).all()

def create_category(db: Session, category = schemas.Categoriescreate):
    db_category = models.Categories(title = category.title, description = category.description)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return {"title": category.title}
    
def create_patient(db: Session, patient = schemas.PatientCreate):
    db_patient = models.Patient(first_name= patient.first_name, second_name= patient.second_name, date_of_birth = patient.date_of_birth, location= patient.location, profession = patient.profession,
                                other_personal_details =patient.other_personal_details, category_id = patient.category.id, treatment_status = patient.treattment_status )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return {"firstname" : patient.first_name}

def create_doctor(db: Session, doctor = schemas.DoctorCreate):
    db_doctor = models.Doctor(first_name = doctor.first_name, second_name= doctor.second_name, date_of_birth= doctor.date_of_birth, location = doctor.location, profession = doctor.profession, other_personal_details = doctor.other_personal_details, 
                              category_id = doctor.category.id, hospital_of_work= doctor.hospital_of_work)
    
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return {"firstname" : doctor.first_name}
