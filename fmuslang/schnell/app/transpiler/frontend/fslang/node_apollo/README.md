# core/connection/graphql/index.js

import { ApolloServer, gql } from 'apollo-server-express';
import { User as UserModel } from 'DB';
__TEMPLATE_APPS_IMPORTS__

harus menjadi:

import { ApolloServer, gql } from 'apollo-server-express';
import { User as UserModel } from 'DB';
import { todoType, todoResolver } from 'A/todo/todo.graphql';

__TEMPLATE_APPS_TYPEDEFS_LIST__
__TEMPLATE_APPS_RESOLVERS_LIST__

const typeDefs = [queryTypes, userType, __TEMPLATE_APPS_TYPEDEFS_LIST__];
const resolvers = [userResolver, __TEMPLATE_APPS_RESOLVERS_LIST__];
const typeDefs = [queryTypes, userType, todoType];
const resolvers = [userResolver, todoResolver];

# news app
harusnya masuk apps, bukan sejajar: apps dan core.
ternyata gara2 kurang 1 tab
