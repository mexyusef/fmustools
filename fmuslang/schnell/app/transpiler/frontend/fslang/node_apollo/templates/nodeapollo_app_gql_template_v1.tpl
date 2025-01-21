import { ApolloServer, gql } from 'apollo-server-express';
import { __TEMPLATE_TABLENAME_CASE__ as __TEMPLATE_TABLENAME_CASE__Model } from 'DB';


const __TEMPLATE_TABLENAME_LOWER__Type = gql`
	type __TEMPLATE_TABLENAME_CASE__ {
		id: ID
		name: String
		email: String
    mobile: String
    suspend_status: Boolean
    updated_by: Int
    created_by: Int
    deleted_by: Int
	}

	extend type Query {
		hello__TEMPLATE_TABLENAME_CASE__: String!
		__TEMPLATE_TABLENAME_LOWER__s: [__TEMPLATE_TABLENAME_CASE__]
		__TEMPLATE_TABLENAME_LOWER__(id: ID!): __TEMPLATE_TABLENAME_CASE__
	}

	input __TEMPLATE_TABLENAME_CASE__CreateInput {
    id: ID!
		name: String!
		email: String!
    mobile: String
    suspend_status: Boolean
    updated_by: Int
    created_by: Int
    deleted_by: Int
	}

	input __TEMPLATE_TABLENAME_CASE__UpdateInput {
		name: String
		email: String
    mobile: String
    suspend_status: Boolean
    updated_by: Int
    created_by: Int
    deleted_by: Int
	}

  type __TEMPLATE_TABLENAME_CASE__DeleteResult {
    affectedRows: Int
  }

  type __TEMPLATE_TABLENAME_CASE__UpdateResult {
    affectedRows: Int
    __TEMPLATE_TABLENAME_LOWER__: __TEMPLATE_TABLENAME_CASE__
  }
	
	extend type Mutation {		
		__TEMPLATE_TABLENAME_LOWER___create(data: __TEMPLATE_TABLENAME_CASE__CreateInput!): __TEMPLATE_TABLENAME_CASE__
		__TEMPLATE_TABLENAME_LOWER___update(id: ID!, data: __TEMPLATE_TABLENAME_CASE__UpdateInput!): __TEMPLATE_TABLENAME_CASE__UpdateResult
		__TEMPLATE_TABLENAME_LOWER___delete(id: ID!): __TEMPLATE_TABLENAME_CASE__DeleteResult
	}
`;


const __TEMPLATE_TABLENAME_LOWER__Resolver = {

	Query: {
		hello__TEMPLATE_TABLENAME_CASE__: () => 'hi __TEMPLATE_TABLENAME_LOWER__!',

		__TEMPLATE_TABLENAME_LOWER__: (root, {id}) => {
      return __TEMPLATE_TABLENAME_LOWER__Service.get__TEMPLATE_TABLENAME_CASE__Detail(id);
		},
		__TEMPLATE_TABLENAME_LOWER__s: async (root, args) => {
      // const __TEMPLATE_TABLENAME_LOWER__s = await __TEMPLATE_TABLENAME_LOWER__Service.get__TEMPLATE_TABLENAME_CASE__List();
      const __TEMPLATE_TABLENAME_LOWER__s = await __TEMPLATE_TABLENAME_CASE__Model.findAll();
      return __TEMPLATE_TABLENAME_LOWER__s || [];
    },
	},

	Mutation: {
		__TEMPLATE_TABLENAME_LOWER___create: async (_, {data}) => {
			const __TEMPLATE_TABLENAME_LOWER__ = await __TEMPLATE_TABLENAME_CASE__Model.create(data);
      return __TEMPLATE_TABLENAME_LOWER__;
		},

		__TEMPLATE_TABLENAME_LOWER___update: async (_, {id, data}) => {
			const result = await __TEMPLATE_TABLENAME_CASE__Model.update(
        data,
        {
          // https://stackoverflow.com/questions/38524938/sequelize-update-record-and-return-result
          returning: true,
          where: { id } 
        }
      );
      // console.log(`kembalian __TEMPLATE_TABLENAME_LOWER___update:`, JSON.stringify(result));
      return {
        affectedRows: result[0],
        __TEMPLATE_TABLENAME_LOWER__: result[1][0]
      };
		},

		__TEMPLATE_TABLENAME_LOWER___delete: async (_, {id}) => {
			const deleteResult = await __TEMPLATE_TABLENAME_CASE__Model.destroy({
        where: { id }
      });
      // https://stackoverflow.com/questions/43735418/sequelize-how-to-return-destroyed-row
      // https://github.com/sequelize/sequelize/issues/4124
      // console.log(`hasil hapus:`, deleteResult, typeof(deleteResult));
      return deleteResult;
		},
	}

}


module.exports = {
  __TEMPLATE_TABLENAME_LOWER__Type,
  __TEMPLATE_TABLENAME_LOWER__Resolver,
}
