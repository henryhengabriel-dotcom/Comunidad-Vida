from flask import render_template, redirect, request, url_for, flash, blueprints
from utils.db import db 
from models.usuarios import Usuarios


contacto_bp = blueprints.Blueprint('iglesia', __name__)


@contacto_bp.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@contacto_bp.route('/about', methods=['GET'])
def about():
    return render_template('acerca.html')



# Ruta para mostrar el formulario de contacto
@contacto_bp.route('/contacto', methods=['GET'])
def contacto():
    personas = Usuarios.query.all()
    return render_template('contactanos.html', personas=personas)


# Ruta para procesar el formulario de contacto
@contacto_bp.route('/nuevo', methods=['POST'])
def nuevo():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    telefono = request.form.get('telefono')

    if nombre and email and telefono:
        nuevo_usuario = Usuarios(nombre, email, telefono)
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('¡Gracias por contactarnos! Nos pondremos en contacto contigo pronto.', 'success')

        return redirect(url_for('iglesia.contacto'))
    else:
        return render_template('contactanos.html', error='Por favor completa todos los campos.', personas=Usuarios.query.all())

