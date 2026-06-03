from fastapi import Depends, HTTPException, APIRouter, Response, Form, Request
from sqlalchemy.orm import Session
from typing import List
from app.database.models.user_model import User
from app.database.db import get_db
from app.database.schemas.db_schemas import UserCreate, UserResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
template = Jinja2Templates(directory="./app/view")

@router.post("/data-processing", response_class=HTMLResponse)
def create_user_and_redirect(
    request: Request,
    firstname: str = Form(...),
    lastname: str = Form(...),
    username: str = Form(...),
    country: str = Form(...),
    password_user: str = Form(...),
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(User.username == username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists!")

    new_user = User(
        name=firstname,
        lastname=lastname,
        username=username,
        country=country,
        password=password_user 
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user) 

    user_list = [new_user.id, new_user.name, new_user.lastname, new_user.username, new_user.country, new_user.password]

    return template.TemplateResponse(
        request=request, 
        name="user.html",  
        context={"data_user": user_list}
    )

@router.get("/users/", response_model=List[UserResponse])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users

@router.get("/users/{user_id}", response_model=UserResponse)
def get_one_user(user_id: int, db: Session = Depends(get_db)):
    user_db = db.query(User).filter(User.id == user_id).first()
    if user_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_db

@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, update_data: UserCreate, db: Session = Depends(get_db)):
    user_db = db.query(User).filter(User.id == user_id).first()
    
    if user_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    if update_data.username != user_db.username:
        username_used = db.query(User).filter(
            User.username == update_data.username
        ).first()
        if username_used:
            raise HTTPException(status_code=400, detail="That username already exists")

    user_db.name = update_data.name
    user_db.lastname = update_data.lastname
    user_db.username = update_data.username
    user_db.country = update_data.country
    user_db.password = update_data.password  

    db.commit()
    db.refresh(user_db)
    return user_db

@router.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_db = db.query(User).filter(User.id == user_id).first()
    
    if user_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user_db)
    db.commit()
    
    return Response(status_code=204)