#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importando as bibliotecas de uso
import urllib.request
from bs4 import BeautifulSoup


# In[2]:


#definindo a URL e armazenas na variável page
with urllib.request.urlopen("https://www.flamengo.com.br/elencos/elenco-profissional") as url:
    page = url.read()


# In[3]:


#imprimir o conteúdo
print(page)


# In[4]:


#criando o parser - tags do html
soup = BeautifulSoup(page, "html.parser")


# In[5]:


#extraindo jogadores da pagina 
vetor_ad_name = soup.select('.elenco-atleta p')
vetor_ad_name


# In[6]:


#estraindo imagens da pagina
vetor_ad_img = soup.select('.elenco-atleta img')
vetor_ad_img


# In[7]:


#extraindo as posições dos jogadores
vetor_ad_posicao_jogador = soup.select('.title-pages')
vetor_ad_posicao_jogador


# In[8]:


#bot para gerar arquivo json sem a categorização, pois estavam em tags diferentes
# vetor_ad_name[0]
# vetor_ad_posicao_jogador[0]
#vetor_ad_img[0]

list_ad = []
comp=len(vetor_ad_name)-1
comp_img = len(vetor_ad_img)-1
for i in range(0,comp):
    ad={}
    ad["nome_jogador"] = vetor_ad_name[i].getText(strip=True)
    ad["imagem_jogador"] = vetor_ad_img[i]['src']
    list_ad.append(ad)
print(list_ad)        


# In[9]:


#extraindo as posições dos jogadores
vetor_ad_posicao_jogador = soup.select('.title-pages')
ad_list = []
comp_posicao = len(vetor_ad_posicao_jogador)-1
for i in range(0,comp_posicao):
    ad_jogador={}
    ad_jogador["posicao_jogador"] = vetor_ad_posicao_jogador[i].getText(strip=True)
    ad_list.append(ad_jogador)
print(ad_list)
