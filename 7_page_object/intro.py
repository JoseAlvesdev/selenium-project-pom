"""
Page Object
  A ideia do PageObject é separar os elementos em arquivos diferentes baseados nas páginas
  em que eles aparecem, assim, escrevemos todos os elementos e métodos específicos
  daquela página em seu arquivo que é uma classe e usamos diretamente nos scripts de teste.

   # Fazendo login (sem page object)
     driver.find_element(By.ID, "user-name").send_keys("standard_user")
     driver.find_element(By.ID, "password").send_keys("secret_sauce")
     driver.find_element(By.ID, "login-button").click()

   # Fazendo login (com page object)
     login_page.fazer_login("standard_user", "secret_sauce"
"""