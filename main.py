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
    return {"Hello": "Prueba de API con FastAPI"}


#-----------------------INICIO USUARIOS-------------------------------
#Obtener todos los users
@app.get("/users/")
def read_users():
    with SessionLocal() as session:
        users = session.query(User).all()
        return users

#Obtener un user por id
@app.get("/users/{user_id}")
def read_user(user_id: int):
    with SessionLocal() as session:
        user = session.query(User).filter(User.id == user_id).first()
        return user
    
#Registrar un user
@app.put("/users/{user_id}")
def create_user(user_id: int, username: str, password: str, email: str, id_role: int, is_active: bool):
    with SessionLocal() as session:
        user = User(id=user_id, username=username, password=password, email=email, id_role=id_role, is_active=is_active)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

#Actualizar un user solo los campos que se deseen
@app.patch("/users/{user_id}")
def update_user(user_id: int, username: str, password: str, email: str, id_role: int, is_active: bool):
    with SessionLocal() as session:
        user = session.query(User).filter(User.id == user_id).first()
        if username:
            user.username = username
        if password:
            user.password = password
        if email:
            user.email = email
        if id_role:
            user.id_role = id_role
        if is_active:
            user.is_active = is_active
        session.commit()
        session.refresh(user)
        return user
    
#Eliminar un user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    with SessionLocal() as session:
        user = session.query(User).filter(User.id == user_id).first()
        session.delete(user)
        session.commit()
        return user
#-----------------------FIN USUARIOS---------------------------------
#-----------------------INICIO ROLES---------------------------------
    