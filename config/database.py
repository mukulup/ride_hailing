# config/database.py
import psycopg2
from psycopg2 import pool
from psycopg2.extras import RealDictCursor
from typing import Any, List, Dict, Optional, Generator
from config.settings import get_db_dsn

class DB:
    _pool: pool.SimpleConnectionPool | None = None

    @classmethod
    def _initialize_pool(cls):
        if cls._pool is None:
            cls._pool = pool.SimpleConnectionPool(
                minconn=1,
                maxconn=20,
                dsn=get_db_dsn(),
                cursor_factory=RealDictCursor
            )

    @classmethod
    def get_connection(cls):
        cls._initialize_pool()
        conn = cls._pool.getconn()
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            cls._pool.putconn(conn)

    @staticmethod
    def get_one(conn, table: str, id_column: str = "id", id_value: Any = None) -> Optional[Dict]:
        query = f"SELECT * FROM {table} WHERE {id_column} = %s LIMIT 1"
        with conn.cursor() as cur:
            cur.execute(query, (id_value,))
            return cur.fetchone()

    @staticmethod
    def get_all(conn, table: str, limit: int = 100, offset: int = 0) -> List[Dict]:
        query = f"SELECT * FROM {table} LIMIT %s OFFSET %s"
        with conn.cursor() as cur:
            cur.execute(query, (limit, offset))
            return cur.fetchall()

    @staticmethod
    def create(conn, table: str, data: Dict, returning: str = "id") -> Any:
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        query = f"""
            INSERT INTO {table} ({columns})
            VALUES ({placeholders})
            RETURNING {returning}
        """
        with conn.cursor() as cur:
            cur.execute(query, tuple(data.values()))
            result = cur.fetchone()
            return result[returning] if result else None

    @staticmethod
    def update(conn, table: str, id_column: str, id_value: Any, data: Dict) -> bool:
        if not data:
            return False
        sets = ', '.join(f"{k} = %s" for k in data.keys())
        query = f"UPDATE {table} SET {sets} WHERE {id_column} = %s"
        values = list(data.values()) + [id_value]

        with conn.cursor() as cur:
            cur.execute(query, values)
            return cur.rowcount > 0

    @staticmethod
    def delete(conn, table: str, id_column: str, id_value: Any) -> bool:
        query = f"DELETE FROM {table} WHERE {id_column} = %s"
        with conn.cursor() as cur:
            cur.execute(query, (id_value,))
            return cur.rowcount > 0