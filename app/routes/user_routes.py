from fastapi import FastAPI, Request, Response, APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()

template = Jinja2Templates(directory="./app/view")

@router.get("/", response_class=HTMLResponse)
def root(req:Request):
    return template.TemplateResponse(request=req, name="index.html")

@router.get("/signup", response_class=HTMLResponse)
def signup(req:Request):
    return template.TemplateResponse(request=req, name="signup.html")

@router.get("/user", response_class=HTMLResponse)
def signup(req:Request):
    return template.TemplateResponse(request=req, name="user.html")
    