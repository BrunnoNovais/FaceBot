from selenium import webdriver
from time import sleep


class FacebookBot:
    def __init__(self, email, senha):
        self.driver = webdriver.Chrome('chromedriver') # Carregando o Driver
        self.user_login = email # Pegando Email
        self.pass_login = senha # Pegando a Senha

    def FazerLogin(self):
        self.driver.get('https://www.facebook.com/') # Acessando o Site
        sleep(3) # Temos que colocar esse Time para não travar o Programa
        CAIXA_LOGIN = self.driver.find_element_by_name('email') # id do elemento "input email" no facebook
        sleep(1)
        CAIXA_LOGIN.click() # Clicando no elemento detctado
        sleep(1)
        CAIXA_LOGIN.send_keys(self.user_login) # Inserido o Email
        sleep(1)
        CAIXA_SENHA = self.driver.find_element_by_id('pass') # id do elemento "input senha" no facebook
        sleep(1)
        CAIXA_SENHA.click() # Clicando no Componente
        sleep(1)
        CAIXA_SENHA.send_keys(self.pass_login) # Inserido a Senha
        sleep(1)
        BOTÃO_LOGIN = self.driver.find_element_by_id('loginbutton') # id do elemento "botão entrar" no facebook
        sleep(1)
        BOTÃO_LOGIN.click() # Clicando Nesse Botão


FaceBot = FacebookBot#(Email,#Senha )

# FaceBot.FazerLogin()
