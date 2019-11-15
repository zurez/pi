var socket = io("http://127.0.0.1:5000");
socket.on('connect', function() {
    socket.emit('my event', {data: 'I\'m connected!'});
});

function sendCommand(actionType,params){
    console.log(actionType);
    
    socket.emit('command',{
        actionType,
        params:"ff"
    });
}

function receiveUpdate(updateString){
    console.log(updateString);
    
}

socket.on("update",receiveUpdate);