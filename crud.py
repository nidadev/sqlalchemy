from sqlalchemy.orm import Session
from models import User
from schemas import *

def create_user(db: Session , user: UserCreate):
    db_user = User(name = user.name, email = user.email)
