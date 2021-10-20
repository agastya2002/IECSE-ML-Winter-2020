let express = require("express"),
  multer = require("multer"),
  mongoose = require("mongoose"),
  { v1: uuidv1, v4: uuidv4 } = require("uuid");
router = express.Router();
const User = require("../models/CertModel");

const csv = require("csv-parser");
const fs = require("fs");
const results = [];
const obj = [];

const DIR = "./csv-uploads/";

const storage_new = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, DIR);
  },
  filename: (req, file, cb) => {
    const fileName = file.originalname.toLowerCase().split(" ").join("-");
    cb(null, uuidv4() + "-" + fileName);
  },
});

var upload_new = multer({
  storage: storage_new,
  fileFilter: (req, file, cb) => {
    if (file.mimetype == "text/csv") {
      cb(null, true);
    } else {
      cb(null, false);
      return cb(new Error("Only .csv format allowed!"));
    }
  },
});

router.post("/", upload_new.single("csv"), (req, res, next) => {
  let path = DIR + req.file.filename;
  fs.createReadStream(path)
    .pipe(csv({}))
    .on("data", (data) => results.push(data))
    .on("end", () => res.status(200).send(results));
});

module.exports = router;
