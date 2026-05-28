from fastapi import FastAPI, Depends, HTTPException,status 
from pydantic import BaseModel
from model import train_sale_split
from preprocess import load_and_preprocess_data

import secrets
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.openapi.docs import get_swagger_ui_html

security = HTTPBasic()
def basic_auth(credentials: HTTPBasicCredentials = Depends(security)):
    user = secrets.compare_digest(credentials.username, "user_admin")
    password = secrets.compare_digest(credentials.password,"user_pass#")
    if not (user and password):
        raise HTTPException(
                 status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
            headers={"WWW-Authenticate": "Basic"} 
        )
    return credentials.username


app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

# Train model once during startup
model = train_sale_split()

class SalesInput(BaseModel):
    marketing_spend:float
    month:int
    
@app.get("/openapi.json",dependencies =[Depends(basic_auth)])
def protected_openapi():
    return app.openapi()

@app.get("/docs",dependencies =[Depends(basic_auth)])
def protected_swagger_ui():
    return get_swagger_ui_html(openapi_url="/openapi.json",title="Docs")

@app.get("/")
def home():
    return{"message":"Sales Forcasting APP Running "}

@app.get("/sales_data")
def get_sales_data():
    df = load_and_preprocess_data()
    
    return df.to_dict(orient="records")

@app.post("/predict")
def predict_sales(data: SalesInput):
    prediction = model.predict([
        [data.marketing_spend,data.month]
        ])
    
    return {
        "predicted_sales": round(float(prediction[0]), 2)
    }