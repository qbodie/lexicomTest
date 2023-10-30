from app.configuration.routes.routes import Routes
from app.internal.routes import phones

__routes__ = Routes(routers=(phones.router, ))
