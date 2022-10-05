$("#btn").click(function(){

    var token = $('input[name="csrfmiddlewaretoken"]').prop('value');

    $.ajax({
	    url: '/test/',
	    method: 'post',
	    data: {"score": 1,
	     'csrfmiddlewaretoken': token
	     },
	    success: function(data){
		    console.log(data["data"]);

		    $("#text").text(data["data"])
	    },
	    error: function(){
		    console.log("error");
	    }
    });

})

