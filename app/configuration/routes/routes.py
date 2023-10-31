from dataclasses import dataclass
from fastapi import FastAPI


@dataclass(frozen=True)
class Routes:
    """
    Класс для регистрации роутеров в приложении

    routers: Кортеж роутеров, которые нужно зарегистрировать в приложении
    """

    routers: tuple

    def register_routers(self, app: FastAPI):

        for router in self.routers:
            app.include_router(router)
