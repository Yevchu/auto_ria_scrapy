from sqlalchemy import Column, String, Integer, func
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CarsInfo(Base):
    __tablename__ = 'cars_info'
    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    title = Column(String(180), nullable=False)
    price_usd = Column(String, nullable=False)
    username = Column(String, nullable=False)
    odometer = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    image_url = Column(String, nullable=False)
    images_count = Column(String, nullable=False)
    car_number = Column(String, nullable=False)
    car_vin = Column(String, nullable=False)
    created_at = Column('created_at', DateTime, default=func.now())
    updated_at = Column('updated_at', DateTime)

    