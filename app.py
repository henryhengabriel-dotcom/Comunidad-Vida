from flask import Flask
from utils.db import db
from routes.contacto import contacto_bp
from config.config import Config



app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(contacto_bp) 
db.init_app(app)



with app.app_context():    
    db.create_all()



if __name__ == '__main__':
    app.run(debug=True)
        
