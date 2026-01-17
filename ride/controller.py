from fastapi import APIRouter, Depends, HTTPException
from config.database import DB
from ride.schema import RideCreate, RideResponse
from ride.service import RideService

router = APIRouter(prefix="/rides", tags=["rides"])

@router.post("/", response_model=RideResponse)
def create_ride(payload: RideCreate, conn=Depends(DB.get_connection)):
    ride_id = RideService.create_ride(payload.dict(), conn)
    ride = RideService.assign_driver(ride_id, conn)
    return RideResponse(**RideService.get_ride(ride_id, conn))

@router.get("/{ride_id}", response_model=RideResponse)
def get_ride(ride_id: int, conn=Depends(DB.get_connection)):
    ride = RideService.get_ride(ride_id, conn)
    if not ride:
        raise HTTPException(status_code=404, detail="Ride not found")
    return RideResponse(**ride)

@router.post("/trips/{ride_id}/end")
def end_trip(ride_id: int, conn=Depends(DB.get_connection)):
    ended = RideService.end_trip(ride_id, conn)
    if not ended:
        raise HTTPException(400, "Trip cannot be ended")
    return {"status": "trip completed"}
