const sqlite = require("sqlite3").verbose();

let db = new sqlite.Database("Blog.db", (err) => {
  if (err) return console.error(err.message);
  console.log("Connected with Database");
});

db.all(`select Name, Content, ArticleName, Articles.Date 
        from Articles join Comments on Articles.ArticleID = Comments.ArticleID
    `, (err, table) => {
    if (err) return console.error(err.message);
    console.log(table);
    });

db.close((err) => {
  if (err) return console.error(err.message);
  console.log("Close Database");
});
