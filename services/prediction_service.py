from models.prediction import predict

async def get_prediction(year: int, month: int):
    """Service to fetch the prediction."""
    result = predict(year, month)
    return result
