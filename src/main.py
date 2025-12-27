import uvicorn
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.core import settings
from src.create_app import create_app

templates = Jinja2Templates(directory="src/templates")

app = create_app()

app.mount(
    "/static",
    StaticFiles(directory="src/static"),
    name="static",
)


@app.get("/")
async def home_page(request: Request):
    return templates.TemplateResponse(request, name="index.html")


if __name__ == "__main__":
    uvicorn.run(
        app="src.main:app",
        host=settings.server.host,
        port=settings.server.port,
        reload=True,
    )
