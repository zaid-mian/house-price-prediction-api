from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:1234@localhost:8888/house_price_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)