from django.test import TestCase
import unittest
from .models import Cliente

# Create your tests here.

class ClientTest(unittest.TestCase):

    def testAdress(self):
        self.teste = Cliente.objects.create(cpf="128.987.176-73", nome="Otávio Augusto de Sousa Resende",
                                    data_nasc="1998-01-27", email="otavioresende1998@gmail.com",
                                    celular="37998371524")
        self.assertEquals(self.teste.get_adress(), "otavioresende1998@gmail.com")
        

    def testeIdade(self):   
        self.teste = Cliente.objects.create(cpf="128.987.176-74", nome="Otávio Augusto de Sousa Resende",
                                    data_nasc="1998-01-27", email="otavioresende1998@gmail.com",
                                    celular="37998371524")
        self.assertFalse(self.teste.maior_que(17))