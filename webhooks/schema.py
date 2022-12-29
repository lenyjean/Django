from ninja import Schema
from datetime import date
from pydantic import Field
from uuid import UUID, uuid4
from typing import List, Optional



class BookingInputSchema(Schema):
    customer_name: str
    cake_name: str
    category: str
    cake_size: str
    quantity: str
    total_amount: str
    pickup_date: str
    phone: str
   

class BookingOutputSchema(Schema):
    id: Optional[str] = None
    customer_name: Optional[str] = None
    cake_name: Optional[str] = None
    category: Optional[str] = None
    cake_size: Optional[str] = None
    quantity: Optional[str] = None
    total_amount: Optional[str] = None
    pickup_date: Optional[str] = None
    phone: Optional[str] = None