#!/usr/bin/env python
# coding: utf-8

# # Password Authentication using Python

# In[2]:


import getpass
database= {"clcoding": "976729", "pythonclcoding":"2502"}
username= input("Enter you Username: ")
password=getpass.getpass("enter your password: ")
for i in database.keys():
    if username==i:
        while password!= database.get(i):
            password=getpass.getpass("Enter you password Again: ")
        break
print("Verified")


# In[ ]:




