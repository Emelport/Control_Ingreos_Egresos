from typing import Union
from fastapi import FastAPI
from models import User, Base # Importa Base para crear la base de datos
from database import engine, SessionLocal  # Importa el motor y el generador de sesiones

# Creamos la base de datos al iniciar la aplicación
Base.metadata.create_all(engine)

app = FastAPI()

# EJECUTAR SERVIDOR
# uvicorn main:app --reload

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    with SessionLocal() as session:
        user = session.query(User).filter(User.id == user_id).first()
        return user
    
#Registrar un user
@app.put("/users/{user_id}")
def create_user(user_id: int, email: str, hashed_password: str, is_active: bool):
    with SessionLocal() as session:
        user = User(id=user_id, email=email, hashed_password=hashed_password, is_active=is_active)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

#Cerrar la sesion de la base de datos
    