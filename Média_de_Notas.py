#!/usr/bin/env python
# coding: utf-8

# In[20]:


print("***CÁLCULO DE MÉDIA***")

nota_1 = input("DIGITE A PRIMEIRA NOTA: ")
nota_1 = float(nota_1)

nota_2 = input("DIGITE A SEGUNDA NOTA: ")
nota_2 = float(nota_2)

nota_3 = input("DIGITE A TERCEIRA NOTA: ")
nota_3 = float(nota_3)

nota_final = (nota_1 + nota_2 + nota_3) / 3

if nota_final >= 7:
    print("PARABÉNS, VOCÊ PASSOU !")
elif nota_final >=5 and nota_final <7:
    print("VOCÊ ESTÁ DE RECUPERAÇÃO.")
else:
    print("VOCÊ ESTÁ REPROVADO.")


# In[ ]:




