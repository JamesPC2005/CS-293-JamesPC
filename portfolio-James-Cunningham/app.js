// console.log("Start");

// setTimeout(()=>{console.log("inside timeout")},2000);

// console.log("end")

const http = require("http");
const fs = require("fs");
const path = require("path")


const server = http.createServer((req, res) =>{

    let filepath = req.url;

    if(filepath==="/"){
        filepath = "/index.html"
    }

    filepath = path.join(__dirname, filepath);

    const ext = path.extname(filepath);

    let content="text/plain";

    if(ext === ".html"){content = "text/html"};
    if(ext === ".css"){content = "text/css"};
    if(ext === ".js"){content = "text/javascript"};

    fs.readFile(filepath, (err,data)=>{

        if (err) {
            res.writeHead(404, { "Content-Type": "text/plain" });
            res.end("Not found");
            return;
        }

        res.writeHead(200, { "Content-Type": content });
        res.end(data);
    });

});

server.listen(3000, () => {
    console.log("server running on http://localhost:3000")
});