import { default as dbConnect } from 'D';
import {
	ARRAY,
	BIGINT, 
	BOOLEAN, 
	DATE,
	DECIMAL,
	DOUBLE, 
	ENUM, 
	FLOAT, 
	INTEGER, 
	STRING, 
	TEXT, 
	UUID, 
	UUIDV1, 
	UUIDV4,
} from 'sequelize';

const tableName = '__TABLENAME_LOWER_PLURAL__';

const fieldsMap = __FIELDS__;

const optionsMap = {
__TAB(1)freezeTableName: true,
__TAB(1)schema: process.env.DB_SCHEMA,
__TAB(1)timestamps: false,
};

const __TABLENAME__ = dbConnect.define(
__TAB(1)tableName,
__TAB(1)fieldsMap,
__TAB(1)optionsMap,
);

/*
if (parseInt(process.env.DB_SYNC)===1) {
	console.log(`\n\nDO SYNC'ing database...`);
	dbConnect.sync({force: true});
} else {
	console.log(`\n\nnot synching database...`);
}
*/

export default __TABLENAME__;
