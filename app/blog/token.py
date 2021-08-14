
from typing import Optional
from datetime import timedelta, datetime
from jose import JWTError, jwt
from blog import schemas

SECRET_KEY = "541bc6ce3af3e3963e3e4f126c84f22801ff39b472e58b039155814d3b6eb7b9"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str, credentials_exception: str):
  try:
      payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
      email: str = payload.get("sub")
      if email is None:
          raise credentials_exception
      token_data = schemas.TokenData(email=email)
  except JWTError:
      raise credentials_exception

  