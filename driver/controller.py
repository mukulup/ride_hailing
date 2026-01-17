# driver/controller.py
from fastapi import APIRouter, Depends, HTTPException, status
from config.database import DB
from driver.schema import DriverCreate, DriverLocationUpdate, DriverResponse, DriverUpdate
from driver.service import DriverService
from ride.service import RideService

router = APIRouter(prefix="/drivers", tags=["drivers"])

@router.post("/", response_model=DriverResponse, status_code=status.HTTP_201_CREATED)
def create_driver(
    driver: DriverCreate,
    conn = Depends(DB.get_connection)
):
    driver_id = DriverService.create_driver(driver.dict(exclude_unset=True), conn)
    created = DriverService.get_driver(driver_id, conn)
    return DriverResponse(**created)


@router.get("/{driver_id}", response_model=DriverResponse)
def get_driver(driver_id: int, conn = Depends(DB.get_connection)):
    driver = DriverService.get_driver(driver_id, conn)
    if not driver:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Driver not found")
    return DriverResponse(**driver)

@router.post("/{driver_id}/location")
def update_driver_location(
    driver_id: int,
    payload: DriverLocationUpdate,
    conn=Depends(DB.get_connection)
):
    updated = DriverService.update_location(
        driver_id, payload.latitude, payload.longitude, conn
    )
    if not updated:
        raise HTTPException(404, "Driver not found")
    return {"status": "location updated"}

@router.post("/{driver_id}/accept")
def accept_ride(
    driver_id: int,
    ride_id: int,
    conn=Depends(DB.get_connection)
):
    accepted = RideService.accept_ride(ride_id, driver_id, conn)
    if not accepted:
        raise HTTPException(400, "Ride cannot be accepted")
    return {"status": "ride accepted"}
