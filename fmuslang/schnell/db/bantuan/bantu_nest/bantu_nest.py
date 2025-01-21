from app.printutils import (
	indah3
)

"""
import {
  Field,
  ID,
  InputType,
  Int,
  ObjectType,
} from '@nestjs/graphql';

@ObjectType()
export class Book {
  @Field(() => ID)
  id: number;

  @Field()
  title: string;

  @Field()
  isbn: string;

  @Field(() => Author)
  author: Author | number;
}

@ObjectType()
export class Author {
  @Field(() => ID)
  id: string;

  @Field()
  name: string;

  @Field(() => [Book])
  author: Book[];
}

@InputType()
export class CreateBookInput {
  @Field(() => ID)
  id: number;

  @Field()
  title: string;

  @Field()
  isbn: string;

  @Field(() => Int)
  author: number;
}

@InputType()
export type FindBookInput {
  @Field(() => Int)
  id: number;
}
"""
from ..common import (
  TAB,
  nestjs_graphql_imports,
)

field_map = {
	'string'						: 'string',
	'float'							: 'number',
}

class NestOutput:
	def __init__(self, RootNode):
		# self.output = ''
		self.root = RootNode
		# self.service = RootNode.label
		self.tables = []
		self.tablenames = []    
		self.service = []
		self._tables()
		self._service()


	def generate(self):
		header = '\n'.join(self.service)
		footer = '\n'.join(self.tables)
		return header + '\n' + footer


	def _service(self):
		self.service.append(f'\n{nestjs_graphql_imports}')


	def _tables(self):
		for index, table in enumerate(self.root.children, 1):
			table_fields = []
			for field_no, field in enumerate(table.children, 1):
				tipe_data = field_map.get(field.type, field.type)
				fieldspec = '@Field ()'
				if field.type == 'django_many_to_many' and hasattr(field, 'relTo'):
					'''
					books <=> authors
					'''
					tipe_data = f"{field.relTo}[]"
					fieldspec = f'@Field (() => [{field.relTo}])'
				elif field.type == 'django_foreign_key' and hasattr(field, 'relTo'):
					'''
					AnyNode(foreignKey=True, 
					foreignKeyOnDelete='models.SET_NULL', 
					hasConstraint=False, 
					label='authors', 
					relTo='Author', 
					type='django_foreign_key')
					'''
					tipe_data = f"{field.relTo} | number" # user_id dll
					fieldspec = f'@Field (() => {field.relTo})'

				column = f"{field.label}: {tipe_data};\n"
				if hasattr(field, 'primaryKey'):
					fieldspec = '@Field (() => ID)'				

				table_fields.append(f'{fieldspec}\n' + TAB + column)

			stringified_fields = '\n'.join([TAB+item for item in table_fields])
			temp = f"\n@ObjectType()\nexport class {table.model} {{\n\n"
			temp += stringified_fields
			temp += '\n}'
			self.tables.append(temp)


def bantu_nest(RootNode):
	indah3('bantu_nest', warna='white')
	grpc = NestOutput(RootNode)
	return grpc.generate()
