# customer/service.py
from customer.repository import CustomerRepository
from typing import Dict, Optional, List

class CustomerService:

    @staticmethod
    def create_customer(data: Dict, conn) -> int:
        """
        data example:
        {
            "name": "Mukul",
            "phone": "+919999999999",
            "email": "mukul@example.com",
            "city": "Bangalore"
        }
        """
        return CustomerRepository.create_customer(data, conn)

    @staticmethod
    def get_customer(customer_id: int, conn) -> Optional[Dict]:
        return CustomerRepository.get_customer(customer_id, conn)

    @staticmethod
    def list_customers(limit: int = 50, offset: int = 0, conn=None) -> List[Dict]:
        return CustomerRepository.get_all_customers(limit, offset, conn)
