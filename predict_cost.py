#!/usr/bin/env python
# coding: utf-8

# In[1]:


import joblib
def predict(data):
    regressor = joblib.load('regressor_model.sav')
    return regressor.predict(data)


# In[ ]:




