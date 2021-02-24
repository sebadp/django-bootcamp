from django import forms
from django.contrib.auth import get_user_model

non_allowed_usernames = [
    "sarasa",
    "marchanta",
]
User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password1 = forms.CharField(
        max_length=100,
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    password2 = forms.CharField(
        max_length=100,
        label="confirm-password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
            }
        ),
    )


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            # Estos son atributos que luego se agregan en la etiqueta html correspondiente
            attrs={
                "class": "form-control",
            }
        ),
    )

    # def clean(self):
    #     username = self.cleaned_data.get("username")
    #     password = self.cleaned_data.get("password")
    #   En este bootcamp vamos a hacer más validaciones en las vistas
    # Pero lo ideal es que las validaciones estén acá.

    def clean_username(self):
        username = self.cleaned_data.get("username")
        # UNA VEZ Q LIMPIAMOS LA DATA, CHECKEAMOS QUE NO HAYA OTRO
        # USUARIO CON EL MISMO NOMBRE
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("This is an invalid user, please pick another.")
        # para agregar una lista de usuarios no validos
        # antes hay que declarar la lista arriba de todo
        if username in non_allowed_usernames:
            raise forms.ValidationError("This is an invalid user, please pick another.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if not qs.exists():
            raise forms.ValidationError("This is an invalid email, please pick another.")
        return email
