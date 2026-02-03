from utils.db import db

class Usuarios(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    numero_telefono = db.Column(db.String(15), nullable=True)

    def __init__(self, nombre, email, numero_telefono):
        self.nombre = nombre
        self.email = email
        self.numero_telefono = numero_telefono

        