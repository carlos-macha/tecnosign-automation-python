from fastapi import APIRouter, HTTPException
from loguru import logger

router = APIRouter()

@router.get("/admin-auth-token")
async def admin_auth_token():
    return {"token_type": "Bearer"}