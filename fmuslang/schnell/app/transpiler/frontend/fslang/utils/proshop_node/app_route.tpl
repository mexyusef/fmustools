import express from 'express'
import {
  __TABLENAME_LOWER__Create,
  __TABLENAME_LOWER__List,
  __TABLENAME_LOWER__Detail,
  __TABLENAME_LOWER__Update,
  __TABLENAME_LOWER__Delete,
  // extra exported methods
} from './controller.js'
// extra imports


const router = express.Router()

router.route('/').post(__CREATE_MIDDLEWARE_OR_NONE____TABLENAME_LOWER__Create).get(__LIST_MIDDLEWARE_OR_NONE____TABLENAME_LOWER__List)
router.route('/:id').get(__DETAIL_MIDDLEWARE_OR_NONE____TABLENAME_LOWER__Detail)
router.route('/:id/edit').put(__UPDATE_MIDDLEWARE_OR_NONE____TABLENAME_LOWER__Update)
router.route('/:id/delete').delete(__DELETE_MIDDLEWARE_OR_NONE____TABLENAME_LOWER__Delete)
// samakan dg versi django
router.route('/create').post(__CREATE_MIDDLEWARE_OR_NONE____TABLENAME_LOWER__Create)
router.route('/list/:keyword').get(__LIST_MIDDLEWARE_OR_NONE____TABLENAME_LOWER__List)
router.route('/update/:id').put(__UPDATE_MIDDLEWARE_OR_NONE____TABLENAME_LOWER__Update)
router.route('/delete/:id').delete(__DELETE_MIDDLEWARE_OR_NONE____TABLENAME_LOWER__Delete)

// extra routes

export default router
