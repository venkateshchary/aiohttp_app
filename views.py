# aiohttpdemo_polls/views.py
from aiohttp import web
from mylogger import LOG

async def login(request):
    LOG.info("-----in the login api")
    return web.json_response({"i am":"you"},status=200)

