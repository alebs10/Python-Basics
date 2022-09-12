#!/usr/bin/env python
# coding: utf-8

# In[6]:


print("***COMPARAÇÃO DE VALORES***")

valor_1 = float(input("DIGITE O PRIMEIRO VALOR: "))
valor_2 = float(input("DIGITE O SEGUNDO VALOR: "))
valor_3 = float(input("DIGITE O TERCEIRO VALOR: "))

if valor_1 > valor_2 and valor_1 > valor_3:
    print("O MAIOR NÚMERO É: ", valor_1)
elif valor_2 > valor_1 and valor_2 > valor_3:
    print("O MAIOR NÚMERO É: ", valor_2)
else:
    print("O MAIOR NÚMERO É: ", valor_3)


# In[ ]:




