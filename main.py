# aiohttp_polls/main.py
from aiohttp import web
<<<<<<< HEAD
import motor.motor_asyncio
from aiohttp_jwt import JWTMiddleware

sharable_secret = "venkatesh"
jwt_middleware = JWTMiddleware(
    sharable_secret, request_property="user", credentials_required=False
)


async def setup():
    client = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017)
    db = client['test_database']
    print(db)
=======
from routes import setup_routes
import motor.motor_asyncio

async def setup_db():
    client= motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017)
    db = client['test_database']
>>>>>>> 6df3bd7c92c13eff813ba0f861e090b10fcddfb8
    return db


async def init_app():
<<<<<<< HEAD
    app = web.Application(middlewares=[jwt_middleware])
    from routes import setup_routes
=======
    app = web.Application(debug=True)
    db = await setup_db()
    app['db'] =db
>>>>>>> 6df3bd7c92c13eff813ba0f861e090b10fcddfb8
    setup_routes(app)
    db = await setup()
    app["db"] = db
    app["secretkey"] = sharable_secret
    return app


def main():
    app = init_app()
    
    web.run_app(app)


if __name__ == '__main__':
    main()
