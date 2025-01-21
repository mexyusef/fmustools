from app.printutils import indah3


"""
import { Entity, PrimaryGeneratedColumn, Column } from "typeorm";

@Entity()
export class User {
	@PrimaryGeneratedColumn ()
	id: number;

	@Column ()
	firstName: string;

	@Column ()
	lastName: string;

	@Column ()
	age: number;
}
"""
from ..common import TAB

entity_field_map = {
	'string'						: 'string',
	'float'							: 'number',
	'array_of'					: '__SUBTYPE__[]',
}

interface_field_map = {
	'string'						: 'string',
	'float'							: 'number',
	'array_of'					: '__SUBTYPE__[]',
}

interface_ro_template = """export interface __TABLENAME__RO {
  __TABLENAME_LOWER__: __TABLENAME__Entity;
}
"""

interface_ro_list_template = """export interface __TABLENAME__sRO {
  __TABLENAME_LOWER__: __TABLENAME__Entity[];
	__TABLENAME_LOWER__Count: number;
}
"""

create_update_dto_template = """import { IsNotEmpty } from 'class-validator';

export class Create__TABLENAME__Dto {
__CREATE_DTO_FIELDS
}

export class Update__TABLENAME__Dto {
__UPDATE_DTO_FIELDS
}
"""

nextjs_types_template = """export interface __TABLENAME__List {
	__TABLENAME_LOWER__s: __TABLENAME__Type[];
}

export interface __TABLENAME__ {
	__TABLENAME_LOWER__: __TABLENAME__Type;
}

export type __TABLENAME__Type = {
__NEXTJS_TYPE_FIELDS
};
"""

