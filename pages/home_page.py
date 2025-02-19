from selenium.webdriver.common.by import By

import conftest
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH, '//div[@class="product_label" and text()="Products"]')
        self.item_inventario = (By.XPATH, '//div[@class="inventory_item_name" and text()="{}"]')
        self.botao_adicionar_carrinho = (By.XPATH, '//button[text()="ADD TO CART"]')
        self.icone_carrinho = (
            By.XPATH, '//a[@href="./cart.html"] | //div[@id="shopping_cart_container"]/a[contains(@class, '
                      '"shopping_cart_link")]')

    def verificar_login_com_sucesso(self):
        self.encontrar_elemento(self.titulo_pagina)

    def adicionar_ao_carrinho(self, nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.clicar(item)
        self.clicar(self.botao_adicionar_carrinho)

    def acessar_carrinho(self):
        self.clicar(self.icone_carrinho)
