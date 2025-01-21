fastapi_mongo_app_fmus = """__TABLENAME_LOWER,d(/mk)
__TABmongo.py,f(e=__FILE__=/__TABLENAME_LOWER/mongo.py)
"""

fastapi_mongo_app_content = """
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


async def fetch_one___TABLENAME_LOWER(__TEMPLATE_COLUMN_FINDBY):
  document = await collection.find_one({"__TEMPLATE_COLUMN_FINDBY": __TEMPLATE_COLUMN_FINDBY})
  return document


async def create___TABLENAME_LOWER(__TABLENAME_LOWER):
  document = __TABLENAME_LOWER
  result = await collection.insert_one(document)
  return document


async def update___TABLENAME_LOWER(__TEMPLATE_COLUMN_ARGS):
  await collection.update_one(
    {"__TEMPLATE_COLUMN_FINDBY": __TEMPLATE_COLUMN_FINDBY}, 
    {
      "$set": {
        __TEMPLATE_COLUMN_DICT_LIKE
      }
    }
  )
  document = await collection.find_one({"__TEMPLATE_COLUMN_FINDBY": __TEMPLATE_COLUMN_FINDBY})
  return document

async def remove___TABLENAME_LOWER(__TEMPLATE_COLUMN_FINDBY):
  await collection.delete_one({"__TEMPLATE_COLUMN_FINDBY": __TEMPLATE_COLUMN_FINDBY})
  return True

# routes

router = APIRouter()

@router.get("/api/__TABLENAME_LOWER")
async def read___TABLENAME_LOWERs_api():
  print('requesting all __TABLENAME_LOWER')
  response = await fetch_all___TABLENAME_LOWERs()
  print('receiving list:', response)
  return response


@router.get("/api/__TABLENAME_LOWER/{__TEMPLATE_COLUMN_FINDBY}", response_model=__TABLENAME_CASE)
async def get___TABLENAME_LOWER_api(__TEMPLATE_COLUMN_FINDBY_TYPE):
  response = await fetch_one___TABLENAME_LOWER(__TEMPLATE_COLUMN_FINDBY)
  if response:
    return response
  raise HTTPException(404, f"There is no __TABLENAME_LOWER with the __TEMPLATE_COLUMN_FINDBY {__TEMPLATE_COLUMN_FINDBY}")


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


@router.put("/api/__TABLENAME_LOWER/{__TEMPLATE_COLUMN_FINDBY}/", response_model=__TABLENAME_CASE)
async def update___TABLENAME_LOWER_api(__TEMPLATE_COLUMN_PARAMS):
  response = await update___TABLENAME_LOWER(__TEMPLATE_COLUMN_ARGS)
  if response:
    return response
  raise HTTPException(404, f"There is no __TABLENAME_LOWER with the __TEMPLATE_COLUMN_FINDBY {__TEMPLATE_COLUMN_FINDBY}")


@router.delete("/api/__TABLENAME_LOWER/{__TEMPLATE_COLUMN_FINDBY}")
async def delete___TABLENAME_LOWER_api(__TEMPLATE_COLUMN_FINDBY):
  response = await remove___TABLENAME_LOWER(__TEMPLATE_COLUMN_FINDBY)
  if response:
    return "Successfully deleted __TABLENAME_LOWER"
  raise HTTPException(404, f"There is no __TABLENAME_LOWER with the __TEMPLATE_COLUMN_FINDBY {__TEMPLATE_COLUMN_FINDBY}")
"""
