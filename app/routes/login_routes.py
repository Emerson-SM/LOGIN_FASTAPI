from fastapi import FastAPI, APIRouter, Request, Form, Depends, HTTPException 
from app.database.db import get_db 
from sqlalchemy.orm import Session 
from app.database.models.user_model import User 
from fastapi.templating import Jinja2Templates 
from fastapi.responses import HTMLResponse 
from fastapi.responses import RedirectResponse

router = APIRouter() 
template = Jinja2Templates(directory="./app/view")

@router.post("/user", response_class=HTMLResponse)
def login(
    request: Request,
    username: str = Form(...),
    password_user: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.username == username
    ).first()

    if not user:
        raise HTTPException(status_code=401)

    if user.password != password_user:
        raise HTTPException(status_code=401)

    user_list = [
        user.id,
        user.name,
        user.lastname,
        user.username,
        user.country,
        user.password
    ]

    return template.TemplateResponse(
        request=request,
        name="user.html",
        context={"data_user": user_list}
    )