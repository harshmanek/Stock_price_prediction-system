import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
#for loading model
from keras.models import load_model
import streamlit as st

start= '2010-01-01'
end = '2019-12-31'
#streamlit
st.title('Stock Trend Prediction')
user_input = st.text_input('Enter Stock Ticker','AAPL')

df = data.DataReader (user_input, data_source='stooq', start=start,end=end)
df=df.reset_index()
df = df.sort_values(by='Date')
df.head()


#Describing Data
st.subheader('Data from 2010-2019')
st.write(df.describe())

fig = plt.figure (figsize = (12,6))
plt.plot(df.Date,df.Close)
st.pyplot(fig)


data = pd.DataFrame(df,columns=['Date','Close']).reset_index()
ma100 = data.Close.rolling(100).mean()
ma200 = data.Close.rolling(200).mean()
st.subheader('Graph with SMA 100&200')
fig=plt.figure(figsize = (12,6))
plt.plot(df.Date,df. Close)
plt.plot(df.Date,ma100, 'red',label='SMA100')
plt.plot(df.Date,ma200,'yellow',label='SMA200')
plt.legend(loc='upper left')
st.pyplot(fig)