// Подождем, пока документ полностью загрузится
document.addEventListener('DOMContentLoaded', function () {
    // Получаем модальные окна по их ID
    var registrationModal = document.getElementById('registrationModal');
    var loginModal = document.getElementById('loginModal');

    // Если модальные окна не найдены, выходим из скрипта
    if (!registrationModal || !loginModal) {
        return;
    }

    // Получаем формы регистрации и входа
    var registrationForm = document.getElementById('registrationForm');
    var loginForm = document.getElementById('loginForm');

    // Функция для отправки данных формы регистрации с помощью AJAX
    function registerUser(event) {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию

        // Получаем данные формы регистрации
        var formData = new FormData(registrationForm);

        // Отправляем данные формы на сервер с помощью AJAX
        fetch(registrationForm.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': getCookie('csrftoken') // Получаем CSRF-токен из куки
            }
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Ошибка сети');
            }
        })
        .then(data => {
            if (data.success) {
                window.location.reload(); // Перезагружаем страницу после успешной регистрации и входа
            } else {
                console.error('Ошибка при регистрации:', data.message || data.errors);
            }
        })
        .catch(error => {
            console.error('Ошибка при регистрации:', error);
        });
    }

    // Функция для отправки данных формы входа с помощью AJAX
    function loginUser(event) {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию

        // Получаем данные формы входа
        var formData = new FormData(loginForm);

        // Отправляем данные формы на сервер с помощью AJAX
        fetch(loginForm.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': getCookie('csrftoken') // Получаем CSRF-токен из куки
            }
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Ошибка сети');
            }
        })
        .then(data => {
            if (data.success) {
                window.location.reload(); // Перезагружаем страницу после успешной регистрации и входа
            } else {
                console.error('Ошибка при входе:', data.message || data.errors);
            }
        })
        .catch(error => {
            console.error('Ошибка при входе:', error);
        });
    }

    // Назначаем обработчики событий на отправку форм регистрации и входа
    if (registrationForm) {
        registrationForm.addEventListener('submit', registerUser);
    }

    if (loginForm) {
        loginForm.addEventListener('submit', loginUser);
    }

    // Функция закрытия всех модальных окон
    function closeModals() {
        registrationModal.classList.remove('show');
        loginModal.classList.remove('show');
    }

    // Назначаем обработчики событий на кнопки закрытия модальных окон
    var closeBtns = document.querySelectorAll('.btn-close');
    if (closeBtns) {
        closeBtns.forEach(function (btn) {
            btn.addEventListener('click', closeModals);
        });
    }
});

// Функция для получения значения CSRF-токена из куки
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Ищем куку с нужным именем
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
