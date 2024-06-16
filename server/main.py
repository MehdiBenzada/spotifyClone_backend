from fastapi import FastAPI
from routes import auth
from models.base import base
from database import engine

app= FastAPI()
app.include_router(auth.router,prefix='/auth')










base.metadata.create_all(engine)