from pydantic import BaseModel

class Patient(BaseModel):

    name : str
    age: int
    weight : float

def insert_patient(patient : Patient):

    print(patient.name)
    print(patient.age)
    print("Data Inserted")    


patient_info = {'name' : 'Mayank', 'age':21}

patient1= Patient(**patient_info)

insert_patient(patient1)