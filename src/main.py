import uvicorn

from src.core import settings
from src.create_app import create_app

app = create_app()


if __name__ == "__main__":
    uvicorn.run(
        app="src.main:app",
        host=settings.server.host,
        port=settings.server.port,
        reload=True,
    )
