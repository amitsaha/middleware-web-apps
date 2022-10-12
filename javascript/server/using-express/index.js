import express from "express";

const app = express();
const port = 3000;

const authHeaderCheck = function (req, res, next) {
  if (req.get("X-API-Key") === undefined) {
    res.status(401).send("X-API-Key header not specified");
  } else {
    next();
  }
};

app.use("/api", authHeaderCheck);

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.get("/api/protected", (req, res) => {
  res.send("This is a protected resource");
});

app.listen(port, () => {
  console.log(`app listening on port ${port}`);
});
