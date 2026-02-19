# Comunidad Vida

Aplicación web con Flask + MySQL para registrar contactos de la comunidad, ahora con integración MCP para ejecutar un CRUD desde Claude.

## 👤 Autor

**Henry Perdomo**

## 📋 Descripción

El proyecto tiene dos partes principales:

1. **Aplicación web Flask** para registrar y consultar contactos.
2. **Servidor MCP** para exponer herramientas CRUD de la tabla `usuarios` y usarlas desde Claude.

## 🛠️ Tecnologías utilizadas

- **Backend web**: Flask 3.1.2
- **Base de datos**: MySQL + SQLAlchemy 2.0
- **MCP server**: FastMCP 3.0
- **Frontend**: HTML/CSS/JS

## 📁 Estructura del proyecto

```
ComunidadVida/
│
├── app.py                  # Configuración Flask y SQLAlchemy
├── mcp_db.py               # Sesión de base de datos para herramientas MCP
├── servidor_mcp.py         # Servidor MCP con CRUD de usuarios
├── requirements.txt
├── README.md
│
├── models/
│   └── usuarios.py         # Modelo Usuarios (tabla usuarios)
│
├── routes/
│   ├── __init__.py
│   └── contacto.py         # Rutas web: /, /about, /contacto, /nuevo
│
├── templates/
│   ├── home.html
│   ├── acerca.html
│   └── contactanos.html
│
├── static/
│   ├── css/style.css
│   ├── js/main.js
│   └── images/
│
└── utils/
    └── db.py
```

## 🚀 Instalación

### Requisitos

- Python 3.8+
- MySQL Server
- pip

### Pasos

1. **Entrar al proyecto**

```bash
cd ComunidadVida
```

2. **Crear entorno virtual**

```bash
python -m venv venv
```

3. **Activar entorno virtual**

- Windows:

```bash
venv\Scripts\activate
```

- Linux/Mac:

```bash
source venv/bin/activate
```

4. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

5. **Configurar `.env`**

```env
DB_USER=tu_usuario_mysql
DB_PASSWORD=tu_password_mysql
DB_HOST=localhost
DB_PORT=3306
DB_NAME=comunidad_vida
SECRET_KEY=tu_clave_secreta
FLASK_ENV=development
```

6. **Crear base de datos**

```sql
CREATE DATABASE comunidad_vida;
```

## ▶️ Ejecutar la aplicación web

```bash
python app.py
```

Disponible en: `http://127.0.0.1:5000/`

## 🤖 Integración MCP (Claude)

### ¿Qué hace `mcp_db.py`?

- Reutiliza la configuración de `app.py` para conectarse a la misma base de datos.
- Crea `SessionLocal` de SQLAlchemy.
- Expone `get_db_session()` como generador para abrir/cerrar sesiones.

### ¿Qué hace `servidor_mcp.py`?

Define un servidor `FastMCP("iglesiasDB")` con herramientas CRUD:

- `mostrar_tabla()` → Lista todos los usuarios.
- `crear_usuario(nombre, email, numero)` → Inserta un usuario.
- `actualizar_usuario(id, nombre, email, numero)` → Actualiza un usuario.
- `eliminar_usuario(id)` → Elimina un usuario.

### Ejecutar servidor MCP local

Con el entorno virtual activo:

```bash
python servidor_mcp.py
```

## ⚙️ Configurar Claude Desktop

Ejemplo de configuración en `claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "iglesiasDB": {
      "command": "C:\\Users\\ailin\\OneDrive\\Escritorio\\ComunidadVida\\venv\\Scripts\\python.exe",
      "args": [
        "C:\\Users\\ailin\\OneDrive\\Escritorio\\ComunidadVida\\servidor_mcp.py"
      ]
    }
  }
}
```

Luego reinicia Claude Desktop y podrás invocar las herramientas del CRUD desde el chat.

## 📊 Base de datos

Tabla principal: `usuarios`

Campos definidos por el modelo Flask (`models/usuarios.py`):

- `id` (Integer, PK)
- `nombre` (String 50)
- `email` (String 100, único)
- `numero_telefono` (String 15)

## 🌐 Rutas web

- `GET /` → Inicio
- `GET /about` → Página acerca
- `GET /contacto` → Formulario + listado
- `POST /nuevo` → Crear contacto desde formulario

## ⚠️ Nota importante

El CRUD MCP usa SQL manual con columna `numero` en `servidor_mcp.py`, mientras que el modelo ORM define `numero_telefono`. Verifica que tu tabla MySQL tenga el nombre de columna esperado por tus consultas MCP para evitar errores.

## 📄 Licencia

Proyecto de uso privado para Comunidad Vida.
