# customer/schema.py
from pydantic import BaseModel, Field
from typing import Optional

class CustomerCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    phone: str = Field(..., pattern=r"^\+?[1-9]\d{1,14}$")  # E.164-ish
    email: Optional[str] = Field(None, pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    city: Optional[str] = None


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    city: Optional[str] = None


class CustomerResponse(BaseModel):
    id: int
    name: str
    phone: str
    email: Optional[str]
    city: Optional[str]

    class Config:
        from_attributes = True  # orm_mode equivalent