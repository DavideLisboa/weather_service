from sqlalchemy.orm import sessionmaker
from app.models import WeatherData, engine

Session = sessionmaker(bind=engine)
session = Session()

session.query(WeatherData).filter_by(user_defined_id='test123').delete()
session.commit()
session.close()
