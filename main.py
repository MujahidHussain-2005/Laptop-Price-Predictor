from fastapi import FastAPI
import numpy as np
from pydantic import BaseModel,computed_field,Field
from typing import Annotated
import pandas as pd
import pickle 
from fastapi.responses import JSONResponse
app=FastAPI()
with open ('model.pkl','rb') as file:
    model=pickle.load(file)

class Inputs(BaseModel):
    company: str=Field(description='laptop commpany',examples=['IBM','HP'])
    typename: str=Field(description='the type of laptop',examples=['notebook','Ultrabook'])
    inches:float=Field(gt=0,description='the screen width in inches')
    xresolution:int=Field(gt=0,description='x resolution of screen')
    yresolution:int=Field(gt=0,description='y resolution of screen')
    ram: int=Field(gt=0,description='Ram of laptop')
    weight: float=Field(gt=0,description='Weight of laptop')
    touchscreen: int=Field(description='do your laptop has touchscreen?')
    ips: int=Field(description='do your laptop has IPS screen?')
    processor: str=Field(description='processor of computer',examples=['intel core i5'])
    processor_speed: float=Field(description='speed of processor in GHZ',examples=[2.5])
    hdd:int=Field(description='do your laptop  have hdd? if yes how much if no then 0 ',examples=[128])
    ssd:int=Field(description='do your laptop  have ssd? if yes how much if no then 0 ',examples=[64])
    gpu_brand:str=Field(description='Brand of Gpu',examples=['intel','amd','etc'])
    os:str=Field(description='curent operating system of laptop',examples=['windows'])
    
    @computed_field
    @property
    def ppi(self)-> float:
        return float(((self.xresolution)**2+(self.yresolution)**2)**0.5/(self.inches))


@app.get('/Title')
def Title():
    return 'This is a Laptop Price Predictor'

@app.post('/predict')
def predict_price(inputs: Inputs):
    try:
        raw_data = inputs.model_dump()
        

        # 1. Map to your exact training column names
        formatted_data = {
            "Company": raw_data['company'],
            "TypeName": raw_data['typename'],
            "Ram": raw_data['ram'],
            "Weight": raw_data['weight'], 
            "Touchscreen": raw_data['touchscreen'],
            "IPS": raw_data['ips'],
            "PPI": raw_data['ppi'],
            "Processor": raw_data['processor'],
            "processor speed": raw_data['processor_speed'],
            "SSD": raw_data['ssd'],
            "HDD": raw_data['hdd'],
            "Gpu Brand": raw_data['gpu_brand'],
            "OS": raw_data['os']
        }

        # 2. Match the exact training column order
        column_order = [
            "Company", "TypeName", "Ram", "Weight", "Touchscreen", 
            "IPS", "PPI", "Processor", "processor speed", "SSD", 
            "HDD", "Gpu Brand", "OS"
        ]
        
        # 3. Create DataFrame and predict
        df = pd.DataFrame([formatted_data])[column_order]
        
        prediction = model.predict(df)
        
        # 4. Handle Log conversion and JSON compatibility
        # If your price is in Log form, keep np.exp. If not, remove it.
        result = float(np.exp(prediction[0])) 
        
        return JSONResponse(status_code=200,content={"predicted_price": result})

    except Exception as e:
        # This will return the actual error message (e.g., "KeyError: 'PPI'")
        return {"error_details": str(e)}
