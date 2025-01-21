from ..common import tab

__JS_APOLLO_TEMPLATE__ = """
import { ApolloServer } from 'apollo-server-express';
import { gql } from 'apollo-server-express';

__PER_TABLE_TYPE__

const typeDefs = [
  __ALL_TABLE_TYPES__
];

__PER_TABLE_RESOLVER__

const resolvers = [
  __ALL_TABLE_RESOLVERS__
];

const server = new ApolloServer({
  typeDefs,
  resolvers,
  subscriptions: {
    onConnect: () => console.log('Connected to websocket....../n'),
  },
  tracing: true,
});

const app = express();
server.applyMiddleware({ app });
const httpServer = http.createServer(app);
server.installSubscriptionHandlers(httpServer);
"""

/*
__TABLENAME_CASE__
__TABLENAME_LOWER__
__NON_ID_PARAMFIELDS__
__TABLE_FIELDS__
*/
__PER_TABLE_TYPE_TEMPLATE = """
const __TABLENAME_LOWER__Type = gql`
  type __TABLENAME_CASE__ {
__TABLE_FIELDS__
  }

  extend type Query {
    __TABLENAME_LOWER__(id: ID!): __TABLENAME_CASE__
    __TABLENAME_LOWER__s: [__TABLENAME_CASE__!]
  }

  type __TABLENAME_CASE__DeleteResult {
    count: Int
    __TABLENAME_CASE__s: [__TABLENAME_CASE__]
  }

  extend type Mutation {
    create__TABLENAME_CASE__(__NON_ID_PARAMFIELDS__): __TABLENAME_CASE__
    update__TABLENAME_CASE__(id: Int!, __NON_ID_PARAMFIELDS__): __TABLENAME_CASE__
    delete__TABLENAME_CASE__(id: Int!): __TABLENAME_CASE__DeleteResult    
  }
`;
"""

entity_field_map = {

}

def generate_gs_apollo(tables):
  all_tables_for_typedefs = []

  for index, table in enumerate(tables, 1):
    table_fields = []
    table_fields_non_id = []
    for field_no, field in enumerate(table.children, 1):
      '''
      type __TABLENAME_CASE__ {
        id: String
        name: String
        email: String
        active: Boolean
        posts: [Post]
      }
      '''
      column = f"{field.label}: {entity_field_map.get(field.type, field.type)};\n"
      table_fields.append(column)
      if field.label != 'id':
        table_fields_non_id.append(column)

    stringified_fields = '\n'.join([tab(2)+item for item in table_fields])
    stringified_fields_non_id = ', '.join(table_fields_non_id)
    nama_table_case = table.model
    nama_table_lower = table.model.lower()
    temp = __PER_TABLE_TYPE_TEMPLATE
    temp = temp.replace('__TABLENAME_CASE__', nama_table_case)
    temp = temp.replace('__TABLENAME_LOWER__', nama_table_lower)
    temp = temp.replace('__NON_ID_PARAMFIELDS__', stringified_fields)
    temp = temp.replace('__TABLE_FIELDS__', stringified_fields_non_id)
    all_tables_for_typedefs.append(temp)

  __PER_TABLE_TYPE__ = '\n\n'.join(all_tables_for_typedefs)
  table_types = [f"{table.model.lower()}Type" for table in tables]
  __ALL_TABLE_TYPES__ = ', '.join(table_types)
  table_resolvers = [f"{table.model.lower()}Resolvers" for table in tables]
  __ALL_TABLE_RESOLVERS__ = ', '.join(table_resolvers)


