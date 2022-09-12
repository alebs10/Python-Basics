#!/usr/bin/env python
# coding: utf-8

# In[2]:


contador = 0

while contador < 10:
    contador = contador + 1
    if contador == 1:
        print(contador, "Item limpo")
    else:
        print(contador, "Itens limpos")
        
print("Fim da repetição do bloco while.")


# In[4]:


contador = 0

while True:
    if contador < 10:
        contador = contador + 1
        if contador == 1:
            print(contador, "Item limpo")
        else:
            print(contador, "Itens limpos")
    else:
        break
        
print("Fim da repetição do bloco while.")


# In[5]:


texto = input("Digite a sua senha: ")

while texto != 'LetsCode':
    texto = input("Senha inválida, tente novamente")
    
print("Acesso permitido")


# In[6]:


contador = 0

while contador < 10:
    contador = contador + 1
    if contador == 1:
        continue
    print(contador, "Itens limpos")
        
print("Fim da repetição do bloco while.")


# In[ ]:




