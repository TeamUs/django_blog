$(function ($) {

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    $('#login_ajax').submit(function (e) {
        e.preventDefault();
        const csrftoken = getCookie('csrftoken'); // Получение CSRF-токена
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            headers: {'X-CSRFToken': csrftoken}, // Передача CSRF-токена в заголовках запроса
            dataType: 'json',
            success: function (response) {
                console.log('ok - ', response);
                if (response.status === 201) {
                    window.location.reload();
                } else if (response.status === 400) {
                    $('.alert-danger').text(response.error).removeClass('d-none');
                }
            },
            error: function (response) {
                console.log('err - ', response);
            }
        });
    });


    $('#register_ajax').submit(function (e) {
        e.preventDefault();
        const csrftoken = getCookie('csrftoken'); // Получение CSRF-токена
        $.ajax({
            type: this.method,
            url: this.action,
            data: {
                'username': $('#register_username').val(),
                'email': $('#register_email').val(),
                'password1': $('#register_password1').val(),
                'password2': $('#register_password2').val(),
            },
            headers: {'X-CSRFToken': csrftoken}, // Передача CSRF-токена в заголовках запроса
            dataType: 'json',
            success: function (response) {
                console.log('Register success - ', response);
                if (response.status === 201) {
                    window.location.reload();
                } else if (response.status === 400) {
                    $('.alert-danger').text(response.errors).removeClass('d-none');
                }
            },
            error: function (response) {
                console.log('Register error - ', response);
            }
        });
    });
});
