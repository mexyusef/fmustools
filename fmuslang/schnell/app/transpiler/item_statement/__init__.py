from app.transpiler.item_expression import (
  expression_item
)

from .if_statement import if_statement
from .single_statement import single_statement
from .for_statement import for_statement
from .switch_statement import switch_statement
from .while_statement import while_statement
from .condition_body import condition_body
from .enum_declaration import enum_declaration

statement_item = f"""
statement_item: if_statement
  | for_statement
  | switch_statement
  | while_statement
  | single_statement
  | expression_item
  | enum_declaration

{if_statement}

{for_statement}

{switch_statement}

{while_statement}

{single_statement}

{expression_item}

{enum_declaration}

{condition_body}
"""
