from fastapi import FastAPI
from .schemas import HouseData
from .model_loader import model, scaler
from .database import SessionLocal, engine
from .models import Prediction, Base

import numpy as np

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

@app.post("/predict")
def predict(data: HouseData):
    db = SessionLocal()
    try:
        # Convert input to array (Boston features: 13)
        input_data = np.array([
            data.CRIM,
            data.ZN,
            data.INDUS,
            data.CHAS,
            data.NOX,
            data.RM,
            data.AGE,
            data.DIS,
            data.RAD,
            data.TAX,
            data.PTRATIO,
            data.B,
            data.LSTAT
        ]).reshape(1, -1)

        # Scale
        scaled_data = scaler.transform(input_data)

        # Predict
        prediction = model.predict(scaled_data)[0]
        prediction = float(prediction)

        # Save to DB
        record = Prediction(
            crim=data.CRIM,
            zn=data.ZN,
            indus=data.INDUS,
            chas=data.CHAS,
            nox=data.NOX,
            rm=data.RM,
            age=data.AGE,
            dis=data.DIS,
            rad=data.RAD,
            tax=data.TAX,
            ptratio=data.PTRATIO,
            b=data.B,
            lstat=data.LSTAT,
            predicted_price=prediction
        )

        db.add(record)
        db.commit()

        return {"predicted_price": prediction}
    finally:
        db.close()
