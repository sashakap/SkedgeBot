const express = require("express");
const app = express();
app.set('view engine', 'ejs');

const path = require("path");
const templatePath = path.join(__dirname, './views');
app.use(express.static(templatePath));
app.set("views", templatePath);

app.listen(3000, () => {
  console.log("Application started and Listening on port 3000");
});

app.get("/", (req,res)=>{
    res.render("index")
});
app.get("/about-me", (req,res)=>{
    res.render("about-me")
});
app.get("/contact-me", (req,res)=>{
    res.render("contact-me")
});
app.post("/add_cal", (req,res)=>{
    res.render("add_cal")
});

