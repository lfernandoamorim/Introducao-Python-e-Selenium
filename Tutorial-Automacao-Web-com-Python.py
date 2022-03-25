#!/usr/bin/env python
# coding: utf-8

# # Automação Web com Python
# 
# ### Python + Selenium
# 
# Neste tutorial tem o conceito básico de RPA com o Chrome, para que esse tutorial funcione, é necessário fazer os passos abaixo:
# 
# 1. Instalar o Selenium dentro do Jupyter
# > para isso abra o terminal no Jupyter e digite:***pip install selenium***
#     
# 2. Baixar e colocar o chromewebdriver
# > coloca na pasta que está o projeto e também (não obrigatório) na pasta anaconda3 (3 por causa da versão que usei no momento)

# In[ ]:





# In[3]:


#Passo 1: acessar o site https://www.advancesistemas.net/
#passo 2: logar com meu usuário
#Passo 3: Fazer download da planilha de crachas


# In[5]:


#importa a biblioteca webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

#abre o navegador crhome, mas tenha certeza de o chromedriver.exe esteja na pasta python e/ou
#anaconda (C:\ProgramData\Anaconda3), ou referencie para a pasta do projeto 
#usando webdriver.Chrome(executable_path=r'./chromedriver.exe')
navegador = webdriver.Chrome()

#abre o navegador crhome
navegador.get('https://www.advancesistemas.net/')

#busca o elemento xptah de um elemento, nesse caso o do link aAcessar Conta
#quando utilizar xpath, coloque o elemento sempre entre ''
elemento = navegador.find_element(By.XPATH,'//*[@id="comp-kns04bql"]/button')
elemento.click()


# In[ ]:




