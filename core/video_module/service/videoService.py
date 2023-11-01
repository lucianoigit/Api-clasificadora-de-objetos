from typing import List
from fastapi import FastAPI, HTTPException
import cv2
import numpy as np
from domain.video_module.dtos import SchemaImageCreate
from domain.video_module.entity.Image import Image

app = FastAPI()

class VideoService:
    def __init__(self, repository_image):
        self._repository_image = repository_image
        # Configuracion de la comunicacion serie
        self.cap = cv2.VideoCapture(0)
        # Modelo de clasificación de imágenes
        self.model = cv2.dnn.readNet('modelo_weights', 'modelo_cfg')  

    def create_image(self, image_data: SchemaImageCreate):

        new_image = Image(**image_data.__dict__())
        return self._repository_image.create(new_image)

    def delete_image(self, image_id: int):
        self._repository_image.delete_by_id(image_id)

    def get_image_by_id(self, image_id: int):
        return self._repository_image.get_by_id(image_id)

    def get_all_image(self) -> List[Image]:
        return list(self._repository_image.get_all())

    def update_image(self, image_data: SchemaImageCreate): # Debo completar
        return None

    def clasificar_imagen(self, image):
        resultado = self.model  # Depende del modelo
        return resultado

    def recibir_video(self):
        try:
            ret, frame = self.cap.read()

            if not ret:
                raise HTTPException(status_code=500, detail="Error al capturar video")

            # Clasificación de objetos de cada cuadro del video
            resultado_clasificacion = self.clasificar_imagen(frame)
            
            # Guardo la imagen en la bdd
            self.save_image(frame, resultado_clasificacion)

            return {"frame": frame, "resultado_clasificacion": resultado_clasificacion}

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al recibir el video: {str(e)}")

    def save_image(self, image, resultado_clasificacion):

        try:
   
            image_bytes = cv2.imencode('.jpg', image)[1].tostring()

            image_data = SchemaImageCreate(datos_imagen=image_bytes, eficience=resultado_clasificacion)

            self.create_image(image_data)

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al guardar la imagen clasificada: {str(e)}")
