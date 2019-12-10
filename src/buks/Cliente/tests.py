from django.test import TestCase
import unittest
from .models import Cliente

# Create your tests here.

class ClientTest(unittest.TestCase):

    def setUp(self):
        self.teste = Cliente.objects.create(cpf="121.212.232-18", nome="Otávio Augusto de Sousa Resende",
                                         data_nasc="1998-01-27", email="otavioresende1998@gmail.com",
                                         celular="37998371524")

    def testAdress(self):
        self.assertEquals(self.teste.get_adress(), "otavioresende1998@gmail.com")


