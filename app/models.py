from sqlalchemy import Column, Integer, Float, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Prediction(Base):
    __tablename__ = "predictions_boston"

    id = Column(Integer, primary_key=True, index=True)
    crim = Column(Float)
    zn = Column(Float)
    indus = Column(Float)
    chas = Column(Float)
    nox = Column(Float)
    rm = Column(Float)
    age = Column(Float)
    dis = Column(Float)
    rad = Column(Float)
    tax = Column(Float)
    ptratio = Column(Float)
    b = Column(Float)
    lstat = Column(Float)
    predicted_price = Column(Float)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
