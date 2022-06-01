#!/usr/bin/env python
# coding: utf-8

# # Python Programe to Generate Password

# In[2]:


import random
passlen= int(input("Enter the length of password"))
s="qwertyuioplkjhgfdsazxcvbnm1234567890@#$%^&*!"
p="".join(random.sample(s,passlen))
print(p)


# In[ ]:




