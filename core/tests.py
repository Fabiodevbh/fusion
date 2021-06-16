from django.test import TestCase

"""
Quando vamos executar algum teste, devemos estar conectados ao banco de dados que usamos para desenvolvimento e o 
DEBUG deve ser True.

Os testes são rodados no terminal através do comando: "python manage.py test"

"""

# Teste 1 =============================================================================================================


def add_num(num):  # Função a ser testada
    return num + 1


class SimplesTestCase(TestCase):

    # roda toda vez
    def setUp(self):
        self.numero = 40

    # Testa a unidade de código
    def test_add_num(self):
        valor = add_num(self.numero)
        self.assertTrue(valor == 42)





