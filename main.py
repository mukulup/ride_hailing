# main.py
from fastapi import FastAPI

from customer.controller import router as customer_router
from driver.controller import router as driver_router
from ride.controller import router as ride_router
from payment.controller import router as payment_router


app = FastAPI(title="Ride Hailing - Modular Structure")

app.include_router(customer_router)
app.include_router(driver_router)
app.include_router(ride_router)
app.include_router(payment_router)


@app.get("/health")
async def health():
    return {"status": "ok"}