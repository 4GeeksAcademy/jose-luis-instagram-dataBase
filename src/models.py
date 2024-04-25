import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, LargeBinary
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
 
# CREACION DE TABLE USUARIO INSTAGRAM

class Usuario(Base):
    __tablename__ = 'usuario'
   
    id_usuario = Column(Integer, primary_key=True)
    name = Column(String(250))
    nombre_usuario = Column(String(250))
    email = Column(String(250), nullable=False)
    contraseña =  Column(String(250),nullable=False)
    fecha_registro=(Column(Date))

    def to_dict(self):
        return {}
# CREACION DE LA TABLA PUBLICACION INSTAGRAM

class Publicacion(Base):
    __tablename__ = 'publicacion'
   
    id_publicacion = Column(Integer, primary_key=True)
    image = Column(LargeBinary, nullable = True)
    descripcion =  Column(String(250))
    fecha_publicacion=(Column(Date))
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    usuario = relationship('Usuario')

    def to_dict(self):
        return {}


# CREACION DE LA TABLA COMENTARIO DE INSTAGRAM
class Comentario(Base):
    __tablename__ = 'comentario'
   
    id_comentario = Column(Integer, primary_key=True)
    comentario =  Column(String(250))
    fecha_comentario=(Column(Date))
    id_publicacion = Column(Integer, ForeignKey('publicacion.id_publicacion'))
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    usuario = relationship('Usuario')
    publicacion = relationship('Publicacion')


    def to_dict(self):
        return {}

    
# CREACION DE LA TABLA LIKE DE INSTAGRAM
class Like(Base):
    __tablename__ = 'like'
   
    id_like = Column(Integer, primary_key=True)
    id_publicacion = Column(Integer, ForeignKey('publicacion.id_publicacion'))
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    fecha_like=(Column(Date))
    usuario = relationship('Usuario')
    publicacion = relationship('Publicacion')

    def to_dict(self):
        return {}
    
#CREACION DE LA TABLA SEGUIR  DE INSTAGRAM

class Seguir(Base):
    __tablename__ = 'Seguir'
   
    id_Seguir = Column(Integer, primary_key=True)
    id_usuario_seguido = Column(Integer, ForeignKey('usuario.id_usuario'))
    id_usuario_seguidor = Column(Integer, ForeignKey('usuario.id_usuario'))
    fecha_seguimiento =(Column(Date))
    usuario = relationship('Usuario')
    

    def to_dict(self):
        return {}
    
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
