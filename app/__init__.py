from fastapi import FastAPI

from app.routers import router

fast_app = FastAPI()
fast_app.include_router(router)
