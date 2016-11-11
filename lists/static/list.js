var hideErrorsOnKeypess = function() {
    var input = $("input[name='text']");
    input.on('keypress', function(){
        $('.has-error').hide();
    });
};

$(document).ready(hideErrorsOnKeypess);
