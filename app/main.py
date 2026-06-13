import os
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="DevOps Crew Training Site",
    description="A small FastAPI site for CI, testing, Docker, and deployment practice.",
    version=os.getenv("APP_VERSION", "0.1.0"),
)

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    features = [
        "FastAPI application",
        "HTML template and static CSS",
        "Health-check endpoint",
        "JSON API endpoint",
        "Pytest test suite",
        "Docker-ready runtime",
    ]
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "title": "DevOps Crew Training",
            "environment": os.getenv("APP_ENV", "local"),
            "features": features,
        },
    )


@app.get("/health")
async def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "devops-crew-training-site",
        "environment": os.getenv("APP_ENV", "local"),
    }


@app.get("/api/info")
async def api_info() -> dict[str, object]:
    return {
        "name": "DevOps Crew Training Site",
        "version": app.version,
        "tasks": [
            "write GitHub Actions CI",
            "run tests on pull requests",
            "build and push Docker image",
            "deploy to a server",
            "promote changes to dev branch",
        ],
    }
