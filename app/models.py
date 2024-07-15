from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime

# Define the SQLite database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./weather_data.db"

# Create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a sessionmaker configured to use the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define your WeatherData model


class WeatherData(Base):
    __tablename__ = "weather_data"

    id = Column(Integer, primary_key=True, index=True)
    user_defined_id = Column(String)
    city_id = Column(Integer)
    temperature = Column(Float)
    humidity = Column(Integer)
    datetime = Column(DateTime, default=datetime.now)


# Create all tables defined in the Base class (including WeatherData)
Base.metadata.create_all(bind=engine)
