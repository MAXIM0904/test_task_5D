from fastapi import APIRouter

from app_task.api.v1.endpoints.transmitted_url import trans_url_router

router_v1 = APIRouter()


router_v1.include_router(
    trans_url_router, prefix="/transmitted_url",
    tags=["v1_transmitted_url"]
)