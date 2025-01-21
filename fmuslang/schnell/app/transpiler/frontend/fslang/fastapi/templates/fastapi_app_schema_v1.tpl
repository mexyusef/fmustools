import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from .models import __TEMPLATE_TABLENAME_CASE__
from core.db.session import SessionLocal as db_session


db = db_session() # .session_factory()


class __TEMPLATE_TABLENAME_CASE__Model(SQLAlchemyObjectType):
  class Meta:
    model = __TEMPLATE_TABLENAME_CASE__


class Hello__TEMPLATE_TABLENAME_CASE__(graphene.ObjectType):
  __TEMPLATE_TABLENAME_LOWER___hello    = graphene.String(name=graphene.String(default_value="World"))
  @staticmethod
  def resolve___TEMPLATE_TABLENAME_LOWER___hello(parent, info, name):
    return f"Hello {name}!"


class List__TEMPLATE_TABLENAME_CASE__(graphene.ObjectType):
  __TEMPLATE_TABLENAME_LOWER___list     = graphene.List(__TEMPLATE_TABLENAME_CASE__Model)
  @staticmethod
  def resolve___TEMPLATE_TABLENAME_LOWER___list(parent, info):
    query = __TEMPLATE_TABLENAME_CASE__Model.get_query(info)
    return query.all()


class Detail__TEMPLATE_TABLENAME_CASE__(graphene.ObjectType):
  # __TEMPLATE_TABLENAME_LOWER___detail   = graphene.Field(__TEMPLATE_TABLENAME_CASE__Model, id=graphene.NonNull(graphene.Int))
  __TEMPLATE_TABLENAME_LOWER___detail   = graphene.Field(__TEMPLATE_TABLENAME_CASE__Model, id=graphene.Int(required=True))
  @staticmethod
  def resolve___TEMPLATE_TABLENAME_LOWER___detail(parent, info, id):
    # return __TEMPLATE_TABLENAME_CASE__.find_or_fail(id)
    return db.query(__TEMPLATE_TABLENAME_CASE__).filter(__TEMPLATE_TABLENAME_CASE__.id == id).first()


class Create__TEMPLATE_TABLENAME_CASE__(graphene.Mutation):
  class Arguments:
__TEMPLATE2_CREATE_ARGUMENTS__
    # name = graphene.String()
    # price = graphene.Float()

  result = graphene.Boolean()

  @staticmethod
  def mutate(parent, info__TEMPLATE_COMMA_MUTATE_FIELDS__):
    """
    __TEMPLATE_COMMA_MUTATE_FIELDS__
    , name, price

    __TEMPLATE_MUTATE_ASSIGNS__
    name=name, price=price
    """
    db___TEMPLATE_TABLENAME_LOWER__ = __TEMPLATE_TABLENAME_CASE__(__TEMPLATE_MUTATE_ASSIGNS__)
    db.add(db___TEMPLATE_TABLENAME_LOWER__)
    db.commit()
    db.refresh(db___TEMPLATE_TABLENAME_LOWER__)
    return Create__TEMPLATE_TABLENAME_CASE__(result=True)


class Update__TEMPLATE_TABLENAME_CASE__(graphene.Mutation):
  class Arguments:
    # data = __TEMPLATE_TABLENAME_CASE__UpdateInput()
    # id = graphene.ID()
    # id = graphene.Int()
__TEMPLATE2_CREATE_ARGUMENTS__
    # name = graphene.String()
    # price = graphene.Float()

  result = graphene.Field(__TEMPLATE_TABLENAME_CASE__Model)

  @staticmethod
  def mutate(parent, info, __TEMPLATE_UPDATE_NONE__):
    """
    __TEMPLATE_UPDATE_NONE__
    , name=None, price=None

    __TEMPLATE_UPDATE_OR__
    name or price

    __TEMPLATE_IF3_ASSIGN4__
      if name:
        db___TEMPLATE_TABLENAME_LOWER__.name = name
      if price:
        db___TEMPLATE_TABLENAME_LOWER__.price = price
    """		
    db___TEMPLATE_TABLENAME_LOWER__ = db.get(__TEMPLATE_TABLENAME_CASE__, ident=id)
    if db___TEMPLATE_TABLENAME_LOWER__ and (__TEMPLATE_UPDATE_OR__):
__TEMPLATE_IF3_ASSIGN4__

      db.add(db___TEMPLATE_TABLENAME_LOWER__)
      db.commit()
      db.refresh(db___TEMPLATE_TABLENAME_LOWER__)
      return Update__TEMPLATE_TABLENAME_CASE__(result=db___TEMPLATE_TABLENAME_LOWER__)

    return Update__TEMPLATE_TABLENAME_CASE__(result=None)


class Delete__TEMPLATE_TABLENAME_CASE__(graphene.Mutation):
  class Arguments:
    id = graphene.ID()

  result = graphene.Boolean()

  def mutate(self, info, id):
    db___TEMPLATE_TABLENAME_LOWER__ = db.get(__TEMPLATE_TABLENAME_CASE__, ident=id)
    if db___TEMPLATE_TABLENAME_LOWER__:
      db.delete(db___TEMPLATE_TABLENAME_LOWER__)
      db.commit()
      return Delete__TEMPLATE_TABLENAME_CASE__(result=True)
    
    return Delete__TEMPLATE_TABLENAME_CASE__(result=False)
