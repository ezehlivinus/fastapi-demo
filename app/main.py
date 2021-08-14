from blog.routers.authentication import login
from fastapi import FastAPI

from blog.database import engine
from blog import models
from blog.routers import blogs, users, authentication as auth


app = FastAPI()


models.Base.metadata.create_all(engine)


# router
app.include_router(auth.router)
app.include_router(blogs.router)
app.include_router(users.router)

