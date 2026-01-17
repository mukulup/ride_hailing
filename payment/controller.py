from fastapi import APIRouter, Depends, HTTPException
from config.database import DB


router = APIRouter(prefix="/drivers", tags=["drivers"])

@router.post("/payments")
def make_payment(ride_id: int, amount: float, conn=Depends(DB.get_connection)):
    DB.create(
        conn,
        "payments",
        {"ride_id": ride_id, "amount": amount, "status": "SUCCESS"}
    )
    return {"status": "payment successful"}
