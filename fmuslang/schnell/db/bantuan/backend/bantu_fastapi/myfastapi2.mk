--% program/fm.us
__REPLACE_WITH_PROJECT_DIR_OR_INPUT__,d(/mk)
  %utama=__FILE__
  %__TEMPLATE_SERVER_PORT__=9000
  %__TEMPLATE_API_PREFIX=/api/v1
__TEMPLATE_DB_INIT
__TEMPLATE_APP_INIT
  alembic.ini,f(e=utama=/myfastapi/alembic.ini)
  work.fmus,f(e=utama=/myfastapi/work.fmus)
  prestart.sh,f(e=utama=/myfastapi/prestart.sh)
  .env,f(e=utama=/myfastapi/.env)
  run.sh,f(e=utama=/myfastapi/run.sh)
  readme.md,f(e=utama=/myfastapi/readme.md)
  alembic.ini,f(e=utama=/myfastapi/alembic.ini)
  $*chmod a+x *.sh
  core,d(/mk)
    deps.py,f(e=utama=/myfastapi/core/deps.py)
    routes.py,f(e=utama=/myfastapi/core/routes.py)
    config.py,f(e=utama=/myfastapi/core/config.py)
    main.py,f(e=utama=/myfastapi/core/main.py)
    mygql.py,f(e=utama=/myfastapi/core/mygql.py)
    schema.py,f(e=utama=/myfastapi/core/schema.py)
    crud.py,f(e=utama=/myfastapi/core/crud.py)
    init.py,f(e=utama=/myfastapi/core/init.py)
    db,d(/mk)
      base.py,f(e=utama=/myfastapi/core/db/base.py)
      session.py,f(e=utama=/myfastapi/core/db/session.py)
      init.py,f(e=utama=/myfastapi/core/db/init.py)
  alembic,d(/mk)
    versions,d(/mk)
      template.py,f(e=utama=/alembic/template.py)
    env.py,f(e=utama=/alembic/env.py)
    script.py.mako,f(e=utama=/alembic/script.py.mako)
  apps,d(/mk)
    index.py,f(e=utama=/myfastapi/apps/index.py)
    common,d(/mk)
      models.py,f(e=utama=/myfastapi/apps/common/models.py)
__TEMPLATE_SERVER_APP_CONTENT

  $*qterminal 2>/dev/null &
  # migrations,d(/mk)
  #   env.py,f(e=utama=/myfastapi/migrations/env.py)
  #   versions,d(/mk)
  # $*alembic init alembic
  # $*alembic revision --autogenerate -m "di awal sekali"
  @silahkan oprek revision file lalu alembic upgrade head*
--#

--% info
belum dihandle:
migrations/env.py
__TEMPLATE_MIGRATIONS_NAMA_SATU_MODEL__

perubahan pada alembic etc

1) env.py
from alembic import context
import os, sys
curdir = os.path.dirname(__file__) # migrations
projectdir = os.path.join(curdir, os.pardir)
sys.path.insert(0, projectdir)
from core.config import settings
from core.db.base import Base
from apps.book.models import Book
target_metadata = Book.metadata
2) revision file
def upgrade():
  book_table = op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
  )
  op.bulk_insert(book_table,
    [
      {'id':1, 'name':'John Smith', 'price':42.123},
      {'id':2, 'name':'Ed Williams', 'price':42.124},
      {'id':3, 'name':'Wendy Jones', 'price':42.125},
    ]
  )
  op.create_index(op.f('ix_book_id'), 'book', ['id'], unique=False)
--#

--% /alembic/template.py
def upgrade():
  book_tablename = 'books'
  book_table = op.create_table(book_tablename,
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
  )
  op.bulk_insert(book_table, [])
  op.create_index(op.f('ix_book_id'), 'book', ['id'], unique=False)
		
--#

--% /alembic/env.py
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
import os, sys
curdir = os.path.dirname(__file__) # migrations
projectdir = os.path.join(curdir, os.pardir)
sys.path.insert(0, projectdir)
from core.config import settings
# from core.db.base import Base
# from apps.book.models import Book
__TEMPLATE_ALEMBIC_FIRSTAPP_IMPORT
target_metadata = __TEMPLATE_ALEMBIC_FIRSTAPP_NAME.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
  """Run migrations in 'offline' mode.

  This configures the context with just a URL
  and not an Engine, though an Engine is acceptable
  here as well.  By skipping the Engine creation
  we don't even need a DBAPI to be available.

  Calls to context.execute() here emit the given string to the
  script output.

  """
  url = config.get_main_option("sqlalchemy.url")
  context.configure(
    url=url,
    target_metadata=target_metadata,
    literal_binds=True,
    dialect_opts={"paramstyle": "named"},
  )

  with context.begin_transaction():
    context.run_migrations()


