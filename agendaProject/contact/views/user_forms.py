from django.shortcuts import redirect, render
from contact.forms import RegisterForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'User criado com sucesso')
            return redirect('contact:login')
    context = {"form": form,
               "site_title": "Register User",
               }
    return render(request, "contact/register.html", context)


def login_view(request):
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            messages.success(request, 'LOGADO COM SUCESSO')
            auth.login(request, user)
            return redirect('contact:index')
        messages.error(request, 'LOGIN INVÁLIDO')

    context = {'form': form, 'site_title': 'Login'}
    return render(
        request,
        'contact/login.html',
        context
    )


def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')
