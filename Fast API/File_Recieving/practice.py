from fastapi import FastAPI, UploadFile
import os
import shutil
from fastapi.staticfiles import StaticFiles

app = FastAPI()
Upload_name= "./uploads"

os.makedirs(Upload_name,exit_ok=True)
app.mount("/Static", StaticFiles(directory=Upload_name), name="static")

@app.post("/upload")
def file_upload (file:UploadFile):
    path= os.path.join (Upload_name,file.filename)

    with open(path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    url=f"/Static/{file.filename}"
    return {"filename":file.filename, "fileurl":url}
#teen cheezie hn hamari file,    path aur user ki file