from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import time
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db

from .routers import posts, users, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware




#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


   

app.include_router(posts.router) 
app.include_router(users.router) 
app.include_router(auth.router) 
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "New Beginnings"}   


#my_posts = [{"title": "title of post 1", "content": "content of post 1", "id":1}, 
            #{"title": "fav food", "content": "I Like Pizza", "id": 2}]

#def find_post(id):
    #for p in my_posts:
        #if p["id"] == id:
            #return p

#def find_index_post(id):
   # for i, p in enumerate(my_posts):
       # if p['id'] == id:
       #     return i




