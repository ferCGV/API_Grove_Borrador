from sqlmodel import SQLModel,Field
from pydantic import EmailStr


### 
###
### User
class UserBase(SQLModel):
    name:str
    email:EmailStr

class CreateUser(UserBase):
    password:str
    device_token:str|None=Field(default=None)

class UserResponse(UserBase):
    id:int


### 
###
### Barber
class CreateBarber(SQLModel):
    name:str
    especialidad:str|None=Field(default=None)
    activo:bool=Field(default=True)

class BarberResponse(CreateBarber):
    id:int

### 
###
### Service
class CreateService(SQLModel):
    name:str
    description:str
    price:float
    duracion_minutos:int

class Service(CreateService):
    id:int

