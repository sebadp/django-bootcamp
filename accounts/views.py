from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect, render

from .forms import LoginForm, RegisterForm

User = get_user_model()


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        try:
            User.objects.create_user(username, email, password)
        except:
            user = None
        if user != None:
            login(request, user)
            return redirect("/home")
        else:
            request.session["register_error"] = 1
    return render(request, "products/forms.html", {"form": form})


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect("/home")
        else:
            #   SI QUISIERAMOS COMPROBAR QUE EL USUARIO NO INTENTE MAS
            # DE X VECES SU INTENTO DE HACER LOGIN::
            # attempt= request.session.get("attempt") or 0
            # request.session['atempt'] += 1
            # return redirect("/invalid-password")

            request.session["invalid_user"] = 1  # NO SERIA UN USER VALIDO
            # PORQUE USER = NONE

            return render(request, "products/forms.html", {"form": form})
    return render(request, "products/forms.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("/login")
