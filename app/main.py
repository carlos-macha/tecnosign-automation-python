from fastapi import FastAPI
from app.api.controllers.customer.customer_controller import router as customer_router

app = FastAPI()

app.include_router(customer_router, prefix="/tecnosign")