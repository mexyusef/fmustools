const mongoose = require("mongoose");
const { ObjectId } = mongoose.Schema;

const __TABLENAME_LOWER__Schema = new mongoose.Schema(
  __FIELDS__,
  { timestamps: true }
);

module.exports = mongoose.model("__TABLENAME__", __TABLENAME_LOWER__Schema);
