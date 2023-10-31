""" Основная конфигурация приложения """

from fastapi import FastAPI
from app.configuration.routes import __routes__


class Server:

    __app: FastAPI

    def __init__(self, app: FastAPI):
        """
        Инициализурует экземпляр класса с параметрами:

        app (FastAPI): FastAPI-приложение, к которому будет привязан этот сервер
        """

        self.__app = app
        self.__register_routers(app)

    def get_app(self) -> FastAPI:
        """
        Получает FastAPI-приложение, связанное с этим сервером

        Возвращает FastAPI
        """

        return self.__app

    @staticmethod
    def __register_events(app):
        pass

    @staticmethod
    def __register_routers(app):
        """ Регистрирует роутеры приложения """

        __routes__.register_routers(app)
