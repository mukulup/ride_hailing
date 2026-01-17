from config.database import DB
from typing import Dict, Optional

class RideRepository:
    TABLE = "public.rides"

    @staticmethod
    def create_ride(data: Dict, conn) -> int:
        return DB.create(table=RideRepository.TABLE, data=data, conn=conn)

    @staticmethod
    def get_ride(ride_id: int, conn) -> Optional[Dict]:
        return DB.get_one(table=RideRepository.TABLE, id_value=ride_id, conn=conn)

    @staticmethod
    def assign_driver(ride_id: int, driver_id: int, conn) -> bool:
        return DB.update(
            conn=conn,
            table=RideRepository.TABLE,
            id_column="id",
            id_value=ride_id,
            data={"driver_id": driver_id, "status": "ASSIGNED"},
        )

    @staticmethod
    def accept_ride(ride_id: int, driver_id: int, conn) -> bool:
        return DB.update(
            conn=conn,
            table=RideRepository.TABLE,
            id_column="id",
            id_value=ride_id,
            data={"accepted": True}
        )

    @staticmethod
    def end_trip(ride_id: int, conn) -> bool:
        return DB.update(
            conn=conn,
            table=RideRepository.TABLE,
            id_column="id",
            id_value=ride_id,
            data={"status": "COMPLETED"}
        )
