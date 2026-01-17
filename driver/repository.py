# driver/repository.py
from config.database import DB
from typing import Optional, Dict

class DriverRepository:
    TABLE = "public.drivers"

    @staticmethod
    def create_driver(data: dict, conn):
        return DB.create(table=DriverRepository.TABLE, data=data, conn=conn)

    @staticmethod
    def get_driver(driver_id: int, conn):
        return DB.get_one(table=DriverRepository.TABLE, id_value=driver_id, conn=conn)

    @staticmethod
    def find_available_driver(conn) -> Optional[Dict]:
        query = """
            SELECT *
            FROM drivers
            WHERE is_available = TRUE
            ORDER BY id
            LIMIT 1
            FOR UPDATE
        """
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchone()

    @staticmethod
    def mark_unavailable(driver_id: int, conn) -> bool:
        return DB.update(
            conn=conn,
            table=DriverRepository.TABLE,
            id_column="id",
            id_value=driver_id,
            data={"is_available": False},
        )

    @staticmethod
    def update_location(driver_id: int, lat: float, lng: float, conn) -> bool:
        return DB.update(
            conn=conn,
            table=DriverRepository.TABLE,
            id_column="id",
            id_value=driver_id,
            data={"latitude": lat, "longitude": lng},
        )

    @staticmethod
    def mark_available(driver_id: int, conn) -> bool:
        return DB.update(
            conn=conn,
            table=DriverRepository.TABLE,
            id_column="id",
            id_value=driver_id,
            data={"is_available": True}
        )
