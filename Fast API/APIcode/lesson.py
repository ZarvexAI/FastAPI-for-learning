#get (frontend ky paas data lana hy backend sy)
#post (frontend sy data dena hy backend ko)
#put (update data on backend)
#delete (deletes data)


from fastapi import FastAPI
app=FastAPI()
@app.get('/')
def hello_world():
    return {"Hello":"world"}

#ip then port then route and ip and port are replaced by domain names
