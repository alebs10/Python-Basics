#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("***IGUAIS OU DIFERENTES")

valor1 = float(input("DIGITE O PRIMEIRO VALOR: "))
valor2 = float(input("DIGITE O SEGUNDO VALOR: "))

if valor1 == valor2 and valor1 > valor2:
    print("OS VALORES", valor1," E", valor2, "SÃO IGUAIS")
elif valor1 == valor2 and valor2 > valor1:
    print("OS VALORES", valor2," E", valor1, "SÃO IGUAIS")
elif valor1 != valor2 and valor1 > valor2:
    print("OS VALORES", valor1," E", valor2, "SÃO DIFERENTES")
else:
    print("OS VALORES", valor2," E", valor1, "SÃO DIFERENTES")


# In[ ]:




