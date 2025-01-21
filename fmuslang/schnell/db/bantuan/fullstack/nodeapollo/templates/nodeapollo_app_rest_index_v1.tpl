const express = require('express');
const controller = require('./__TEMPLATE_TABLENAME_LOWER__.controller');

const router = express.Router();

router.get('/', controller.index);
router.get('/:id', controller.detail);
router.post('/', controller.create);
router.put('/:id', controller.update);
router.delete('/:id', controller.destroy);

module.exports = router;