def run_migrations_online():
  """Run migrations in 'online' mode.

  In this scenario we need to create an Engine
  and associate a connection with the context.

  """
  connectable = engine_from_config(
    config.get_section(config.config_ini_section),
    prefix="sqlalchemy.",
    poolclass=pool.NullPool,
  )

  with connectable.connect() as connection:
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
      context.run_migrations()


if context.is_offline_mode():
  run_migrations_offline()
else:
  run_migrations_online()
--#

--% /alembic/script.py.mako
"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}


def upgrade():
  ${upgrades if upgrades else "pass"}


def downgrade():
  ${downgrades if downgrades else "pass"}

--#

--% /myfastapi/readme.md
docker exec -it pg psql -U usef postgres
create database __TEMPLATE_DBNAME

alembic revision --autogenerate -m "loading data"
./prestart.sh
./run.sh
localhost:__TEMPLATE_SERVER_PORT____TEMPLATE_API_PREFIX/<app>s

query list {
  bookList {
    id
    name
    price
  }
}

query detail {
  bookDetail(id:6619) {
    id
    name
    price
  }
}

mutation create {
  bookCreate(
    name: "buku selanjutnya semoga ada..."
    price: 42.42
  ) {
    result
  }
}

mutation update {
  bookUpdate(
    id:"6619"
    name: "buku pertama 6619 diganti la yaw"
    price: 49.49
  ) {
    result {
      id
    }
  }
}

mutation delete {
  bookDelete(
    id:"4818"
  ) {
    result
  }
}

pydantic -> BaseModel -> BookBase
                      -> BookSchema

--#

--% /myfastapi/alembic.ini
# A generic, single database configuration.

[alembic]
# path to migration scripts
script_location = alembic

# template used to generate migration files
# file_template = %%(rev)s_%%(slug)s

# timezone to use when rendering the date
# within the migration file as well as the filename.
# string value is passed to dateutil.tz.gettz()
# leave blank for localtime
# timezone =

# max length of characters to apply to the
# "slug" field
# truncate_slug_length = 40

# set to 'true' to run the environment during
# the 'revision' command, regardless of autogenerate
# revision_environment = false

# set to 'true' to allow .pyc and .pyo files without
# a source .py file to be detected as revisions in the
# versions/ directory
# sourceless = false

# version location specification; this defaults
# to alembic/versions.  When using multiple version
# directories, initial revisions must be specified with --version-path
# version_locations = %(here)s/bar %(here)s/bat alembic/versions

# the output encoding used when revision files
# are written from script.py.mako
# output_encoding = utf-8

sqlalchemy.url = postgresql://__TEMPLATE_DBUSER:__TEMPLATE_DBPASS@__TEMPLATE_DBHOST:__TEMPLATE_DBPORT/__TEMPLATE_DBNAME


[post_write_hooks]
# post_write_hooks defines scripts or Python functions that are run
# on newly generated revision scripts.  See the documentation for further
# detail and examples

# format using "black" - use the console_scripts runner, against the "black" entrypoint
# hooks=black
# black.type=console_scripts
# black.entrypoint=black
# black.options=-l 79

