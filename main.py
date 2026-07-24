from fastapi import FastAPI, Path, HTTPException, Query
import json
from pydantic import BaseModel,Field, computed_field
from typing import Annotated, Literal

app = FastAPI()

class Pateint(BaseModel):

    id : Annotated[str, Field(..., description="Id of the patient", examples="P001")]
    name : Annotated[str, Field(..., description="Name of the patient")]
    city : Annotated[str, Field(..., description="City where patient live")]
    age : Annotated[int, Field(..., gt =0 , lt = 120, description="Id of the patient")]
    gender : Annotated[Literal['male', 'female', 'other'], Field(..., description="Gender of the patient")]
    height : Annotated[float, Field(..., gt=0, description="Height of the patient in mtrs")]
    weight : Annotated[float, Field(..., gt=0, description="weight of the patient in kgs")]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = self.weight / self.height * 2
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return 'UnderWeight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return 'Obese'
        
def load_data():
    with open('pateints.json', 'r') as f:
        data = json.load(f)

        return data

@app.get("/")
def hello():
    return {"message" : "Patient Management System API"}

@app.get("/about")
def about():
    return {"message" : "A fully functional API to manage your patient records"}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id : str =  Path(..., description='This is the ID of the patient in databse', example="P001")):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient Not Found")

@app.get('/sort')
def sort_patients(sort_by:str= Query(...,description='Sort on the basis of height, weight or bmi'), order: str= Query("asc", description="Sort in asc or desc")):
    
    valid_fields = ['height', 'weight','bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid Request, select form {valid_fields}')
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail=f"Invalid field, Select from {'asc','desc'}")
    data = load_data()
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key = lambda x : x.get(sort_by,0), reverse=sort_order)
    return sorted_data  
