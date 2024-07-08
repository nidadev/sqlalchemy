from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import *
from schemas import UserCreate
from crud import *

app = FastAPI()

Base.metadata.create_all(bind = engine)

def get_db():
    db = SessionLocal()
    try :
        yield db
    finally:
        db.close

@app.post("user/create")
async def create_user_api(user:UserCreate, db : Session = Depends(get_db)):
    return create_user(db,user)