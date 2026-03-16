# Revisado por Mateo Pineda y Santiago Idárraga

# Importaciones
import sqlite3 # Base de datos
from typing import Optional # Tipado de variables
from layers.models import User # Modelo Usuario

class SQLiteUserRepository:
    """
    Clase para gestionar todo lo pertinente al modelo
    usuario con la base de datos.
    """
    # Constructor
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn # Inicializa la conexión a la BD

    # Encontrar un usuario por su número de id
    def find_by_id(self, user_id: int) -> Optional[User]:
        cur = self.conn.cursor() # Define el cursor para conexión con la BD y ejecución de consultas
        cur.execute("SELECT id, first, last FROM users WHERE id = ?", (user_id,)) # Ejecuta query de SQL para buscar usuario por id
        row = cur.fetchone() # Toma la primera fila que arroja el resultado de la consulta SQL
        if row is None:
            return None # En caso de que no haya usuario con ese id
        return User(id=row[0], first=row[1], last=row[2]) # Devuelve objeto de la clase User con los datos extraídos de la BD
