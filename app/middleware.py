from starlette.middleware.base import BaseHTTPMiddleware
from app.database import SessionLocal


class DBSessionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request.state.db = SessionLocal()
        try:
            response = await call_next(request)

        finally:
            request.state.db.close()
        return response
