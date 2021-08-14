from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()



@app.get('/')
def index(limit = 10, pub: bool = None):
  return { 'data': 'blog list' }


@app.get('/blog/{id}')
def show(id: int):
  # fetch blog with id = 1
  return {'data': id}


class Blog(BaseModel):
  title: str
  body: str
  published_at: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
  return {'date': 'blog created'}

# if __name__ == '__main__':
#   uvicorn.run(app, host = '127.0.0.1', port = 9000)

  