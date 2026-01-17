# customer/repository.py
from config.database import DB
from typing import List, Dict, Optional

class CustomerRepository:
    TABLE = "public.customers"

    @staticmethod
    def create_customer(data: dict, conn) -> int:
        return DB.create(table=CustomerRepository.TABLE, data=data, conn=conn)

    @staticmethod
    def get_customer(customer_id: int, conn) -> Optional[Dict]:
        return DB.get_one(table=CustomerRepository.TABLE, id_value=customer_id, conn=conn)

    @staticmethod
    def get_all_customers(limit: int = 50, offset: int = 0, conn=None) -> List[Dict]:
        return DB.get_all(table=CustomerRepository.TABLE, limit=limit, offset=offset, conn=conn)

    @staticmethod
    def update_customer(customer_id: int, data: dict, conn) -> bool:
        return DB.update(table=CustomerRepository.TABLE, id_value=customer_id, data=data, conn=conn)

    @staticmethod
    def delete_customer(customer_id: int, conn) -> bool:
        return DB.delete(table=CustomerRepository.TABLE, id_value=customer_id, conn=conn)