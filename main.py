from fastapi import FastAPI
from container.container import Container
from core.electronic_module.controller.electronicController import router as controllerMicroRouter




def create_app() -> FastAPI:
    container = Container() # Traigo mi contenedor de dependencias
    db = container.db() # Instancio mi base de datos
    db.create_database() # Creo la base de datos
    app = FastAPI(debug = True)
    app.container = container
    app.include_router(controllerMicroRouter)
    
    return app

app = create_app() # Creo la App
    
    
# La arquitectura de este proyecto es en capas, se separa la etapa de persistencia, domain, y logica
# se eliminan responsabilidades cruzadas
# se utiliza un repositorio generico para interaccion con la BDD
# se utilza el ORM de SQLAlchemy para la generacion de tablas 
# se utilizan inyecciones de dependencias para los servicios
# se utiliza web sockets para la comunicacion y endpoints con arduino
# se utiliza un modelo de machine learnigs

