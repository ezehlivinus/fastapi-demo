from fastapi.exceptions import HTTPException
from blog import schemas
from blog import models
from blog.hashing import Hash
from sqlalchemy.orm import Session
from fastapi import status


def create(request, db: Session):
  hashed_password = Hash.bcrypt(request.password)
  new_user = models.User(name = request.name, email = request.email, password = hashed_password)
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  
  return new_user


def show(id, db: Session):
  user = db.query(models.User).filter(models.User.id == id).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user not found')
  
  return user