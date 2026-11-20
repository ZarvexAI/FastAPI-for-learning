from fastapi import FastAPI, UploadFile
from fastapi.staticfiles import StaticFiles
import os
import shutil
app=FastAPI()
upload_folder= "./uploads"
os.makedirs(upload_folder,exist_ok=True)
app.mount("/static",StaticFiles(directory=upload_folder), name="static")
@app.post("/upload")
def practice(file:UploadFile):
    path=os.path.join(upload_folder,file.filename)
    with open(path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    url=f"/static/{file.filename}"
    return {"Name": file.filename, "Url": url}
