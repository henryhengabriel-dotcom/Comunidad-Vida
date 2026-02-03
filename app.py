from flask import Flask
from utils.db import db
from routes.contacto import contacto_bp
from dotenv import load_dotenv
import os



app = Flask(__name__)
load_dotenv()

DB_USER= os.getenv('DB_USER')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DB_HOST=os.getenv('DB_HOST')
DB_PORT=os.getenv('DB_PORT')
DB_NAME=os.getenv('DB_NAME')
SECRET_KEY=os.getenv('SECRET_KEY')
FLASK_ENV=os.getenv('FLASK_ENV')




app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.register_blueprint(contacto_bp) 
db.init_app(app)



with app.app_context():    
    db.create_all()



if __name__ == '__main__':
    app.run(debug=True)
        
