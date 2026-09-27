from sqlmodel import SQLModel,Field

class User(SQLModel,table=True):
    id:int|None=Field(default=None,primary_key=True)
    name:str
    email:str=Field(index=True,unique=True)
    hashed_password:str
    device_token:str|None=Field(default=None)

class Barber(SQLModel,table=True):
    id:int|None=Field(default=None,primary_key=True)
    name:str
    especialidad:str|None=Field(default=None)
    activo:bool=Field(default=True)


class Service(SQLModel,table=True):
    id:int|None=Field(default=None,primary_key=True)
    name:str
    description:str
    price:float
    duracion_minutos:int


