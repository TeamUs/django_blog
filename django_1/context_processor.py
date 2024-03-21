from blog.forms import AuthenticationAjaxForm


def get_context_data(request):
    context = {
        'login_ajax': AuthenticationAjaxForm(),
        'register_ajax': AuthenticationAjaxForm()
    }
    return context