from pydantic import BaseModel
from typing import Optional

class Customer(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    cpf: Optional[str] = None
    cnpj: Optional[str] = None
    soluti_request: Optional[str] = None
    cellphone: Optional[str] = None
    order_number: Optional[str] = None
    partner: Optional[str] = None