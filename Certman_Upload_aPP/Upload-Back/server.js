require("dotenv").config();
const express = require("express");
const multer = require("multer");
const cookieParser = require("cookie-parser");
const cert = require("./routes/upload.js");
const csv = require("./routes/csv-upload.js");

const InitiateMongoServer = require("./config/db");

const cors = require("cors");

InitiateMongoServer();
const app = express();

app.use(
  cors({
    credentials: true,
    origin: "http://localhost:3000",
  })
);

app.use((req, res, next) => {
  res.setHeader(
    "Access-Control-Allow-Methods",
    "OPTIONS, GET, POST, PUT, PATCH, DELETE"
  );
  res.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization");
  next();
});

app.use(cookieParser());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use("/uploads", express.static("uploads"));

const PORT = process.env.PORT || 5000;

app.get("/", (req, res) => {
  res.json("helllo");
});

app.use("/api", cert);
app.use("/csv-uploads", csv);

app.listen(PORT, (req, res) => {
  console.log(`Server Started at PORT ${PORT}`);
});
