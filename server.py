from fastapi import FastAPI,path

app = FastAPI()
@app.get("/get_blogs")
def get_blogs():
   return {"input":{"get blogs":"  "}}
@app.get("/get_blogs/{blog_id}")
def get_blogs():
   return {"input":{"blog id":" "}}
@app.post("/create_blog")
def create_blogs():
   return {"process":{"post blog":" "}}
@app.post("/delete")
def delete_blog():
   return {"remove":{"delete blog":"  "}}
@app.post("/update")
def update_blog():
    return {"change":{"update blog":" "}}