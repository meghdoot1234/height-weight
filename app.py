#!/usr/bin/env python
# coding: utf-8

# In[12]:


import streamlit as st
from predict_cost import predict
import numpy as np
import pandas as pd
df_new = pd.read_csv('weight-height.csv')
df_w = df_new.drop('Gender',axis = 1)
st.title('Weight Prediction by Dr. Meghdoot Ghosh')
st.write('---------------------------------------')
height = st.slider('enter the height',50,200)
if st.button('Predict your Weight'):
    myheight = predict(np.array([[height]]))
    st.text(myheight[0])
    st.line_chart(df_w)


# In[ ]:





# In[ ]:




