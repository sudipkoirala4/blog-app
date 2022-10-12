from fastapi import FastAPI
app = FastAPI()
@app.get("/get_blogs")
def get_blogs():
   return {"data":{"get blogs":"  "}}
@app.get("/get_blogs/{blog_id}")
def get_blogs():
   return {"data":{"blog id":" "}}
@app.post("/create_blog")
def create_blogs():
   return {"data":{"post blog":" "}}
@app.post("/delete")
def delete_blog():
   return {"data":{"delete blog":"  "}}
@app.post("/update")
def update_blog():
    return {"data":{"update blog":" "}}