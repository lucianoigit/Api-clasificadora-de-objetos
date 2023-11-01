from pydantic import BaseModel
from datetime import datetime

class SchemaImageCreate(BaseModel):
    id: int
    datos_imagen: bytes
    eficience: int
    fecha_creacion: datetime

    class Config:
        orm_mode = True
