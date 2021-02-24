from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.

User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        user_a = User(username="UsuariodePrueba", email="usuario@deprueba.com")
        user_a.is_staff = True
        user_a.is_superuser = True
        self.user_a = user_a
        user_a_pw = "contrasenia"
        self.user_a_pw = user_a_pw
        user_a.set_password(user_a_pw)
        user_a.save()
        user_a.set_password

    # Vamos a crear un usuario que luego podemos reutilizar

    def test_user_exist(self):
        """
        Vamos a probar que se crea sólo un usuario.
        """
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)

    def test_user_password_correct(self):
        """
        Vamos a probar que se chequee la contraseña correcta. Tendría que retornar True.
        """
        self.assertTrue(self.user_a.check_password(self.user_a_pw))

    def test_user_password_incorrect(self):
        """
        Tendría que retornar Falso al incorporar una contraseña incorrecta.
        """
        self.assertFalse(self.user_a.check_password("sarasa"))


class ViewsTestsCase(TestCase):
    def setUp(self):
        user_a = User(username="UsuariodePrueba", email="usuario@deprueba.com")
        user_a.is_staff = True
        user_a.is_superuser = True
        self.user_a = user_a
        user_a_pw = "contrasenia"
        self.user_a_pw = user_a_pw
        user_a.set_password(user_a_pw)
        user_a.save()
        user_a.set_password

    def test_login_url_view(self):
        """
        Si visitamos el view de login, Tiene que ser igual que el login que tenemos configurado en settings.py.
        Nos debe responder con el código 200.
        """
        url_login = settings.LOGIN_URL
        # response = self.client.post(url, {}, follow=True)
        data = {"username": "usuario", "password": self.user_a_pw}
        response = self.client.post(url_login, data, follow=True)
        # print(dir(response))
        status_code = response.status_code
        redirect_path = response.request.get("PATH_INFO")
        self.assertEqual(url_login, redirect_path)
        self.assertEqual(status_code, 200)
