from fastapi import FastAPI
from app.api.routes import user
import logging
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()
app.include_router(user.router)