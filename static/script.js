var socket = io("http://192.168.1.92:5000");
socket.on('connect', function() {
    //Reset the socket buffer if reconnection happens
    socket.sendBuffer.length = 0;
    socket.emit('my event', {data: 'I\'m connected!'});
    
});
console.log("Pinging for GetImage")
socket.emit("getImage",{})
console.log("Pinging for GetImage Done")
function sendCommand(actionType,params){
    // console.log(actionType);
    
    socket.emit('command',{
        actionType,
        params:"ff"
    });
}

function moveServos(axis,direction){
    $.ajax({
        url: "/moveServos",
        data: {
            axis,
            direction
        },
        method: "post",
        success: function(r){
            console.log("Success")
        }
    })
}
