# customer/controller.py
from fastapi import APIRouter, Depends, HTTPException, status
from config.database import DB
from customer.schema import CustomerCreate, CustomerResponse, CustomerUpdate
from customer.service import CustomerService

router = APIRouter(prefix="/customers", tags=["customers"])

@router.post(
    "/",
    response_model=CustomerResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create new customer"
)
def create_customer(
    customer: CustomerCreate,
    conn = Depends(DB.get_connection)
):
    customer_id = CustomerService.create_customer(customer.dict(exclude_unset=True), conn)
    created = CustomerService.get_customer(customer_id, conn)
    return CustomerResponse(**created)


@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer(customer_id: int, conn = Depends(DB.get_connection)):
    customer = CustomerService.get_customer(customer_id, conn)
    if not customer:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Customer not found")
    return CustomerResponse(**customer)


@router.patch("/{customer_id}", response_model=CustomerResponse)
def update_customer(
    customer_id: int,
    update_data: CustomerUpdate,
    conn = Depends(DB.get_connection)
):
    if not CustomerService.update_customer(customer_id, update_data.dict(exclude_unset=True), conn):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Customer not found or no changes")
    
    updated = CustomerService.get_customer(customer_id, conn)
    return CustomerResponse(**updated)