from fastapi import FastAPI,HTTPException,Query
from db.database import create_db_and_tables,session_dep
from db.models import Service,Barber,User
from schemas import CreateService,ServiceResponse,BarberResponse,CreateBarber

from db.crud import insert_row,select_rows,select_row,delete_row,update_row

from typing import Annotated

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_db_and_tables()
    yield

app=FastAPI(lifespan=lifespan)

@app.get('/')
async def root():
    return 'Hola vean Arcane'

#Services endpoints

@app.post('/services',response_model=ServiceResponse)
async def create_service(service:CreateService,session:session_dep):
    return insert_row(service,session,Service)
    

@app.get('/services/',response_model=list[ServiceResponse])
async def get_services(session:session_dep,skip:int=0,limit:Annotated[int, Query(le=4)]=4):
    return select_rows(session,Service)

@app.get('/services/{service_id}',response_model=ServiceResponse)
async def get_service(service_id:int,session:session_dep):
    return select_row(service_id,session,Service)

#Barbers endpoints

@app.post('/barbers/',response_model=BarberResponse)
async def create_barber(barber:CreateBarber,session:session_dep):
    return insert_row(barber,session,Barber)

