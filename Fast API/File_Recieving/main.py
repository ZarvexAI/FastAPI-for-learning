#now we are going to process files in fastapi
#digital ocean and aws s3 for purchasing server space and memory and cpu
#python_multipart library


from fastapi import FastAPI, UploadFile
from fastapi.staticfiles import StaticFiles
import os
import shutil
app=FastAPI()
upload_folder= "./uploads"
os.makedirs(upload_folder,exist_ok=True)
app.mount("/static"(directory=upload_folder),name="static")

@app.post("/upload")
def practice(file:UploadFile):
    path=os.path.join(upload_folder,file.filename)
    with open(path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    url=f"/static/{file.filename}"
    return {"Name": file.filename, "Url": url}



# from fastapi import FastAPI, UploadFile
# from fastapi.staticfiles import StaticFiles  #files that front end can see
# import shutil                                #librabry to create files from frontend
# import os     #custom file 

# app = FastAPI()
# UPLOAD_FOLDER = "./uploads"#dot means current folder
# #folder banye ga OS

# os.makedirs(UPLOAD_FOLDER, exist_ok=True)#folder bany ga, first parameter is route ky folder kahan bnany ga

# app.mount("/static",StaticFiles(directory=UPLOAD_FOLDER),name="static")
# #first route second is wo file jo front end dekh sakta hy third is validation aisy hi hy

# @app.post("/upload")
# def file_upload(file: UploadFile):
#     file_path = os.path.join(UPLOAD_FOLDER,file.filename)

#     with open (file_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     file_url = f"/static/{file.filename}"
#     return {"filename":file.filename, "fileurl": file_url}



# ==============================
# FASTAPI FILE HANDLING
# ==============================

# FastAPI = Python ka framework/library hai API banane ke liye.
# FastAPI() ek class hai jo application banati hai.

# UploadFile = FastAPI ki predefined class/type hai.
# Ye Python ka built-in datatype nahi hai.
# Iska use client/user se uploaded file receive karne ke liye hota hai.

# StaticFiles = FastAPI ki predefined class hai.
# Iska use files ko URL ke through frontend/client ke liye accessible banane ke liye hota hai.

# shutil = Python ki built-in module/library hai.
# Ismein file ko copy karne ke functions available hote hain.

# os = Python ki built-in module/library hai.
# Iska use folders aur file paths ke saath kaam karne ke liye hota hai.


# ==============================
# APP
# ==============================

# app = hamara user-defined variable hai.
# FastAPI() ek object/instance create karta hai aur woh app mein store hota hai.

# app = FastAPI()


# ==============================
# UPLOAD FOLDER
# ==============================

# UPLOAD_FOLDER = hamara user-defined variable hai.
# Ismein folder ka path string ki form mein store hai.
# "./" ka matlab current project/folder hai.
# Yani uploaded files "uploads" folder mein save hongi.

# UPLOAD_FOLDER = "./uploads"


# ==============================
# FOLDER CREATE KARNA
# ==============================

# os.makedirs() = os module ka predefined function hai.
# Iska use folder create karne ke liye hota hai.

# UPLOAD_FOLDER = woh path hai jahan folder create karna hai.
# exist_ok=True = agar folder already exist karta hai to error na do.
# True = Python ki predefined Boolean value hai.

# os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ==============================
# STATIC FILES
# ==============================

# app.mount() = FastAPI app ka predefined method hai.
# Iska use URL path ko kisi folder/directory ke saath connect karne ke liye hota hai.

# "/static" = user-defined URL path/string hai.
# StaticFiles() = FastAPI ki predefined class hai.
# directory=UPLOAD_FOLDER = batata hai ke actual files kis folder mein hain.
# name="static" = mount ka naam hai.

# Iska result:
# uploads/cat.jpg
# ko browser/client ke through
# /static/cat.jpg
# se access kiya ja sakta hai.

# app.mount("/static", StaticFiles(directory=UPLOAD_FOLDER), name="static")


# ==============================
# UPLOAD API
# ==============================

# @app.post("/upload")
# @app.post = FastAPI ka predefined decorator/method hai.
# "/upload" = user-defined route/path hai.
# Jab client POST request /upload par bhejega,
# neeche wala file_upload function execute hoga.

# @app.post("/upload")


# ==============================
# FUNCTION + UPLOADFILE
# ==============================

# file_upload = hamara user-defined function hai.

# file = hamara user-defined parameter/variable hai.
# Ye koi predefined naam nahi hai.
# Iska naam kuch bhi ho sakta hai:
# file, my_file, uploaded_file etc.

# UploadFile = FastAPI ki predefined class/type hai.
# file: UploadFile ka matlab:
# "file naam ka parameter UploadFile type ka hoga."

# def file_upload(file: UploadFile):


    # ==============================
    # FILE PATH
    # ==============================

    # file_path = hamara user-defined variable hai.
    # os.path.join() = Python ke os module ka predefined function hai.
    # Iska use folder path aur filename ko properly join karne ke liye hota hai.

    # file.filename = UploadFile object ka predefined attribute hai.
    # Ye uploaded file ka naam deta hai.
    # Example: "cat.jpg"

    # Agar:
    # UPLOAD_FOLDER = "./uploads"
    # file.filename = "cat.jpg"
    #
    # to file_path:
    # "./uploads/cat.jpg"
    # ban jayega.

    # file_path = os.path.join(UPLOAD_FOLDER, file.filename)


    # ==============================
    # FILE OPEN / CREATE
    # ==============================

    # open() = Python ka built-in function hai.
    # Iska use file ko open ya create karne ke liye hota hai.

    # file_path = woh location jahan file save karni hai.
    # "wb" = file mode:
    # w = write
    # b = binary
    #
    # Binary mode images, PDFs, videos waghera ke liye use hota hai.

    # buffer = hamara user-defined variable hai.
    # open() jo file object return karta hai,
    # woh buffer variable mein store ho jata hai.

    # with = file ko safely manage karta hai.
    # Is block ka kaam complete hone ke baad
    # file automatically close/manage ho jati hai.

    # with open(file_path, "wb") as buffer:


        # ==============================
        # UPLOADED FILE COPY KARNA
        # ==============================

        # shutil.copyfileobj() = shutil module ka predefined function hai.
        # Iska kaam ek file object ka data doosre file object mein copy karna hai.

        # file.file = UploadFile object ke andar actual uploaded file object.
        # buffer = destination/new file ka file object.

        # Yani:
        # uploaded file
        #       ↓
        # file.file
        #       ↓
        # copyfileobj()
        #       ↓
        # buffer
        #       ↓
        # ./uploads/filename

        # shutil.copyfileobj(file.file, buffer)


    # ==============================
    # FILE URL
    # ==============================

    # file_url = hamara user-defined variable hai.
    # f-string ki madad se file ka URL banaya ja raha hai.

    # file.filename = uploaded file ka naam.
    # Agar filename "cat.jpg" hai:
    #
    # file_url = "/static/cat.jpg"

    # file_url = f"/static/{file.filename}"


    # ==============================
    # RESPONSE
    # ==============================

    # return mein dictionary return ho rahi hai.
    # "filename" aur "fileurl" user-defined keys hain.
    #
    # file.filename = uploaded file ka naam.
    # file_url = file ka accessible URL.

    # Example response:
    #
    # {
    #     "filename": "cat.jpg",
    #     "fileurl": "/static/cat.jpg"
    # }

    # return {"filename": file.filename, "fileurl": file_url}


# ==============================
# COMPLETE FLOW
# ==============================

# 1. Client/user file upload karta hai.
#
# 2. POST /upload request FastAPI ko milti hai.
#
# 3. file parameter mein uploaded file
#    UploadFile object ki form mein receive hoti hai.
#
# 4. file.filename se file ka naam milta hai.
#
# 5. os.path.join() se file ka complete path banta hai.
#
# 6. open(file_path, "wb") destination file ko
#    write-binary mode mein open/create karta hai.
#
# 7. shutil.copyfileobj() uploaded file ko
#    uploads folder mein copy karta hai.
#
# 8. /static route ki wajah se uploaded file
#    frontend/client ke liye accessible ho jati hai.
#
# 9. API filename aur file URL response mein return karti hai.
#
#
# MAIN IDEA:
# Client → File Upload → FastAPI → UploadFile
# → uploads folder → Static URL → Client
