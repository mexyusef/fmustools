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
