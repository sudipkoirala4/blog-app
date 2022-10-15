from fastapi import FastAPI
from pydantic import BaseModel

class Blog(BaseModel):
    id: int | None = None
    title: str
    description: str
    author: str
    date: int | None = None


app = FastAPI()


@app.post("/blogs/")
async def create_item(blog: Blog):
    return blog
