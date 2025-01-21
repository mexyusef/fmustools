import graphene
from graphene import Argument
from graphene_django.types import DjangoObjectType

from .models import __TEMPLATE_TABLENAME_CASE__


class __TEMPLATE_TABLENAME_CASE__Type(DjangoObjectType):
  class Meta:
    model = __TEMPLATE_TABLENAME_CASE__

class Query(graphene.ObjectType):
  __TEMPLATE_TABLENAME_LOWER___list = graphene.List(__TEMPLATE_TABLENAME_CASE__Type)
  __TEMPLATE_TABLENAME_LOWER___detail = graphene.Field(__TEMPLATE_TABLENAME_CASE__Type, id=graphene.ID())  
  
  def resolve___TEMPLATE_TABLENAME_LOWER___list(self, info, **kwargs):
    return __TEMPLATE_TABLENAME_CASE__.objects.all()

  def resolve___TEMPLATE_TABLENAME_LOWER___detail(self, info, id):
    return __TEMPLATE_TABLENAME_CASE__.objects.get(pk=id)

class __TEMPLATE_TABLENAME_CASE__Create(graphene.Mutation):
  class Arguments:
__TEMPLATE_TABLENAME_GRAPHQLFIELDS__

  __TEMPLATE_TABLENAME_LOWER__ = graphene.Field(__TEMPLATE_TABLENAME_CASE__Type)

  def mutate(self, info, __TEMPLATE_TABLENAME_SIMPLEPARAMFIELDS__):
    __TEMPLATE_TABLENAME_LOWER__ = __TEMPLATE_TABLENAME_CASE__.objects.create(
      __TEMPLATE_TABLENAME_ASSIGNPARAMFIELDS__
    )
    return __TEMPLATE_TABLENAME_CASE__Create(
      __TEMPLATE_TABLENAME_LOWER__ = __TEMPLATE_TABLENAME_LOWER__
    )

class __TEMPLATE_TABLENAME_CASE__Update(graphene.Mutation):
  class Arguments:
    id            = graphene.ID()
__TEMPLATE_TABLENAME_GRAPHQLFIELDS__

  __TEMPLATE_TABLENAME_LOWER__ = graphene.Field(__TEMPLATE_TABLENAME_CASE__Type)

  def mutate(self, info, id, __TEMPLATE_TABLENAME_ASNONEPARAMFIELDS__):
    __TEMPLATE_TABLENAME_LOWER__ = __TEMPLATE_TABLENAME_CASE__.objects.get(pk=id)
    if __TEMPLATE_TABLENAME_LOWER__:
__TEMPLATE_TABLENAME_VALUEASSIGNMENTS__
      __TEMPLATE_TABLENAME_LOWER__.save()

    return __TEMPLATE_TABLENAME_CASE__Update(__TEMPLATE_TABLENAME_LOWER__ = __TEMPLATE_TABLENAME_LOWER__)

class __TEMPLATE_TABLENAME_CASE__Delete(graphene.Mutation):
  class Arguments:
    id            = graphene.ID()

  __TEMPLATE_TABLENAME_LOWER__ = graphene.Field(__TEMPLATE_TABLENAME_CASE__Type)
  
  def mutate(self, info, id):
    __TEMPLATE_TABLENAME_LOWER__ = __TEMPLATE_TABLENAME_CASE__.objects.get(pk=id)
    if __TEMPLATE_TABLENAME_LOWER__:
      __TEMPLATE_TABLENAME_LOWER__.delete()
    return __TEMPLATE_TABLENAME_CASE__Delete(__TEMPLATE_TABLENAME_LOWER__ = __TEMPLATE_TABLENAME_LOWER__)

class Mutation(graphene.ObjectType):
  __TEMPLATE_TABLENAME_LOWER___create = __TEMPLATE_TABLENAME_CASE__Create.Field()
  __TEMPLATE_TABLENAME_LOWER___update = __TEMPLATE_TABLENAME_CASE__Update.Field()
  __TEMPLATE_TABLENAME_LOWER___delete = __TEMPLATE_TABLENAME_CASE__Delete.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
