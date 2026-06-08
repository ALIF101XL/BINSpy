(function() {
	var paths = [
		'localhost/static/js/libs.min.js',
		'localhost/static/js/base.js',
		'localhost/static/js/BINSpy.js'
	];
	window.gMapsApiKey = "AIzaSyBUPHAjZl3n8Eza66ka6B78iVyPteC5MgM";
	var imported = {};
	var idx = 0;

	loadScript(function(){
		idx++;
		loadScript(function(){
			idx++;
			window.serverPath = 'localhost';
			loadScript(function(){
				idx++;
			});
		});
	});

	function loadScript(callback){
		imported = document.createElement('script');
	    imported.type = 'text/javascript';
		imported.src = paths[idx];

	    imported.onload = callback;

	    var head = document.getElementsByTagName('head')[0];
	    head.appendChild(imported, head);
	}
}())