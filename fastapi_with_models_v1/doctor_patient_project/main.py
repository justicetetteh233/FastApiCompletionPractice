import schemas
from fastapi import FastAPI, HTTPException,Depends,status
from sqlalchemy.orm import Session
import crud, models
from databaseconnector import sessionLocal, engine 
models.Base.metadata.create_all(bind=engine)
import routers


app = FastAPI()


# # Dependency
# def get_db():
#     db = sessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post("/categories/",status_code=status.HTTP_201_CREATED)
# async def create_category(category:schemas.Categoriescreate, db: Session = Depends(get_db)):
#     return crud.create_category(db=db , category= category)

# @app.post("/Patients/",status_code=status.HTTP_201_CREATED)
# async def create_patient(patient:schemas.PatientCreate, db: Session = Depends(get_db)):
#     return crud.create_patient(db = db, patient = patient )


# @app.post("/doctors/",status_code=status.HTTP_201_CREATED)
# async def create_doctor(doctor:schemas.DoctorCreate, db: Session = Depends(get_db)):
#     return crud.create_doctor(db = db, doctor= doctor)

# @app.get("/getcategories_by_id/{category_id}", status_code= status.HTTP_200_OK)
# async def get_categories(category_id : int ,db: Session = Depends(get_db) ):
#     return crud.get_category_by_id(db=db  ,category_id= category_id)

# @app.get("/get_patient_by_id/{patient_id}", status_code= status.HTTP_200_OK)
# async def get_patient_by_id(patient_id : int ,db: Session = Depends(get_db) ):
#     return crud.get_patient_by_id(db=db  ,patient_id= patient_id)

# @app.get("/get_doctor_by_id/{doctor_id}", status_code= status.HTTP_200_OK)
# async def get_patient_by_id(doctor_id : int ,db: Session = Depends(get_db) ):
#     return crud.get_doctor_by_id(db=db, doctor_id= doctor_id)


app.include_router(routers.app)
