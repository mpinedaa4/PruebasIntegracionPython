
import sqlite3
from db.repo import SQLiteUserRepository
from layers.service import UserService

def test_user_service_with_sqlite_in_memory():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.executescript(
        """
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            first TEXT NOT NULL,
            last  TEXT
        );
        INSERT INTO users (id, first, last) VALUES (1, 'Ada', 'Lovelace');
        INSERT INTO users (id, first, last) VALUES (2, 'Alan', 'Turing');
        INSERT INTO users (id, last) VALUES (3, 'Pineda');
        """
    )
    conn.commit()

    repo = SQLiteUserRepository(conn)
    service = UserService(repo)

    assert service.get_full_name(1) == "Ada Lovelace"
    assert service.get_full_name(2) == "Alan Turing"
    assert service.get_full_name(999) is None

    """
    Con el constraint, si se inserta un usuario sin first name la prueba saca error
    porque se está violando el constraint
    """
