const ws = require("ws")

const server = new ws.Server({ host: '0.0.0.0', port: 3434})

server.on('connection', socket => {
    console.log("New connection");
    socket.on('message', message => {
        console.log(message);
        server.clients.forEach(client => {
            client.send(message);
        });
    });
});