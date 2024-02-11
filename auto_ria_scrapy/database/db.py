from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from src.conf.config import settings

SQLALCHEMY_DATABASE_URL="postgresql+psycopg2://postgres:567234@localhost:5432/scrapy_db"

# SQLALCHEMY_DATABASE_URL = settings.sqlalchemy_database_url
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()