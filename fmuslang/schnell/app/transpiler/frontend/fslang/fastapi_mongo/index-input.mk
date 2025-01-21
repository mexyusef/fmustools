--% index/fmus
fastapi-mongo,d(/mk)
  %__TEMPLATE_HOST=0.0.0.0
  %__TEMPLATE_PORT=9000
__TEMPLATE_DB_INIT
	apps,d(/mk)
__TEMPLATE_APP_CONTENT
	core,d(/mk)
		main.py,f(e=__FILE__=main.py)
		config.py,f(e=__FILE__=config.py)
		routes.py,f(e=__FILE__=routes.py)
	.env,f(e=__FILE__=.env)
	run.sh,f(e=__FILE__=run.sh)
	docker-compose.yml,f(e=__FILE__=docker-compose.yml)
	$*chmod a+x run.sh
--#

--% docker-compose.yml
version: '3'
services:
  database:
    image: 'mongo'
    # container_name: 'mymongocontainer'
    environment:
      - MONGO_INITDB_DATABASE=__TEMPLATE_DBNAME
      - MONGO_INITDB_ROOT_USERNAME=__TEMPLATE_DBUSER
      - MONGO_INITDB_ROOT_PASSWORD=__TEMPLATE_DBPASS
    ports:
      - '27017-27019:27017-27019'

# MONGODB_URI=mongodb://usef:rahasia@localhost:27017/tempdb?authSource=admin
--#

--% template/apps_model
# __TEMPLATE_COLUMN_KEY
# __TEMPLATE_COLUMN_PARAMS
# __TEMPLATE_COLUMN_ARGS
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
import asyncio
import motor.motor_asyncio
client = motor.motor_asyncio.AsyncIOMotorClient('__TEMPLATE_DBTYPE://__TEMPLATE_DBUSER:__TEMPLATE_DBPASS@__TEMPLATE_DBHOST:__TEMPLATE_DBPORT')

# https://stackoverflow.com/questions/65542103/future-task-attached-to-a-different-loop
# https://stackoverflow.com/questions/41584243/runtimeerror-task-attached-to-a-different-loop
client.get_io_loop = asyncio.get_running_loop

database = client.__TEMPLATE_DBNAME
collection = database.__TABLENAME_LOWER


class __TABLENAME_CASE(BaseModel):
__TEMPLATE_MODEL_KOLOM


async def fetch_all___TABLENAME_LOWERs():
  print('fetch_all___TABLENAME_LOWERs #1')
  __TABLENAME_LOWERs = []
  print('fetch_all___TABLENAME_LOWERs #2: mau coll find')
  cursor = collection.find({})
  print('fetch_all___TABLENAME_LOWERs #3: terima coll find', cursor)
  async for document in cursor:
    print('fetch_all___TABLENAME_LOWERs #4: loop doc:', document)
    __TABLENAME_LOWERs.append(__TABLENAME_CASE(**document))
  print('fetch_all___TABLENAME_LOWERs #5: mau return prods', __TABLENAME_LOWERs)
  return __TABLENAME_LOWERs


async def fetch_one___TABLENAME_LOWER(__TEMPLATE_COLUMN_KEY):
  document = await collection.find_one(
    {
      "__TEMPLATE_COLUMN_KEY": __TEMPLATE_COLUMN_KEY
    }
  )
  return document


async def create___TABLENAME_LOWER(__TABLENAME_LOWER):
  document = __TABLENAME_LOWER
  result = await collection.insert_one(document)
  return document


async def update___TABLENAME_LOWER(__TEMPLATE_COLUMN_ARGS):
  await collection.update_one(
    {
      "__TEMPLATE_COLUMN_KEY": __TEMPLATE_COLUMN_KEY
    }, 
    {
    "$set": {
        # "description": desc
__TEMPLATE_COLUMNS_NONKEY_ASDICT
      }
    }
  )
  document = await collection.find_one({"__TEMPLATE_COLUMN_KEY": __TEMPLATE_COLUMN_KEY})
  return document


async def remove___TABLENAME_LOWER(__TEMPLATE_COLUMN_KEY):
  await collection.delete_one({"__TEMPLATE_COLUMN_KEY": __TEMPLATE_COLUMN_KEY})
  return True


# routes
router = APIRouter()


@router.get("/api/__TABLENAME_LOWER")
async def read___TABLENAME_LOWERs_api():
  print('requesting all __TABLENAME_LOWER')
  response = await fetch_all___TABLENAME_LOWERs()
  print('receiving list:', response)
  return response


@router.get("/api/__TABLENAME_LOWER/{__TEMPLATE_COLUMN_KEY}", response_model=__TABLENAME_CASE)
async def get___TABLENAME_LOWER_api(__TEMPLATE_COLUMN_KEY: str):
  response = await fetch_one___TABLENAME_LOWER(__TEMPLATE_COLUMN_KEY)
  if response:
    return response
  raise HTTPException(404, f"There is no __TABLENAME_LOWER with the __TEMPLATE_COLUMN_KEY {__TEMPLATE_COLUMN_KEY}")


@router.post("/api/__TABLENAME_LOWER/", response_model=__TABLENAME_CASE)
async def create___TABLENAME_LOWER_api(__TABLENAME_LOWER: __TABLENAME_CASE):
  print('create __TABLENAME_LOWER #0:', __TABLENAME_LOWER)
  if not isinstance(__TABLENAME_LOWER, dict):
    print('redicking...')
    __TABLENAME_LOWER = __TABLENAME_LOWER.dict()
  response = await create___TABLENAME_LOWER(__TABLENAME_LOWER)
  if response:
    return response
  raise HTTPException(400, "Something went wrong")


@router.put("/api/__TABLENAME_LOWER/{__TEMPLATE_COLUMN_KEY}/", response_model=__TABLENAME_CASE)
async def update___TABLENAME_LOWER_api(__TEMPLATE_COLUMN_PARAMS):
  response = await update___TABLENAME_LOWER(__TEMPLATE_COLUMN_ARGS)
  if response:
    return response
  raise HTTPException(404, f"There is no __TABLENAME_LOWER with the __TEMPLATE_COLUMN_KEY {__TEMPLATE_COLUMN_KEY}")


@router.delete("/api/__TABLENAME_LOWER/{__TEMPLATE_COLUMN_KEY}")
async def delete___TABLENAME_LOWER_api(__TEMPLATE_COLUMN_KEY):
  response = await remove___TABLENAME_LOWER(__TEMPLATE_COLUMN_KEY)
  if response:
    return "Successfully deleted __TABLENAME_LOWER"
  raise HTTPException(404, f"There is no __TABLENAME_LOWER with the __TEMPLATE_COLUMN_KEY {__TEMPLATE_COLUMN_KEY}")
--#

--% routes.py
from fastapi import APIRouter

__TEMPLATE_ROUTE_IMPORTS

api_router = APIRouter()
__TEMPLATE_ROUTE_PATHS
--#

--% .env
API_V1_STR="/api/v1"
PROJECT_NAME="FastAPI"
SQLALCHEMY_DATABASE_URI="__TEMPLATE_DBTYPE://__TEMPLATE_DBUSER:__TEMPLATE_DBPASS@__TEMPLATE_DBHOST:__TEMPLATE_DBPORT/__TEMPLATE_DBNAME"
--#

--% config.py
import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):
  API_V1_STR: str = "/api/v1"
  PROJECT_NAME: str = "FastAPI"
  SECRET_KEY: str = secrets.token_urlsafe(32)
  SQLALCHEMY_DATABASE_URI: str = "__TEMPLATE_DBTYPE://__TEMPLATE_DBUSER:__TEMPLATE_DBPASS@__TEMPLATE_DBHOST:__TEMPLATE_DBPORT/__TEMPLATE_DBNAME"

  class Config:
    env_file = ".env"


settings = Settings()

--#

--% main.py
import uvicorn
from fastapi import FastAPI

from .config import settings
from .routes import api_router

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
  return {"status": "OK"}

@app.get("/ping")
async def ping():
  return {"ping": "pong"}

if __name__ == "__main__":
  uvicorn.run(app, host="__TEMPLATE_HOST", port=__TEMPLATE_PORT)
--#

--% run.sh
python -m core.main
--#
