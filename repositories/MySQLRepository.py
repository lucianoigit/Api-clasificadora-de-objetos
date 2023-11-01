from contextlib import AbstractContextManager
from sqlalchemy.orm import Session
from typing import Callable, Iterator, Type, TypeVar
import logging
from database.database import Base

Entity = TypeVar("Entity", bound=Base)


# Mediante este repositorio hago las modificaciones en la base de datos, separo la capa de persistencia, domain y logica (core)


class MySQLRepository():
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]], entity_type: Type[Entity]) -> None:
        self.session_factory = session_factory
        self.entity_type = entity_type

    def get_all(self) -> Iterator:
        with self.session_factory() as session:
            return session.query(self.entity_type)

    def get_by_id(self, entity_id: int) -> Type:
        logging.info("No se encontró la sesión")
        with self.session_factory() as session:
            logging.warning("Sesión encontrada")
            item = session.query(self.entity_type).filter(
                self.entity_type.id == entity_id).first()
            logging.info("Encontré el ítem: %s", item)
            if not item:
                logging.info("No encontré el ítem")
                raise Exception(
                    f"{self.entity_type.__name__} with id {entity_id} not found.")
            logging.info(f"Tipo de ítem: {type(item)}")
            return item

    def create(self, item_data) -> None:
        with self.session_factory() as session:
            logging.warning("Accediendo al repositorio")
            session.add(item_data)
            session.commit()

    def update(self, item_data) -> None:
        with self.session_factory() as session:
            item = self.get_by_id(item_data.id)
            if not item:
                raise Exception(
                    f"{self.entity_type.__name__} with id {item_data.id} not found.")

            for key, value in item_data.__dict__.items():
                setattr(item, key, value)
            session.merge(item)
            session.commit()

    def delete_by_id(self, item_id: int) -> None:
        with self.session_factory() as session:
            item = session.query(self.entity_type).filter(
                self.entity_type.id == item_id).first()
            if not item:
                raise Exception(
                    f"{self.entity_type.__name__} with id {item_id} not found.")

            session.delete(item)
            session.commit()
