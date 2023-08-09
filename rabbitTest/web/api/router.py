from fastapi.routing import APIRouter
from rabbitTest.web.api import echo
from rabbitTest.web.api import dummy
from rabbitTest.web.api import rabbit
from rabbitTest.web.api import monitoring

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(dummy.router, prefix="/dummy", tags=["dummy"])
api_router.include_router(rabbit.router, prefix="/rabbit", tags=["rabbit"])
