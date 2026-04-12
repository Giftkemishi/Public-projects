from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base
import models
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

current_user = None

@app.get("/")
def home():
    return{"message": "Application is running!"}

@app.post("/signin") 
def signin(username: str, password: str, db: Session = Depends(get_db)):
    user = models.account(username=username, password=password)
    db.add(user)
    db.commit()
    return {"message": "account created Successfully!"}


@app.post("/login") 
def login (username: str, password: str, db: Session = Depends(get_db)):
    global current_user

    user = db.query(models.account).filter (
        models.account.username == username,
        #models.account.password == password
    ).first()

    if not user:
        return {"error": "Not found"}
    
    if user.password != password:
        return {"status": "error", "message": "Wrong password"}

    current_user = username
    return {"message": "loggin in"}
    

@app.get("/debug-users")
def debug_users(db: Session = Depends(get_db)):
    return db.query(models.account).all()
