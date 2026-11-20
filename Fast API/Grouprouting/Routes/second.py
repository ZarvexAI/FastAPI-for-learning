#custom router for other files to use 
# APIRouter
from fastapi import APIRouter
postRouter= APIRouter()

@postRouter.get("/CreateStudent")
def hello():
    return "hii"


@postRouter.get("/second")
def idk():
    return "second"
