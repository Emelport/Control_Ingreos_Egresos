from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    #NOMBRE DE LA TABLA
    __tablename__ = "users"

    #CAMPOS
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, unique=True, index=True)
    id_role = Column(Integer, ForeignKey("roles.id"))
    is_active = Column(Boolean, default=True)

    #RELACIONES
    role = relationship("Role", back_populates="users") #a
    movimientos = relationship("Movimientos", back_populates="usuario") #e


class Role(Base):
    #NOMBRE DE LA TABLA
    __tablename__ = "roles"

    #CAMPOS
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    schools_limit = Column(Integer)

    #RELACIONES
    users = relationship("User", back_populates="role") #a

class Cuentas(Base):
    #NOMBRE DE LA TABLA
    __tablename__ = "cuentas"

    #CAMPOS
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, index=True)
    saldo_neto = Column(Integer)

    #RELACIONES
    clasificaciones = relationship("Clasificaciones", back_populates="cuentas") #c


class Movimientos(Base):
    #NOMBRE DE LA TABLA
    __tablename__ = "movimientos"

    #CAMPOS
    id = Column(Integer, primary_key=True)
    fecha = Column(String)
    id_tipo_movimiento = Column(Integer, ForeignKey("tipos_movimientos.id"))
    concepto = Column(String)
    motivo = Column(String)
    persona = Column(String)
    importe = Column(Integer)
    id_clasificacion = Column(Integer, ForeignKey("clasificaciones.id"))
    id_usuario = Column(Integer, ForeignKey("users.id"))

    #RELACIONES
    usuario = relationship("User", back_populates="movimientos") #e
    TiposMovimientos = relationship("TiposMovimientos", back_populates="movimientos") #f
    clasificaciones = relationship("Clasificaciones", back_populates="movimientos") #g


class TiposMovimientos(Base):
    #NOMBRE DE LA TABLA
    __tablename__ = "tipos_movimientos"

    #CAMPOS
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, index=True)

    #RELACIONES
    movimientos = relationship("Movimientos", back_populates="TiposMovimientos") #f

class Clasificaciones(Base):
    #NOMBRE DE LA TABLA
    __tablename__ = "clasificaciones"

    #CAMPOS
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, index=True)
    id_cuenta = Column(Integer, ForeignKey("cuentas.id"))

    #RELACIONES
    movimientos = relationship("Movimientos", back_populates="clasificaciones") #g
    cuentas = relationship("Cuentas", back_populates="clasificaciones") #c