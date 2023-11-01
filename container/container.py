import logging
from typing import TypeVar
from dependency_injector import containers, providers
from core.video_module.service.videoService import VideoService
from database.database import Base, Database
from domain.video_module.entity.Image import Image
from domain.video_module.entity.types import Type
from repositories.MySQLRepository import MySQLRepository





Model = TypeVar("Model", bound=Base)

class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=["core.electronic_module.controller.electronicController"])

    db = providers.Singleton(
        Database, db_url='mysql+pymysql://root:irda0205@localhost/miresto')

    ################################################################### ADMINISTRATION MODULE ####################################################


    repository_image_provider = providers.Factory(
        MySQLRepository,
        session_factory=db.provided.session,
        entity_type=Image
    )

    repository_type_provider = providers.Factory(
        MySQLRepository,
        session_factory=db.provided.session,
        entity_type=Type
    )
    
    video_service_provider = providers.Factory(
        VideoService,
        repository_image_provider
    )