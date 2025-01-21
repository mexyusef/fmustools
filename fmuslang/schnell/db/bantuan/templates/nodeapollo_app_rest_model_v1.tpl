// const { USER_ROLES } = require('../../config/buckets');

const Fields = (DataTypes) => ({
  id: {
    type: DataTypes.INTEGER,
    autoIncrement: false,
    primaryKey: true,
    allowNull: false,
    unique: true,
  },
  name: DataTypes.STRING,
  // username: DataTypes.STRING,
  // password: DataTypes.STRING,
  // role: {
  //   type: DataTypes.STRING,
  // },
  email: DataTypes.STRING,
  mobile: DataTypes.STRING,
  suspend_status: {
    type: DataTypes.BOOLEAN,
    defaultValue: false,
  },
  updated_by: DataTypes.INTEGER,
  created_by: DataTypes.INTEGER,
  deleted_by: DataTypes.INTEGER,
});

module.exports = (sequelize, DataTypes) => {
  const __TEMPLATE_TABLENAME_CASE__ = sequelize.define(
    '__TEMPLATE_TABLENAME_CASE__', 
    Object.assign(Fields(DataTypes)), 
    {
      tableName: '__TEMPLATE_TABLENAME_LOWER__s',
      timestamps: true,
      underscored: true,
      paranoid: true,
      createdAt: 'created_on',
      updatedAt: 'updated_on',
      deletedAt: 'deleted_on',
    }
  );

  // __TEMPLATE_TABLENAME_CASE__.associate = (db) => {};

  __TEMPLATE_TABLENAME_CASE__.get__TEMPLATE_TABLENAME_CASE__ = (db, Id) =>
    db.__TEMPLATE_TABLENAME_CASE__.findOne({
      // attributes: ['name', 'email'],
      where: { id: Id, },
      order: [['id', 'asc']],
      limit: 1,
    });

  return __TEMPLATE_TABLENAME_CASE__;
};
