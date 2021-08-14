


from fastapi.exceptions import HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from blog import models
from blog import database
from fastapi import APIRouter, status
from fastapi import Depends
from sqlalchemy.orm import Session
from blog import schemas, token
from blog.hashing import Hash

router = APIRouter(
  tags=['Authentication']
)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
  user = db.query(models.User).filter(models.User.email == request.username).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail='invalid login details')
  if not Hash.verify(request.password, user.password):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail='invalid login details')
  # generate a jwt token and return it
  access_token = token.create_access_token(data={"sub": user.email})
  return {"access_token": access_token, "token_type": "bearer"}


