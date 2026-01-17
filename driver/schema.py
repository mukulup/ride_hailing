# driver/schema.py
from pydantic import BaseModel, Field
from typing import Optional

class DriverCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    phone: str = Field(..., pattern=r"^\+?[1-9]\d{1,14}$")
    vehicle_number: str = Field(..., pattern=r"^[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}$")  # example Indian format
    vehicle_type: str = Field(default="sedan", pattern="^(sedan|hatchback|suv|bike)$")
    current_city: Optional[str] = None


class DriverUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    vehicle_number: Optional[str] = None
    vehicle_type: Optional[str] = None
    current_city: Optional[str] = None


class DriverResponse(BaseModel):
    id: int
    name: str
    phone: str
    vehicle_number: str
    vehicle_type: str
    current_city: Optional[str]

    class Config:
        from_attributes = True


class DriverLocationUpdate(BaseModel):
    latitude: float
    longitude: float
