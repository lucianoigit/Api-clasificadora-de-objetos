import logging
from typing import List, Union
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from container.container import Container
from dependency_injector.wiring import Provide, inject
from sqlalchemy.exc import SQLAlchemyError

from core.video_module.service.videoService import VideoService


router = APIRouter(
    prefix='/prediction',
    tags=['prediction'],
)

logging.warning("accediendo al crud")


@router.get("/")
@inject
def get_prediction(
    video_service_class: VideoService = Depends(
        Provide[Container.video_service_provider]),

):
    prediction = video_service_class.clasificar_imagen
    return prediction

# Este es el unico endpoit necesario para utilizar el microcontrolador
# al realizar la peticion el microcontrolador el servicio verificara si es que hay un video pasandose a la api y en ese momento procesara y enviara resultados
