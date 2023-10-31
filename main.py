from fastapi import FastAPI
from dotenv import load_dotenv
from src.modules.api.currency.controller import router
load_dotenv()

app = FastAPI()

app.include_router(router, prefix="/api")
