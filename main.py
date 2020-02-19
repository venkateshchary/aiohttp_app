# aiohttp_polls/main.py
import logging
from aiohttp import web
from routes import setup_routes
import motor.motor_asyncio

async def setup_db():
    client= motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017)
    db = client['test_database']
    return db


async def init_app():
    app = web.Application(debug=True)
    db = await setup_db()
    app['db'] =db
    setup_routes(app)
    return app


def main():
    logging.basicConfig(level=logging.DEBUG)
    app = init_app()
    
    web.run_app(app)


if __name__ == '__main__':
    main()
