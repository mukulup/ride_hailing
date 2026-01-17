from pydantic import BaseModel
from typing import Optional

class RideCreate(BaseModel):
    customer_id: int
    pickup_lat: float
    pickup_lng: float
    drop_lat: Optional[float] = None
    drop_lng: Optional[float] = None


class RideResponse(BaseModel):
    id: int
    customer_id: int
    driver_id: Optional[int]
    pickup_lat: float
    pickup_lng: float
    status: str
