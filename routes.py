# aiohttp_polls/routes.py
from views import login
from views2 import routes
from mylogger import LOG

def setup_routes(app):
    LOG.info("------------- setup routes.")
    app.router.add_get('/login', login)
    app.add_routes(routes)