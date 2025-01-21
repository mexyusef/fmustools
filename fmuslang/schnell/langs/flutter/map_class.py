map_stateful = """
import 'package:flutter/material.dart';

class ___TEMPLATE_CLASSNAMEState extends State<__TEMPLATE_CLASSNAME> {
	@override
	Widget build(BuildContext context) {}
}

class __TEMPLATE_CLASSNAME extends StatefulWidget {
	__TEMPLATE_CLASSNAME({Key key, this.title}) : super(key: key);
	final String title;

	@override
	___TEMPLATE_CLASSNAMEState createState() => ___TEMPLATE_CLASSNAMEState();
}
"""

map_stateless = """
import 'package:flutter/material.dart';

class __TEMPLATE_CLASSNAME extends StatelessWidget {
	@override
	Widget build(BuildContext context) {
		return Scaffold();
	}
}
"""
