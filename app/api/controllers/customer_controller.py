from fastapi import APIRouter, HTTPException
from app.services.customer_service.customer_service import CustomerService
from loguru import logger

router = APIRouter()

@router.get("/customers/{customer_identification_code}")
async def get_customers(customer_identification_code: str):
    try:
        logger.info(f"Received request for customer ID: {customer_identification_code}")
        data = await CustomerService.get_customer(customer_identification_code)

        # Verifica se algum dado crítico está ausente
        if not data.name or not data.cnpj:
            logger.warning(f"Customer data incomplete for ID: {customer_identification_code}")
            raise HTTPException(
                status_code=404,
                detail=f"Customer with ID {customer_identification_code} not found or incomplete"
            )

        logger.success(f"Customer data retrieved successfully for ID: {customer_identification_code}")
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

    except HTTPException:
        # Lança a exceção já formatada acima
        raise
    except Exception:
        logger.exception(f"Unexpected error retrieving customer ID: {customer_identification_code}")
        raise HTTPException(
            status_code=500,
            detail="Internal server error while retrieving customer data"
        )
