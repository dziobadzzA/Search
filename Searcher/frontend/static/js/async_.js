
let token = $('input[name="csrfmiddlewaretoken"]').prop('value');

function read_name() {
    var path=""
    //console.log($("#inp"))
              // path
     // TODO read file
    return path;
}

$("#test").click(
        function() {
              request_test(read_name(), 0)
        }
);

$("#combat").click(
        function() {
              request_test(read_name(), 1)
        }
);


function request(path, command) {
        $.ajax({
	        url: "",
	        method: 'post',
	        data: {
	         'csrfmiddlewaretoken': token,
	         'path': path,
	         'command': command
	        },
	        success: function(){
	            console.log("success send to process name 'Test' ")
	        },
	        error: function(){
		        console.log("error");
	        }
        });
}

