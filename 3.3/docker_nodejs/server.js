const http=require('http');
const port=Number(process.env.PORT||10000);
http.createServer((req,res)=>{
 if(req.url==='/api'){res.writeHead(200,{'Content-Type':'application/json; charset=utf-8'});return res.end(JSON.stringify({service:'Node.js',student:'Maxim Kuznetsov',group:'IKBO-15-25',sum:2+3,node:process.version}));}
 res.writeHead(200,{'Content-Type':'text/html; charset=utf-8'});
 res.end('<!doctype html><meta charset="utf-8"><title>Node.js</title><h1>Node.js в Docker</h1><p>Кузнецов Максим Дмитриевич, ИКБО-15-25</p><p>Это ответ настоящего HTTP-сервера Node.js '+process.version+'.</p><p><a href="/api">Пример API: вычисление 2 + 3</a></p>');
}).listen(port,'0.0.0.0',()=>console.log('Node.js service ready on '+port));
