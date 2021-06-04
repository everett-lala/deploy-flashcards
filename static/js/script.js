$(document).ready(function() {
    $("#email").change(function() {
        var email = $(this).val();

        $.ajax({
            url: '/validate_email/',
            data: {
                'email': email
            },
            dataType: 'json',
            success: function(data) {
                if (data.is_taken) {
                    alert("A user with this email already exists.");
                }
            }
        });

    });
});


$(document).ready(function() {
    $("#username").change(function() {
        var username = $(this).val();

        $.ajax({
            url: '/validate_username/',
            data: {
                'username': username
            },
            dataType: 'json',
            success: function(data) {
                if (data.is_taken) {
                    alert("A user with this username already exists.");
                }
            }
        });

    });
});