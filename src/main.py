import uvicorn
from fastapi import FastAPI

from src.core import settings

app = FastAPI()


if __name__ == "__main__":
    uvicorn.run(
        app="src.main:app",
        host=settings.server.host,
        port=settings.server.port,
        reload=True,
    )
