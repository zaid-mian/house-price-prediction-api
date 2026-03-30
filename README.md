
# Boston House Price Prediction API

This project provides a FastAPI-based REST API to predict house prices using a Linear Regression model trained on the Boston Housing dataset. It includes data validation with Pydantic and database persistence with SQLAlchemy.

## Project Structure

- `app/`: Contains the FastAPI application code.
  - `main.py`: Entry point for the FastAPI application.
  - `models.py`: SQLAlchemy database models.
  - `schemas.py`: Pydantic models for request/response validation.
  - `database.py`: Database connection and session configuration.
  - `model_loader.py`: Utility to load the trained ML model and scaler.
- `model/`: Contains the Jupyter Notebook for model training and analysis.
  - `Linear Regression ML Implementation.ipynb`: Training script for the Linear Regression model.
- `regmodel.pkl`: The serialized Linear Regression model.
- `scaling.pkl`: The serialized StandardScaler for feature normalization.

## Requirements

The project dependencies are listed in `requirement.txt`:
- fastapi
- uvicorn
- sqlalchemy
- pydantic
- scikit-learn
- pandas
- numpy
- psycopg2-binary (for PostgreSQL support)

## Setup and Running

1. **Install Dependencies**:
   ```bash
   pip install -r requirement.txt
   ```

2. **Database Configuration**:
   Update the `DATABASE_URL` in `app/database.py` to point to your PostgreSQL instance.

3. **Run the API**:
   From the project root directory, run:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

## API Usage

### Predict House Price

**Endpoint**: `POST /predict`

**Request Body**:
```json
{
  "CRIM": 0.00632,
  "ZN": 18.0,
  "INDUS": 2.31,
  "CHAS": 0.0,
  "NOX": 0.538,
  "RM": 6.575,
  "AGE": 65.2,
  "DIS": 4.09,
  "RAD": 1.0,
  "TAX": 296.0,
  "PTRATIO": 15.3,
  "B": 396.9,
  "LSTAT": 4.98
}
```

**Response**:
```json
{
  "predicted_price": 29.953396377335693
}
```

## Features

- **Automated Table Creation**: The API automatically creates the `predictions_boston` table in the database upon startup.
- **Data Normalization**: Input features are scaled using the same `StandardScaler` used during training.
- **Persistence**: Every prediction is logged in the database with a timestamp.

