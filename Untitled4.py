#!/usr/bin/env python
# coding: utf-8

# In[4]:


import yfinance as yf
import pandas as pd
import numpy as np


# In[36]:


data=yf.download(tickers='SBIN.NS ITC.NS',period='2d',interval='5m')
#data[['Close','High','Low']]
data


# In[ ]:




