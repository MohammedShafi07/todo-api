from fastapi import APIRouter

router = APIRouter(prefix="/ping", tags=["Ping"])


@router.get("/")
async def ping():
    """
    Ping route for health check
    """
    return {
        "message": "pong",
        "attempt": "3"
    }