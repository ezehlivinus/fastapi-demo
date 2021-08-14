from fastapi.exceptions import HTTPException
from blog import schemas
from blog import models
from sqlalchemy.orm import Session
from fastapi import status



def get_all(db: Session):
  blogs = db.query(models.Blog).all()
  return blogs


def create(request: schemas.Blog, db: Session):
  new_blog = models.Blog(title = request.title, body = request.body, user_id = 1)
  db.add(new_blog)
  db.commit()
  db.refresh(new_blog)
  
  return new_blog

def delete(id, db: Session):
  blog = db.query(models.Blog).filter(models.Blog.id == id)
  if not blog.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='blog not found')
  
  blog.delete(synchronize_session=False)
  
  db.commit()

  return 'deleted'


def show(id, db: Session):
  blog = db.query(models.Blog).filter(models.Blog.id == id).first()
  if not blog:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
      'message': f'The blog with the id {id} not found'
    })
    
    # response.status_code = status.HTTP_404_NOT_FOUND
    # return {'message': f'The blog with id {id} is not available'}
  return blog
