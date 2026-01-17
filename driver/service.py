# driver/service.py
from driver.repository import DriverRepository
from typing import Dict, Optional

class DriverService:

    @staticmethod
    def create_driver(data: Dict, conn) -> int:
        return DriverRepository.create_driver(data, conn)

    @staticmethod
    def get_driver(driver_id: int, conn) -> Optional[Dict]:
        return DriverRepository.get_driver(driver_id, conn)
    

    @staticmethod
    def update_location(driver_id: int, lat: float, lng: float, conn) -> bool:
        return DriverRepository.update_location(driver_id, lat, lng, conn)
