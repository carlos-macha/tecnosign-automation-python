from fastapi import APIRouter
from app.services.customer_service.customer_service import CustomerService

router = APIRouter()

@router.get("/customers/{customer_identification_code}")
async def get_customers(customer_identification_code: str):
    data = await CustomerService.get_customer(customer_identification_code)
    return {
        "data": {
            "name": data.name,
            "email": data.email,
            "cpf": data.cpf,
            "cnpj": data.cnpj,
            "soluti_request": data.soluti_request,
            "cellphone": data.cellphone,
            "order_number": data.order_number,
            "partner": data.partner,
        }
    }
