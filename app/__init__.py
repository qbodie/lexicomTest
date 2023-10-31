from fastapi import FastAPI
from app.configuration.server import Server


def create_app(_=None) -> FastAPI:
    """ Возвращает созданное и настроенное приложение FastAPI """

    app = FastAPI()

    return Server(app).get_app()
