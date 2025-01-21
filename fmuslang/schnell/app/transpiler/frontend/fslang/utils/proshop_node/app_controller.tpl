import asyncHandler from 'express-async-handler'
import __TABLENAME_CASE__ from './model.js'

// extra imports

const __TABLENAME_LOWER__Create = asyncHandler(async (req, res) => {
  // create starts
  const __TABLENAME_LOWER__ = new __TABLENAME_CASE__({
    // extra fields args
    ...req.body
  })
  const created__TABLENAME_CASE__ = await __TABLENAME_LOWER__.save()
  res.status(201).json(created__TABLENAME_CASE__)
  // create ends
})

const __TABLENAME_LOWER__List = asyncHandler(async (req, res) => {
  // list starts
  const __TABLENAME_LOWER__s = await __TABLENAME_CASE__.find({})
    // .populate('user', 'id name')
  res.json(__TABLENAME_LOWER__s)
  // list ends
})

const __TABLENAME_LOWER__Detail = asyncHandler(async (req, res) => {
  // detail starts
  const __TABLENAME_LOWER__ = await __TABLENAME_CASE__.findById(req.params.id)
    // .populate('user', 'name email')
    // .select('-password')
  if (__TABLENAME_LOWER__) {
    res.json(__TABLENAME_LOWER__)
  } else {
    res.status(404)
    throw new Error('__TABLENAME_CASE__ not found')
  }
  // detail ends
})

const __TABLENAME_LOWER__Update = asyncHandler(async (req, res) => {
  // update starts
  const __TABLE_FIELDS__ = req.body
  const __TABLENAME_LOWER__ = await __TABLENAME_CASE__.findById(req.params.id)
  if (__TABLENAME_LOWER__) {
__FIELDS_UPDATE_ASSIGNMENT__
    const updated__TABLENAME_CASE__ = await __TABLENAME_LOWER__.save()
    res.json(updated__TABLENAME_CASE__)
  } else {
    res.status(404)
    throw new Error('__TABLENAME_CASE__ not found')
  }
  // update ends
})

const __TABLENAME_LOWER__Delete = asyncHandler(async (req, res) => {
  // delete starts
  const __TABLENAME_LOWER__ = await __TABLENAME_CASE__.findById(req.params.id)
  if (__TABLENAME_LOWER__) {
    await __TABLENAME_LOWER__.remove()
    res.json({ message: '__TABLENAME_CASE__ removed' })
  } else {
    res.status(404)
    throw new Error('__TABLENAME_CASE__ not found')
  }
  // delete ends
})

// extra controllers

export {
  __TABLENAME_LOWER__Create,
  __TABLENAME_LOWER__List,
  __TABLENAME_LOWER__Detail,
  __TABLENAME_LOWER__Update,
  __TABLENAME_LOWER__Delete,
  // extra exports
}
