from fastapi import FastAPI
from app.routes.user_routes import router as router1
from app.routes.db_routes import router as router2
from app.routes.login_routes import router as router3
from dotenv import load_dotenv
import os
from app.database.models import user_model
from app.database.db import engine

load_dotenv()

def create_app():
    app = FastAPI()

    app.include_router(router2)
    app.include_router(router1)
    app.include_router(router3)
    
    user_model.Base.metadata.create_all(bind=engine)

    return app
    