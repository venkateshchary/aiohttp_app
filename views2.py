from aiohttp import web
from mylogger import LOG

routes = web.RouteTableDef()


@routes.get("/")
async def index(request):
    LOG.info("------ in the index api")
    return web.Response(text='Hello Aiohttp!')
    