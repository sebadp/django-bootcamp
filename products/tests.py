from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()

# Create your tests here.

from .models import Product


class ProductTestCase(TestCase):
    """
    Vamos ahacer varios usuarios para hacer diferentes pruebas.
    """

    def setUp(self):
        user_a = User(username="UsuariodePrueba", email="usuario@deprueba.com")
        self.user_a = user_a
        user_a_pw = "contrasenia"
        self.user_a_pw = user_a_pw

        user_a.set_password(user_a_pw)
        user_a.save()
        user_a.is_staff = True
        user_a.is_superuser = False

        user_b = User(username="UsuariodePruebaSegundp", email="usuarioSegundo@deprueba.com")
        user_b.is_staff = False
        user_b.is_superuser = False
        self.user_b = user_b
        user_b_pw = "contrasenia"
        self.user_b_pw = user_b_pw
        user_b.set_password(user_b_pw)
        user_b.save()

    def test_user_count(self):
        """
        Probamos que los usuarios se hayan creado correctamente.
        """
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 2)

    def test_invalid_request(self):
        """
        Tendría que retornar True si no se le permite al usuario crear el producto.
        Porque no tiene el permiso requerido de ser staff
        """
        self.client.login(username=self.user_b.username, password=self.user_b_pw)
        response = self.client.post(
            "/products/create/", {"title": "Esto es un producto de prueba que no se podría crear."}
        )
        self.assertTrue(response.status_code != 200)

    def test_valid_request(self):
        """
        Tendría que retornar True si le permite al usuario staff crear el producto.
        """
        self.client.login(username=self.user_a.username, password=self.user_a_pw)
        response = self.client.post("/products/create/", {"title": "Esto es un producto de prueba."})
        self.assertEqual(response.status_code, 200)
