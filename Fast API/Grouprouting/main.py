from fastapi import FastAPI
from Routes.second import postRouter
app = FastAPI()
app.include_router(postRouter,prefix="/create",tags=["post"])






# from fastapi import APIRouter
# upload_router = APIRouter()
# app.include_router(upload_router,prefix="/post",tags=["practice"])




# upload_router.get("/upload")
# def upload():
#     return "hiiii"  