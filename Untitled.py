
# coding: utf-8

# # My First Jupyter Notebook
# ## Zakk Hess
# This is my very first Jupyter Notebook. I am a Python newbie. Here are some things I would like to do with Python 3:
# 
# 1. Read in hydrologic data
# 2. Do some data analysis
# 3. Create some plots
# 4. Output some data
# 

# In[53]:


import numpy as np #import numpy library
import matplotlib.pyplot as plt #import plotting library

rand_matrix = np.random.random((50))

plt.plot(rand_matrix)
plt.ylabel('Rand. Numbers')
plt.show()

