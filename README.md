# Comunidad Vida

Una aplicación web para la gestión de contactos de la comunidad religiosa "Comunidad Vida". Desarrollada con Flask y MySQL.

## 👤 Autor

**Henry Perdomo**

## 📋 Descripción

Comunidad Vida es una aplicación web diseñada para gestionar la información de contacto de los miembros y personas interesadas en la comunidad. La aplicación permite:

- Visualizar información sobre la comunidad
- Registrar nuevos contactos con nombre, email y teléfono
- Gestionar la base de datos de usuarios
- Interfaz responsive y moderna con Bootstrap

## 🛠️ Tecnologías Utilizadas

- **Backend**: Flask 3.1.2
- **Base de Datos**: MySQL con SQLAlchemy
- **Frontend**: HTML, CSS, Bootstrap, Bootstrap Icons
- **Librerías principales**:
  - Flask-SQLAlchemy 3.1.1
  - Flask-Login 0.6.3
  - PyMySQL
  - python-dotenv

## 📁 Estructura del Proyecto

```
ComunidadVida/
│
├── app.py                 # Archivo principal de la aplicación
├── requirements.txt       # Dependencias del proyecto
├── .env                   # Variables de entorno (no incluido en el repo)
│
├── models/
│   └── usuarios.py        # Modelo de datos para usuarios
│
├── routes/
│   ├── __init__.py
│   └── contacto.py        # Rutas para páginas y formulario de contacto
│
├── templates/
│   ├── main.html          # Template base
│   ├── home.html          # Página de inicio
│   ├── about.html         # Página "Sobre nosotros"
│   └── contacto.html      # Página de contacto con formulario
│
├── static/
│   └── main.css           # Estilos personalizados
│
└── utils/
    └── db.py              # Configuración de la base de datos
```

## 🚀 Instalación

### Requisitos Previos

- Python 3.8 o superior
- MySQL Server
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el repositorio**

```bash
cd ComunidadVida
```

2. **Crear un entorno virtual**

```bash
python -m venv venv
```

3. **Activar el entorno virtual**

- Windows:
```bash
venv\Scripts\activate
```

- Linux/Mac:
```bash
source venv/bin/activate
```

4. **Instalar las dependencias**

```bash
pip install -r requirements.txt
```

5. **Configurar las variables de entorno**

Crear un archivo `.env` en la raíz del proyecto con la siguiente información:

```env
DB_USER=tu_usuario_mysql
DB_PASSWORD=tu_contraseña_mysql
DB_HOST=localhost
DB_PORT=3306
DB_NAME=comunidad_vida
SECRET_KEY=tu_clave_secreta_aqui
FLASK_ENV=development
```

6. **Crear la base de datos en MySQL**

```sql
CREATE DATABASE comunidad_vida;
```

7. **Ejecutar la aplicación**

```bash
python app.py
```

La aplicación estará disponible en `http://127.0.0.1:5000/`

## 📊 Base de Datos

### Tabla: usuarios

| Campo           | Tipo         | Descripción                    |
|----------------|--------------|--------------------------------|
| id             | INTEGER      | Clave primaria (auto-increment)|
| nombre         | VARCHAR(50)  | Nombre del usuario             |
| email          | VARCHAR(100) | Email (único)                  |
| numero_telefono| VARCHAR(15)  | Número de teléfono             |

## 🌐 Rutas de la Aplicación

| Ruta       | Método | Descripción                              |
|------------|--------|------------------------------------------|
| `/`        | GET    | Página de inicio                         |
| `/about`   | GET    | Información sobre la comunidad           |
| `/contacto`| GET    | Formulario de contacto y lista de usuarios|
| `/nuevo`   | POST   | Procesar nuevo registro de contacto      |

## 🎨 Características

- **Diseño Responsive**: Se adapta a dispositivos móviles, tablets y escritorio
- **Formulario de Contacto**: Validación de campos y mensajes flash
- **Gestión de Usuarios**: Almacenamiento seguro en base de datos MySQL
- **Interfaz Moderna**: Bootstrap 5 con iconos y diseño limpio
- **Arquitectura MVC**: Separación clara de modelos, vistas y controladores

## 🔒 Seguridad

- Variables de entorno para credenciales sensibles
- Secret key para sesiones Flask
- Validación de formularios
- SQLAlchemy ORM para prevenir inyección SQL

## 📝 Uso

1. **Página de Inicio**: Presenta información general sobre Comunidad Vida
2. **Sobre Nosotros**: Describe la misión y valores de la comunidad
3. **Contacto**: 
   - Formulario para nuevos contactos
   - Lista de personas registradas
   - Mensajes de confirmación al registrar

## 🤝 Contribuir

Si deseas contribuir al proyecto:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

## 📧 Contacto

Para más información sobre el proyecto, contacta a **Henry Perdomo**.

## 📄 Licencia

Este proyecto es de uso privado para Comunidad Vida.

---

**Comunidad Vida** - Un lugar para crecer en fe, esperanza y amor. 🙏