class TypscriptOutput:


	def __init__(self, RootNode):
		self.root = RootNode
		self.tablenames = []

		self.entity_body = []
		self.entity_header = []

		self.interface_body = []
		self.interface_header = []
		self.interface_ro_body = []
		self.interface_ro_list_body = []
		self.create_update_dto = []

		self.nextjs_types = []

		self.nestjs_service = []
		self.nestjs_controller = []


	def generate_entity(self):
		self._entity_header()
		self._entity_body()		
		body_header_separator = '\n' # + '-' * 40 + '\n'
		header = '\n'.join(self.entity_header)
		footer = '\n'.join(self.entity_body)
		return header + body_header_separator + footer


	def generate_interface(self):
		separator_if_ro = '\n\n'
		self._interface_body()
		# self._interface_ro_body()
		body_if = '\n'.join(self.interface_body)
		body_if_ro = '\n'.join(self.interface_ro_body)
		body_if_ro_list = '\n'.join(self.interface_ro_list_body)
		return body_if + separator_if_ro + body_if_ro + separator_if_ro + body_if_ro_list


	def generate_dto(self):
		separator_if_ro = '\n\n'
		self.dto_body()
		body_dto = '\n'.join(self.create_update_dto)
		return body_dto

	
	def generate_nextjs_types(self):
		self.nextjs_types_body()
		body_nextjs = '\n'.join(self.nextjs_types)
		return body_nextjs


	def generate_nestjs_service_controller_process(self):
		from ..config.ts_nest import nestjs_service_template, nestjs_controller_template
		# nestjs_service
		# nestjs_controller
		for index, table in enumerate(self.root.children, 1):
			# table_fields = []
			# for field_no, field in enumerate(table.children, 1):
			# 	table_fields.append(f'{fieldspec}\n' + TAB + column)
			service = nestjs_service_template \
				.replace('__TABLENAME__', table.model) \
				.replace('__TABLENAME_LOWER__', table.model.lower())
			controller = nestjs_controller_template \
				.replace('__TABLENAME__', table.model) \
				.replace('__TABLENAME_LOWER__', table.model.lower())
			self.nestjs_service.append(service)
			self.nestjs_controller.append(controller)


	def generate_nestjs_service_controller(self):
		self.generate_nestjs_service_controller_process()
		separator = '\n\n// ' + '*' * 40 + '\n'
		svc = '\n'.join(self.nestjs_service)
		ctl = '\n'.join(self.nestjs_controller)
		return svc + separator + ctl


	def generate(self):
		separator = '\n\n// ' + '=' * 40
		formatted_result = separator + ' Entity\n' + \
			self.generate_entity() + \
			separator + ' Interface Data+RO\n' + \
			self.generate_interface() + \
			separator + ' DTO\n' + \
			self.generate_dto() + \
			separator + ' Nest Types\n' + \
			self.generate_nextjs_types() + \
			separator + ' Nest Services+Controller\n' + \
			self.generate_nestjs_service_controller()
		
		return formatted_result


	def _entity_header(self):
		self.entity_header.append('\nimport { Column, Entity, PrimaryGeneratedColumn, } from "typeorm";')


	def _entity_body(self):
		for index, table in enumerate(self.root.children, 1):
			table_fields = []
			for field_no, field in enumerate(table.children, 1):
				fieldspec = '@Column (__COLUMN_CONSTRAINT)'
				fieldspec_constraint_object = []
				fieldspec_constraint_nonobject = ''
				column = f"{field.label}: {entity_field_map.get(field.type, field.type)};\n"
				if hasattr(field, 'subtype'):
					column = column.replace('__SUBTYPE__', entity_field_map.get(field.subtype, field.subtype))
					if field.type == 'array_of':
						fieldspec_constraint_nonobject = "'simple-array'"
				if hasattr(field, 'allowNull'):
					fieldspec_constraint_object .append ('nullable: ' + ('true' if field.allowNull else 'false'))
				if hasattr(field, 'defaultValue'):
					nilai_default = field.defaultValue
					if nilai_default == 'empty':
						nilai_default = "''"
					fieldspec_constraint_object .append ('default: ' + nilai_default)

				# bisa specify @Column ('int', { default: 60, nullable: true })
				if hasattr(field, 'primaryKey'):
					fieldspec = '@PrimaryGeneratedColumn (__COLUMN_CONSTRAINT)'

				stringified_fieldspec_constraint_object = ', '.join(fieldspec_constraint_object)
				if stringified_fieldspec_constraint_object:
					stringified_fieldspec_constraint_object = f'{{ {stringified_fieldspec_constraint_object} }}'
				# print('stringified_fieldspec_constraint_object:',stringified_fieldspec_constraint_object)
				stringified_nonobject = ', '.join([fieldspec_constraint_nonobject])
				# print('stringified_nonobject:', stringified_nonobject)
				fieldspec_constraint = stringified_nonobject + stringified_fieldspec_constraint_object
				fieldspec = fieldspec.replace('__COLUMN_CONSTRAINT', fieldspec_constraint)
				table_fields.append(f'{fieldspec}\n' + TAB + column)

			stringified_fields = '\n'.join([TAB+item for item in table_fields])
			nama_table = table.model.lower()
			nama_entity = f"{table.model}Entity"
			temp = f"\n@Entity('{nama_table}')\nexport class {nama_entity} {{\n\n"
			temp += stringified_fields
			temp += '\n}'
			self.entity_body.append(temp)


	def _interface_header(self):
		# self.interface_header.append('\nimport { Column, Entity, PrimaryGeneratedColumn, } from "typeorm";')
		pass


	def _interface_body(self):
		for index, table in enumerate(self.root.children, 1):
			table_fields = []
			for field_no, field in enumerate(table.children, 1):
				nama_kolom = field.label
				jenis_kolom = interface_field_map.get(field.type, field.type)
				if hasattr(field, 'subtype'):
					jenis_kolom = jenis_kolom.replace('__SUBTYPE__', interface_field_map.get(field.subtype, field.subtype))
				if hasattr(field, 'allowNull') and field.allowNull == True:
					nama_kolom += '?'
				table_fields.append(f'{nama_kolom}: {jenis_kolom}')

			stringified_fields = '\n'.join([TAB+item for item in table_fields])
			temp = f"\ninterface {table.model}Data {{\n\n"
			temp += stringified_fields
			temp += '\n\n}'
			self.interface_body.append(temp)
			if_ro = interface_ro_template.replace('__TABLENAME_LOWER__', table.model.lower()).replace('__TABLENAME__', table.model)
			self.interface_ro_body.append(if_ro)
			if_ros = interface_ro_list_template.replace('__TABLENAME_LOWER__', table.model.lower()).replace('__TABLENAME__', table.model)
			self.interface_ro_list_body.append(if_ros)


	def dto_body(self):
		for index, table in enumerate(self.root.children, 1):
			create_fields = []
			update_fields = []
			for field_no, field in enumerate(table.children, 1):
				nama_kolom = field.label
				jenis_kolom = interface_field_map.get(field.type, field.type)
				if hasattr(field, 'subtype'):
					jenis_kolom = jenis_kolom.replace('__SUBTYPE__', interface_field_map.get(field.subtype, field.subtype))
				
				nama_kolom_readonly = f'readonly {nama_kolom}'
				if hasattr(field, 'allowNull') and field.allowNull == True:
					nama_kolom_readonly = '@IsNotEmpty()\n' + TAB + nama_kolom_readonly
				create_fields.append(f'{nama_kolom_readonly}: {jenis_kolom};')
				update_fields.append(f'{nama_kolom_readonly}: {jenis_kolom};')

			stringified_create_fields = '\n'.join([TAB+item for item in create_fields])
			stringified_update_fields = '\n'.join([TAB+item for item in update_fields])

			create_update_dto = '\n' + create_update_dto_template \
				.replace('__TABLENAME__', table.model) \
				.replace('__CREATE_DTO_FIELDS', stringified_create_fields) \
				.replace('__UPDATE_DTO_FIELDS', stringified_update_fields)

			self.create_update_dto.append(create_update_dto)


	def nextjs_types_body(self):
		for index, table in enumerate(self.root.children, 1):
			nextjs_fields = []
			for field_no, field in enumerate(table.children, 1):
				nama_kolom = field.label
				jenis_kolom = interface_field_map.get(field.type, field.type)
				if hasattr(field, 'subtype'):
					jenis_kolom = jenis_kolom.replace('__SUBTYPE__', interface_field_map.get(field.subtype, field.subtype))
				nextjs_fields.append(f'{nama_kolom}: {jenis_kolom};')

			stringified_nextjs_fields = '\n'.join([TAB+item for item in nextjs_fields])

			nextjs_types_body = '\n' + nextjs_types_template \
				.replace('__TABLENAME__', table.model) \
				.replace('__TABLENAME_LOWER__', table.model.lower()) \
				.replace('__NEXTJS_TYPE_FIELDS', stringified_nextjs_fields)

			self.nextjs_types.append(nextjs_types_body)


def bantu_ts(RootNode):
	indah3('bantu_ts', warna='white')
	grpc = TypscriptOutput(RootNode)
	return grpc.generate()
