# aiohttp_polls/main.py
import logging
from aiohttp import web
from routes import setup_routes


async def init_app():
    app = web.Application(debug=True)
    setup_routes(app)
    return app


def main():
    logging.basicConfig(level=logging.DEBUG)
    app = init_app()
    web.run_app(app)


if __name__ == '__main__':
    main()