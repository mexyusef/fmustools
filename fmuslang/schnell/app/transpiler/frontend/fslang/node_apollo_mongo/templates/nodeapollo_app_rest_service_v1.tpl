const { __TEMPLATE_TABLENAME_CASE__ } = require('DB');

const checkDuplicate = (email) =>
  __TEMPLATE_TABLENAME_CASE__.findOne({
    attributes: ['id'],
    where: { email },
    raw: true,
  }
);

async function signup(body) {
  try {
    const { id = null, name, email: e, acting__TEMPLATE_TABLENAME_CASE__ = null, mobile } = body;

    const email = e && e.trim();
    // - Todo: Email Validation
    const found = await checkDuplicate(email);

    if (found) {
      return {
        code: 409,
        id: found.id,
        message: 'Duplicate',
      };
    }

    const __TEMPLATE_TABLENAME_LOWER__ = {
      id,
      name,
      email,
      created_by: acting__TEMPLATE_TABLENAME_CASE__,
      mobile,
    };

    await __TEMPLATE_TABLENAME_CASE__.upsert(__TEMPLATE_TABLENAME_LOWER__);

    return { code: 201, id: __TEMPLATE_TABLENAME_LOWER__.id };
  } catch (err) {
    return Promise.reject(err);
  }
}

module.exports = {
  signup,
};
