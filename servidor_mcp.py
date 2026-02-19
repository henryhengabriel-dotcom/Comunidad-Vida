from fastmcp import FastMCP

from mcp_db import get_db_session
from sqlalchemy import text




mcp=FastMCP("iglesiasDB")

@mcp.tool()
def mostrar_tabla():
        """Muestra la tabla de usuarios"""
     
        db=next(get_db_session())
        rows =db.execute(text("SELECT * FROM USUARIOS")).fetchall()
        results=[dict(r) for r in rows]
        return results

       

@mcp.tool()
def crear_usuario(nombre:str, email:str, numero:str):
    """Crea un nuevo usuario en la tabla de usuarios"""
    db=next(get_db_session())
    sql= ("INSERT INTO USUARIOS (nombre, email, numero) VALUES (:nombre, :email, :numero)")
    results=db.execute(text(sql), {"nombre": nombre, "email": email, "numero": numero})
    db.commit()
    nuevo_id= getattr(results, "lastrowid", None)

   

    return f"Usuario creado con ID: {nuevo_id}"

@mcp.tool()
def actualizar_usuario(id:int, nombre:str, email:str, numero:str):
    """Actualiza un usuario existente en la tabla de usuarios"""
    db=next(get_db_session())
    sql= ("UPDATE USUARIOS SET nombre=:nombre, email=:email, numero=:numero WHERE id=:id")
    db.execute(text(sql), {"id": id, "nombre": nombre, "email": email, "numero": numero})
    db.commit()
    return f"Usuario con ID {id} actualizado"

@mcp.tool()
def eliminar_usuario(id:int):
    """Elimina un usuario de la tabla de usuarios"""
    db=next(get_db_session())
    sql= ("DELETE FROM USUARIOS WHERE id=:id")
    db.execute(text(sql), {"id": id})
    db.commit()
    return f"Usuario con ID {id} eliminado"

if __name__ == "__main__":
    mcp.run()