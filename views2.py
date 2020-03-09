from aiohttp import web
import bson
from bson import ObjectId
import datetime
from aiohttp_jwt import login_required
import jwt
from .mylogger import LOG
import json
routes = web.RouteTableDef()


def serialize(data):
    d = {}
    for i in data:
        if isinstance(i["_id"], ObjectId):
            str(i["_id"])


class CustomEncoder(json.JSONEncoder):
    """A C{json.JSONEncoder} subclass to encode documents that have fields of
    type C{bson.objectid.ObjectId}, C{datetime.datetime}
    """
    def default(self, obj):
        if isinstance(obj, bson.objectid.ObjectId):
            return str(obj)
        elif isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


@routes.get("/")
async def index(request):
    LOG.info("------ in the index api")
    return web.Response(text='Hello Aiohttp!', status=200)


@routes.post("/register")
async def registration(request):
    LOG.info("request info at registration:{0}".format(dir(request)))
    req_data = await request.json()
    db = request.app["db"]
    curs = await db.user.find_one({"username": req_data["username"]})
    if curs is None:
        inserted_id = await db.user.insert_one(await request.json())
        return web.json_response({"message": "inserted", "id": str(inserted_id.inserted_id)}, status=200)
    else:
        return web.json_response({"message":"user already present"}, status=200)


@routes.get("/users")
@login_required
async def get_users(request):
    cursor = request.app["db"].user.find({})
    list_users = []
    enc = CustomEncoder()
    for document in await cursor.to_list(length=100):
        list_users.append(enc.encode(document))
    return web.json_response({"userslist": list_users}, status=200)


@routes.post("/login")
async def do_login(request):
    req_data = await request.json()
    db = request.app["db"]
    secret_key = request.app["secretkey"]
    curs = await db.user.find_one({"username": req_data["username"], "password": req_data["password"]})
    if curs is None:
        return web.json_response({"message": "no user found"}, status=200)
    else:
        jwt_key = jwt.encode({"username": req_data["username"]}, secret_key).decode('UTF-8')
    return web.json_response({"jwt_key": jwt_key}, status=200)


