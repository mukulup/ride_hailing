from ride.repository import RideRepository
from driver.repository import DriverRepository
from typing import Optional, Dict


class RideService:

    @staticmethod
    def create_ride(data: dict, conn) -> int:
        data["status"] = "REQUESTED"
        return RideRepository.create_ride(data, conn)

    @staticmethod
    def assign_driver(ride_id: int, conn) -> Optional[Dict]:

        driver = DriverRepository.find_available_driver(conn)

        if not driver:
            # No driver available, ride remains REQUESTED
            return None

        # Assign driver to ride
        RideRepository.assign_driver(
            ride_id=ride_id,
            driver_id=driver["id"],
            conn=conn
        )

        # Mark driver unavailable
        DriverRepository.mark_unavailable(driver["id"], conn)

        return driver

    @staticmethod
    def get_ride(ride_id: int, conn) -> Optional[Dict]:
        return RideRepository.get_ride(ride_id, conn)
    
    @staticmethod
    def accept_ride(ride_id: int, driver_id: int, conn) -> bool:
        return RideRepository.accept_ride(ride_id, driver_id, conn)

    @staticmethod
    def end_trip(ride_id: int, conn) -> bool:
        ride = RideRepository.get_ride(ride_id, conn)
        if not ride or not ride.get("driver_id"):
            return False

        RideRepository.end_trip(ride_id, conn)
        DriverRepository.mark_available(ride["driver_id"], conn)
        return True
