import mongoose from 'mongoose'
// extra imports
// extra schemas

const __TABLENAME_LOWER__Schema = mongoose.Schema(  
  __TABLE_FIELDS__,
  {
    timestamps: true,
  }
)

// extra methods

const __TABLENAME_CASE__ = mongoose.model('__TABLENAME_CASE__', __TABLENAME_LOWER__Schema)
export default __TABLENAME_CASE__
