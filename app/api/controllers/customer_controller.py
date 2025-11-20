from fastapi import APIRouter
from app.services.customer_service.customer_service import CustomerService

router = APIRouter()

@router.get("/customers")
async def get_customers():
    await CustomerService.get_customer()
    return {"message": "Relatório financeiro aberto"}
