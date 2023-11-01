from sqlalchemy import Column, Integer, String, LargeBinary, DateTime
from sqlalchemy.ext.declarative import declarative_base
from database.database import Base




class Type(Base):
    __tablename__ = 'Tipos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255))
