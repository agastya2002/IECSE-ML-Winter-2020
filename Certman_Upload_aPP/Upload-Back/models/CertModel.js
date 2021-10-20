const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const userSchema = new Schema(
  {
    _id: mongoose.Schema.Types.ObjectId,
    profileImg: {
      type: String,
    },
    coordinates: [Number]
  },

  {
    collection: "users",
  }
);

module.exports = mongoose.model("User", userSchema);
