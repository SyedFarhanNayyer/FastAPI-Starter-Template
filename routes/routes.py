from fastapi import APIRouter, Request, Form, File, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from bson import ObjectId
from fastapi.templating import Jinja2Templates
from schema import WelcomeMessage

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_model= WelcomeMessage, include_in_schema=False )
def welcome():
    return {
        "message" : "Welcome to Fast Api"
    }