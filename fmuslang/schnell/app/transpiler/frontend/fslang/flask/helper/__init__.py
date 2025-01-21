from app.usutils import tab

def assign_remaining_variables(tables, mkfile_template):
	"""
	utk remaining variables di mkfile yg perlu diassign.
	
	__TEMPLATE2_BLUEPRINTS_IMPORTS
	from project.apps import user
	__TEMPLATE2_BLUEPRINTS_REGISTER
	self.register_blueprint(user.blueprint)
	"""

	appimports = [tab(2) + f"from project.apps import {table.model.lower()}" for table in tables]
	__TEMPLATE2_BLUEPRINTS_IMPORTS = '\n'.join(appimports)
	apptypedefs = [tab(2) + f"self.register_blueprint({table.model.lower()}.blueprint)" for table in tables]
	__TEMPLATE2_BLUEPRINTS_REGISTER = '\n'.join(apptypedefs)
	# appresolvers = [f"{table.model.lower()}Resolver" for table in tables]
	# __TEMPLATE_APPS_RESOLVERS_LIST__ = ', '.join(appresolvers)

	mkfile_template = mkfile_template.replace('__TEMPLATE2_BLUEPRINTS_IMPORTS', __TEMPLATE2_BLUEPRINTS_IMPORTS)
	mkfile_template = mkfile_template.replace('__TEMPLATE2_BLUEPRINTS_REGISTER', __TEMPLATE2_BLUEPRINTS_REGISTER)
	# mkfile_template = mkfile_template.replace('__TEMPLATE_APPS_RESOLVERS_LIST__', __TEMPLATE_APPS_RESOLVERS_LIST__)
	return mkfile_template
