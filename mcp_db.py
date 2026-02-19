from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import app
from utils import db

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Sessionlocal = sessionmaker(bind=engine)

def get_db_session():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()