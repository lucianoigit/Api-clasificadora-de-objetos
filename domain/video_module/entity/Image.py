from sqlalchemy import Column, Integer, String, LargeBinary, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import validates
from database.database import Base



class Image(Base):
    __tablename__ = 'imagenes'

    id = Column(Integer, primary_key=True)
    datos_imagen = Column(LargeBinary)  # Almacena los datos de la imagen
    eficience = Column (Integer)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())