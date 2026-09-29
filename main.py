from fastapi import FastAPI
from database import create_db_and_tables,session_dep
from models import Service,Barber,User
from schemas import CreateService,ServiceResponse,BarberResponse,CreateBarber

from sqlmodel import select

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

@app.post('/service',response_model=ServiceResponse)
async def create_service(service:CreateService,session:session_dep):
    new_service=Service.model_validate(service)
    session.add(new_service)
    session.commit()
    session.refresh(new_service)
    return new_service

@app.get('/services/',response_model=list[ServiceResponse])
async def get_services(session:session_dep):
    service=session.exec(select(Service)).all()
    return service

@app.get('/service/{service_id}',response_model=ServiceResponse)
async def get_service(service_id:int,session:session_dep):
    service=session.get(Service,service_id)
    return service

#Barberos endpoints

@app.post('/barber',response_model=BarberResponse)
async def create_barber(barber:CreateBarber,session:session_dep):
    new_barber=Barber.model_validate(barber)
    session.add(new_barber)
    session.commit()
    session.refresh(new_barber)
    return new_barber

