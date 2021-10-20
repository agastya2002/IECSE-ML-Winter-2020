let express = require("express"),
  multer = require("multer"),
  mongoose = require("mongoose"),
  { v1: uuidv1, v4: uuidv4 } = require("uuid");
router = express.Router();
const User = require("../models/CertModel");

const DIR = "./uploads/";

const csv = require("csv-parser");
const fs = require("fs");
const results = [];
const obj = [];

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, DIR);
  },
  filename: (req, file, cb) => {
    const fileName = file.originalname.toLowerCase().split(" ").join("-");
    cb(null, uuidv4() + "-" + fileName);
  },
});

var upload = multer({
  storage: storage,
  fileFilter: (req, file, cb) => {
    if (
      file.mimetype == "image/png" ||
      file.mimetype == "image/jpg" ||
      file.mimetype == "image/jpeg"
    ) {
      cb(null, true);
    } else {
      cb(null, false);
      return cb(new Error("Only .png, .jpg and .jpeg format allowed!"));
    }
  },
});

router.post("/user-profile", upload.single("profileImg"), (req, res, next) => {
  const url = req.protocol + "://" + req.get("host");
  const user = new User({
    _id: new mongoose.Types.ObjectId(),
    name: req.body.name,
    profileImg: url + "/uploads/" + req.file.filename,
  });
  user
    .save()
    .then((result) => {
      res.send(result);
    })
    .catch((err) => {
      console.log(err),
        res.status(500).json({
          error: err,
        });
    });
});

router.get("/", (req, res, next) => {
  User.find().then((data) => {
    res.status(200).send(data);
  });
});

//FOR SINGLE IMAGE
router.get("/:id", async (req, res) => {
  try {
    const image = await User.findById(req.params.id);
    res.status(200).json(image);
  } catch (err) {
    res.status(500).json(err);
  }
});



module.exports = router;
