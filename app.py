from fastapi import FastAPI, Request, Depends, Form, HTTPException, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean, func, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship, joinedload
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime

import uvicorn
app = FastAPI()


@app.get('/')
def hello_world():
    return 'Hello World!'

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8013)