# Logging configuration
[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARN
handlers = console
qualname =

[logger_sqlalchemy]
level = WARN
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S

--#

--% /myfastapi/migrations/env.py
from alembic import context
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool

import os, sys
curdir = os.path.dirname(__file__) # migrations
projectdir = os.path.join(curdir, os.pardir)
sys.path.insert(0, projectdir)

from core.config import settings
from core.db.base import Base

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# from apps.book.models import Book
__TEMPLATE_MIGRATIONS_IMPORT_SATU_MODEL__
# from apps.product.models import Product

# add your model's MetaData object here
# for 'autogenerate' support
# target_metadata = Base.metadata
# target_metadata = [Book.metadata, Product.metadata]
target_metadata = [__TEMPLATE_MIGRATIONS_NAMA_SATU_MODEL__.metadata]

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
  """Run migrations in 'offline' mode.

  This configures the context with just a URL
  and not an Engine, though an Engine is acceptable
  here as well.  By skipping the Engine creation
  we don't even need a DBAPI to be available.

  Calls to context.execute() here emit the given string to the
  script output.

  """
  url = settings.SQLALCHEMY_DATABASE_URI
  context.configure(url=url, 
    target_metadata=target_metadata, 
    literal_binds=True,
    dialect_opts={"paramstyle": "named"}, 
    compare_type=True
  )

  with context.begin_transaction():
    context.run_migrations()


def run_migrations_online():
  """Run migrations in 'online' mode.

  In this scenario we need to create an Engine
  and associate a connection with the context.

  """
  configuration = config.get_section(config.config_ini_section)
  configuration["sqlalchemy.url"] = settings.SQLALCHEMY_DATABASE_URI
  connectable = engine_from_config(configuration, prefix="sqlalchemy.", poolclass=pool.NullPool)

  with connectable.connect() as connection:
    context.configure(connection=connection, target_metadata=target_metadata, compare_type=True)

    with context.begin_transaction():
      context.run_migrations()


if context.is_offline_mode():
  run_migrations_offline()
else:
  run_migrations_online()

--#

--% /myfastapi/alembic.ini

[alembic]
script_location = migrations

[post_write_hooks]

[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARN
handlers = console
qualname =

[logger_sqlalchemy]
level = WARN
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S
--#

--% /myfastapi/work.fmus
*~localhost:__TEMPLATE_SERVER_PORT__/items p json {user=name}

*~localhost:__TEMPLATE_SERVER_PORT____TEMPLATE_API_PREFIX/products
[{"id":1,"name":"apa saja","price":100.24},{"id":2,"name":"produk no 2","price":50.42}]
[{"id":1,"name":"apa saja","price":100.24}]
[]

*~localhost:__TEMPLATE_SERVER_PORT____TEMPLATE_API_PREFIX/products/5
{"detail":"The product 5 not found."}

*~localhost:__TEMPLATE_SERVER_PORT____TEMPLATE_API_PREFIX/products/2
{"id":2,"name":"produk no 2","price":50.42}

*~localhost:__TEMPLATE_SERVER_PORT____TEMPLATE_API_PREFIX/products/1
{"id":1,"name":"apa saja","price":100.24}

*~localhost:__TEMPLATE_SERVER_PORT____TEMPLATE_API_PREFIX/products p json {name=produk no 2, price=50.42}
{"id":2,"name":"produk no 2","price":50.42}
{"id":1,"name":"apa saja","price":100.24}

wmc
--#

--% /myfastapi/prestart.sh
#!/usr/bin/env sh

export PYTHONPATH=.

# Run migrations
alembic upgrade head

# Create initial data in DB
python -m core.db.init

--#

--% /myfastapi/.env
API_V1_STR="__TEMPLATE_API_PREFIX"
PROJECT_NAME="FastAPI"
SQLALCHEMY_DATABASE_URI="postgresql://__TEMPLATE_DBUSER:__TEMPLATE_DBPASS@__TEMPLATE_DBHOST:__TEMPLATE_DBPORT/__TEMPLATE_DBNAME"
--#

--% /myfastapi/run.sh
python -m core.main
--#

--% /myfastapi/core/deps.py
from typing import Generator
from .db.session import SessionLocal


def get_db() -> Generator:
  try:
    db = SessionLocal()
    yield db
  finally:
    db.close()

--#

--% /myfastapi/core/routes.py
from fastapi import APIRouter

# from apps.product import routes as product_router
__TEMPLATE_APP_ROUTE_IMPORTS

api_router = APIRouter()
# api_router.include_router(product_router.router, prefix="/products", tags=["products"])
__TEMPLATE_APP_ROUTE_LIST
--#

--% /myfastapi/core/config.py
import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):
  API_V1_STR: str = "__TEMPLATE_API_PREFIX"
  PROJECT_NAME: str = "FastAPI"
  SECRET_KEY: str = secrets.token_urlsafe(32)
  SQLALCHEMY_DATABASE_URI: str = "postgresql://__TEMPLATE_DBUSER:__TEMPLATE_DBPASS@__TEMPLATE_DBHOST:__TEMPLATE_DBPORT/__TEMPLATE_DBNAME"

  class Config:
    env_file = ".env"


settings = Settings()
--#

--% /myfastapi/core/schema.py
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
# from pydantic import BaseModel
# from graphene_pydantic import PydanticInputObjectType, PydanticObjectType

# from apps.book.schema import (
# 	HelloBook,
# 	ListBook,
# 	DetailBook,
# 	CreateBook,
# 	UpdateBook,
# 	DeleteBook,
# )
__TEMPLATE_PER_APP_SCHEMA_IMPORTS__

class Query(__TEMPLATE_PER_APP_QUERY_PARAMS__):
	pass
	

class Mutation(graphene.ObjectType):
__TEMPLATE_PER_APP_MUTATION_FIELDS__
	# book_create = CreateBook.Field()
	# book_update = UpdateBook.Field()
	# book_delete = DeleteBook.Field()

--#

--% /myfastapi/core/mygql.py
# https://stackoverflow.com/questions/65974026/fastapi-graphql-getting-error-nonetype-is-callable-when-raise-exception

import json
import typing

from starlette.graphql import GraphQLApp
from starlette import status
from starlette.background import BackgroundTasks
from starlette.concurrency import run_in_threadpool
from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse, PlainTextResponse, Response
from starlette.types import Receive, Scope, Send
from graphql.error.graphql_error import format_error


class CustomGraphQLApp(GraphQLApp):
  async def handle_graphql(self, request: Request) -> Response:
    if request.method in ("GET", "HEAD"):
      if "text/html" in request.headers.get("Accept", ""):
        if not self.graphiql:
          return PlainTextResponse(
            "Not Found", status_code=status.HTTP_404_NOT_FOUND
          )
        return await self.handle_graphiql(request)

      data = request.query_params  # type: typing.Mapping[str, typing.Any]

    elif request.method == "POST":
      content_type = request.headers.get("Content-Type", "")

      if "application/json" in content_type:
        data = await request.json()
      elif "application/graphql" in content_type:
        body = await request.body()
        text = body.decode()
        data = {"query": text}
      elif "query" in request.query_params:
        data = request.query_params
      else:
        return PlainTextResponse(
            "Unsupported Media Type",
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
        )

    else:
      return PlainTextResponse(
        "Method Not Allowed", status_code=status.HTTP_405_METHOD_NOT_ALLOWED
      )

    try:
      query = data["query"]
      variables = data.get("variables")
      operation_name = data.get("operationName")
    except KeyError:
      return PlainTextResponse(
        "No GraphQL query found in the request",
        status_code=status.HTTP_400_BAD_REQUEST,
      )

    background = BackgroundTasks()
    context = {"request": request, "background": background}

    result = await self.execute(
      query, variables=variables, context=context, operation_name=operation_name
    )
    error_data = (
      [format_error(err) for err in result.errors]
      if result.errors
      else None
    )
    response_data = {"data": result.data}
    if error_data:
      response_data["errors"] = error_data
    status_code = (
      status.HTTP_400_BAD_REQUEST if result.errors else status.HTTP_200_OK
    )

    return JSONResponse(
      response_data, status_code=status_code, background=background
    )
--#

--% /myfastapi/core/main.py
import uvicorn
from fastapi import FastAPI
import graphene
from starlette.graphql import GraphQLApp

from .config import settings
from .routes import api_router
from .schema import Mutation, Query
from .mygql import CustomGraphQLApp

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router, prefix=settings.API_V1_STR)
# app.add_route('/graphql', GraphQLApp(schema=graphene.Schema(mutation=Mutation, query=Query)))
# app.add_route('/graphql', GraphQLApp(schema=graphene.Schema(query=Query)))
# app.add_route('/graphql', CustomGraphQLApp(schema=graphene.Schema(query=Query)))
app.add_route('/graphql', CustomGraphQLApp(schema=graphene.Schema(mutation=Mutation, query=Query)))

@app.get("/")
async def root():
  return {"status": "OK"}

@app.get("/")
async def ping():
  return {"ping": "pong"}

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=__TEMPLATE_SERVER_PORT__)

--#

--% /myfastapi/core/crud.py
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from core.db.base import Base


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
  def __init__(self, model: Type[ModelType]):
    """
    CRUD object with default methods to Create, Read, Update, Delete (CRUD).
    **Parameters**
    * `model`: A SQLAlchemy model class
    * `schema`: A Pydantic model (schema) class
    """
    self.model = model

  def get(self, db: Session, model_id: Any) -> Optional[ModelType]:
    return db.query(self.model).get(model_id)

  def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[ModelType]:
    return db.query(self.model).offset(skip).limit(limit).all()

  def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
    obj_in_data = jsonable_encoder(obj_in)
    db_obj = self.model(**obj_in_data)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

  def update(self, db: Session, *, db_obj: ModelType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
    obj_data = jsonable_encoder(db_obj)
    if isinstance(obj_in, dict):
      update_data = obj_in
    else:
      update_data = obj_in.dict(exclude_unset=True)
    for field in obj_data:
      if field in update_data:
        setattr(db_obj, field, update_data[field])
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

  def remove(self, db: Session, *, model_id: int) -> ModelType:
    obj = db.query(self.model).get(model_id)
    db.delete(obj)
    db.commit()
    return obj

--#

--% /myfastapi/core/init.py
from core.db.init import initialise
from core.db.session import SessionLocal


def init() -> None:
  db = SessionLocal()
  initialise(db)


def main() -> None:
  init()


if __name__ == "__main__":
  main()

--#

--% /myfastapi/core/db/base.py
from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from .session import ScopedSession

@as_declarative()
class Base:
  id: Any
  __name__: str

  query = ScopedSession.query_property()

  # Generate __tablename__ automatically
  @declared_attr
  def __tablename__(self) -> str:
    return self.__name__.lower()

--#

--% /myfastapi/core/db/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
ScopedSession = scoped_session(SessionLocal)
--#

--% /myfastapi/core/db/init.py
from sqlalchemy.orm import Session


def initialise(db: Session) -> None:
  # Write database initialisation queries.
  pass

--#

--% /myfastapi/apps/index.py

--#

--% /myfastapi/apps/common/models.py
from pydantic import BaseModel

class Message(BaseModel):
  message: str

--#
