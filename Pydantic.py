from pydantic import BaseModel, AnyUrl, EmailStr, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name : Annotated[str, Field(max_length=50, title='Name of the patient', description='less than 50 chars', examples=['mayank', 'goyal'])]
    age: int = Field( gt=0, lt=120)
    weight : Annotated[float,Field(gt=0, strict=True)] 
    linkedin_url : Annotated[AnyUrl, Field(default=None)]
    married : Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies : Optional[List[str]] = None
    contact_details : Dict[str, str]

def insert_patient(patient : Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("Data Inserted")    

def update_patient(patient : Patient):

    print(patient.name)
    print(patient.age)
    print("Updated")    


patient_info = {'name' : 'Mayank', 'age':21, 'weight' : 65.3, 'married':True, 
                'contact_details':{'email':'goyalmayank@gmail.com','Mob No': '43413'}}

patient1= Patient(**patient_info)

insert_patient(patient1)