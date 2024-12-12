from fastapi import FastAPI
from models.prediction import predict
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from models.prediction_service import get_prediction

app = FastAPI()

# Create a Pydantic model for request validation
class PredictionRequest(BaseModel):
    year: int
    month: int

@app.post("/predict")
async def make_prediction(request: PredictionRequest):
    year = request.year
    month = request.month
    result = await get_prediction(year, month)
    return JSONResponse(content=result)

@app.get("/")
async def read_root():
    return {"message": "DPS Munich AI Challenge!"}
