from pydantic import BaseModel
from typing import Optional


class CategoriesBase(BaseModel):
    title: str
    description: Optional[str]
    
        

class Categoriescreate(CategoriesBase):
    pass

class Categories(CategoriesBase):
    id : int
    title: str
    description: str | None = None
    
    class Config:
        orm_mode = True
        
        
        
        
class PersonalProfileBase(BaseModel):
    first_name: str
    second_name: str
    date_of_birth: str
    location : str
    profession:str
    other_personal_details: str | None = None 
    category: Categories
 
    
class Patients(PersonalProfileBase):
    id : int 
    treattment_status : str | None = None
    
    class Config:
        orm_mode = True
    
class Doctor(PersonalProfileBase):
    id : int 
    hospital_of_work: str | None = None

    class Config:
        orm_mode = True
        
class PatientCreate(PersonalProfileBase):
    treattment_status : str | None = None
    
class DoctorCreate(PersonalProfileBase):
    hospital_of_work : str | None = None


    
    
        
    
    
    
        
        