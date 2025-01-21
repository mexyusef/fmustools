template_rootapp_import_perapp = """
import { __tablename_caseModule } from './__tablename_lower/__tablename_lower.module';
import { __tablename_caseEntity } from './__tablename_lower/__tablename_lower.model';
"""


def assign_remaining_variables(tables, mkfile_template):
	"""
	import { AttendeeModule } from './attendee/attendee.module';
	import { AttendeeEntity } from './attendee/attendee.model';
	AttendeeEntity,
	AttendeeModule
	"""

	__TEMPLATE_ROOTAPP_IMPORTS_LIST__ = [template_rootapp_import_perapp.replace('__tablename_lower', table.model.lower()).replace('__tablename_case', table.model) for table in tables]
	__TEMPLATE_ROOTAPP_IMPORTS__ = '\n'.join(__TEMPLATE_ROOTAPP_IMPORTS_LIST__)

	__TEMPLATE_ROOTAPP_SERVICEPARAMS_LIST_ = [f'{table.model}Entity' for table in tables]
	__TEMPLATE_ROOTAPP_SERVICEPARAMS__ = ', ' + ', '.join(__TEMPLATE_ROOTAPP_SERVICEPARAMS_LIST_)

	__TEMPLATE_ROOTAPP_RESOLVERPARAMS_LIST_ = [f'{table.model}Module' for table in tables]
	__TEMPLATE_ROOTAPP_RESOLVERPARAMS__ = ', ' + ', '.join(__TEMPLATE_ROOTAPP_RESOLVERPARAMS_LIST_)

	mkfile_template = mkfile_template.replace('__TEMPLATE_ROOTAPP_IMPORTS__', __TEMPLATE_ROOTAPP_IMPORTS__)
	mkfile_template = mkfile_template.replace('__TEMPLATE_ROOTAPP_ENTITYPARAMS__', __TEMPLATE_ROOTAPP_SERVICEPARAMS__)
	mkfile_template = mkfile_template.replace('__TEMPLATE_ROOTAPP_MODULEPARAMS__', __TEMPLATE_ROOTAPP_RESOLVERPARAMS__)
	return mkfile_template
