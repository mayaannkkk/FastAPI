from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_valdator(cls, value):
        valid_domain = ['hdfc.com', 'icici.com']
        # extract last part of the email Ex = [gmail.com, outlook.com]
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domain:
            raise ValueError('Not a valid domain')
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'mayank', 'email':'abc@icici.com', 'age': '30', 'weight': 65.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462'}}

patient1 = Patient(**patient_info) # validation -> type coercion

update_patient_data(patient1)