import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.login
class TestCT03:

    def test_ct03_login_invalido(self):
        menssagem_erro_esperada = 'Epic sadface: ''Username and password do not match any user in this service'

        # Instância os objetos a serem usandos no teste
        login_page = LoginPage()

        # Faz login
        login_page.fazer_login('standard_user', 'secret_sauczzz')

        # Verifica se o login não foi realizado
        login_page.verificar_mensagem_erro_login_existe()

        # Verifica o texto da mensagem de erro
        login_page.verificar_texto_menssage_erro_login(menssagem_erro_esperada)


