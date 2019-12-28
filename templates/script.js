var socket = io("http://192.168.1.92:5000");
socket.on('connect', function() {
    socket.emit('connect', {data: 'I\'m connected!'});
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
