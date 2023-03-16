#!/usr/bin/env python
# coding: utf-8

# In[1]:


nama = "AlfridaPutriBellaAzzara"
jumlah_karakter = len(nama)
print(jumlah_karakter)


# In[12]:


nama = "Alfrida Putri Bella Azzara" 
vokal = 'aiueoAIUEO' 
huruf = len(nama) - nama.count(' ') 
print ("Jumlah Huruf : ", huruf) 
jmlvkl = 0
jmlksn = 0
for i in nama: 
    if i in vokal: 
        jmlvkl += 1
    else : 
        jmlksn += 1 
print("Jumlah Huruf Vokal : ", jmlvkl) 
print("Jumlah Huruf Konsonan : ", jmlksn)


# In[ ]:




