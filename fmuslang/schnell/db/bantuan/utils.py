from anytree.search import find, findall


def get_tables_from_rootnode(RootNode):
  """
  AnyNode(dbname='MyDummyGRPC', label='root', output='', outputs=[], type='root')
  └─ AnyNode(model='Book', name='table', type='table')
    ├─ AnyNode(hasConstraint=True, label='isbn', primaryKey=True, type='string')
    ├─ AnyNode(hasConstraint=False, label='title', type='string')
    ├─ AnyNode(hasConstraint=False, label='publisher', type='string')
    ├─ AnyNode(hasConstraint=False, label='authors', subtype='string', type='array_of')
    └─ AnyNode(hasConstraint=False, label='publishedDate', type='string')
  """
  node_tables = lambda node: hasattr(node, 'name') and node.name == 'table' and node.type == 'table'
  tables = findall(RootNode, node_tables)
  return tables


def process_each_table(tables, callback):
  for index, tbl in enumerate(tables, 1):
    callback(tbl, index)


def process_each_table_from_rootnode(RootNode, callback):
  process_each_table(get_tables_from_rootnode(RootNode), callback)

