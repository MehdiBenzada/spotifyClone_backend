from fastapi import HTTPException,Depends
import uuid
import bcrypt
from database import get_db
from models.user import User
from pydantic_schemas.user_create import UserCreate
from fastapi import APIRouter
from sqlalchemy.orm import Session
from pydantic_schemas.user_login import UserLogin
router=APIRouter()


@router.post('/signup',status_code=201)
def signup_user(user:UserCreate,db: Session= Depends(get_db)):
    # search for email in database
    user_db= db.query(User).filter(User.email==user.email).first()
    if  user_db:
        raise HTTPException(400,"email already exists")
        return "email already exists"
    #hashing password
    hashed_pw=bcrypt.hashpw(user.password.encode(),bcrypt.gensalt())
    #adding to database
    newuser=User(id=str(uuid.uuid4()),email=user.email,password=hashed_pw,name=user.name)
    db.add(newuser)
    db.commit()
    db.refresh(newuser)
    return newuser

    pass

@router.post('/login')
def login_user(user:UserLogin,db: Session = Depends(get_db)):
    #check if a user email exists already
    user_db = db.query(User).filter(User.email==user.email).first()
    if not user_db:
        raise HTTPException(400,"user with this email does not exist!!")
    # check if password is correct
    ismatch = bcrypt.checkpw(user.password.encode(),user_db.password)
    if not ismatch:
        raise HTTPException(400,"incorrect password")
    return user_db



    pass
