from pydantic import BaseModel, EmailStr

class Customer(BaseModel):
    name: str
    email: EmailStr
    cpf: str
    cnpj: str
    soluti_request: str
    cellphone: str
    order_number: str
    partner: str