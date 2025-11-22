from pydantic import BaseModel

class Customer(BaseModel):
    name: str
    email: str
    cpf: str
    cnpj: str
    soluti_request: str
    cellphone: str
    order_number: str
    partner: str