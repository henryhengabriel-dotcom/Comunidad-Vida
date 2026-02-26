from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import app


db_uri= create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

session=sessionmaker(bind=db_uri)

def get_db():
    db=session()
    try:
        yield db
    finally:       
        db.close()
