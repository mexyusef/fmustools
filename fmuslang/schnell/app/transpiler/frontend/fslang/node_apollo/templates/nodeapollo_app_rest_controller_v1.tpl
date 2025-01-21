const service = require('./__TEMPLATE_TABLENAME_LOWER__.service');
const db = require('DB');

const messagesMap = {
  201: 'Your account created successfully.',
  409: 'Duplicate',
};
const SUCCESS = 200;

const { __TEMPLATE_TABLENAME_CASE__ } = db;

async function create(req, res, next) {
  try {
    const status = await service.signup(req.body);

    return res.json({ message: messagesMap[status.code], id: status.id });
  } catch (err) {
    return next(err);
  }
}

async function index(req, res, next) {
  try {
    const limit = 100;
    const offset = 0;

    const __TEMPLATE_TABLENAME_LOWER__s = await __TEMPLATE_TABLENAME_CASE__.findAll({
      limit,
      offset,
    });

    return res.json(__TEMPLATE_TABLENAME_LOWER__s);
  } catch (err) {
    return next(err);
  }
}

async function detail(req, res, next) {
  try {
    const __TEMPLATE_TABLENAME_LOWER__ = await __TEMPLATE_TABLENAME_CASE__.findOne({
      // attributes: ['id', 'mobile', 'name', 'email'],
      where: { id: req.params.id },
      raw: true,
    });
    return res.json(__TEMPLATE_TABLENAME_LOWER__);
  } catch (err) {
    return next(err);
  }
}

async function update(req, res, next) {  
  try {
    await __TEMPLATE_TABLENAME_CASE__.update(
      {
        ...req.body,
      },
      {
        where: {
          id: req.params.id,
        },
      },
    );
    return res.sendStatus(SUCCESS);
  } catch (err) {
    return next(err);
  }
}

async function destroy(req, res, next) {  
  try {
    await __TEMPLATE_TABLENAME_CASE__.destroy(
      {
        where: {
          id: req.params.id,
        },
      },
    );
    return res.sendStatus(SUCCESS);
  } catch (err) {
    return next(err);
  }
}

module.exports = {
  create,
  index,
  detail,
  update,
  destroy,
};
