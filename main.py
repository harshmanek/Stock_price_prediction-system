import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
import streamlit as st
#for loading model
from keras.models import load_model

start= '2010-01-01'
end = '2019-12-31'
#streamlit
st.title('Stock Trend Prediction')
user_input = st.text_input('Enter Stock Ticker','AAPL')
#
df = data.DataReader ('AAPL', data_source='stooq', start=start,end=end)
df=df.reset_index()
print(df)


#Describing Data
st.subheader('Data from 2010-2019')
st.write(df.describe())

#Visualizations
st.subheader('Closing Price vs Time chart')
# fig,ax = plt. figure(figsize=(12,6))
import seaborn as sns


def _plot_series(series, series_name, series_index=0):
  from matplotlib import pyplot as plt
  import seaborn as sns
  palette = list(sns.palettes.mpl_palette('Dark2'))
  xs = series['Date']
  ys = series['Close']

  plt.plot(xs, ys, label=series_name)


fig, ax = plt.subplots(figsize=(10, 5.2))
df_sorted = df.sort_values('Date', ascending=True)
_plot_series(df_sorted, '')

plt.xlabel('Date')
_ = plt.ylabel('Open')
st.pyplot(fig)
#
#
st.subheader('Closing Price vs Time chart with 100MA and 200MA')
ma100 = df. Close.rolling(100).mean()
ma200 = df. Close.rolling(200).mean()
fig = plt.figure(figsize = (12,6))
plt.plot (ma100)
plt.plot (ma200)
plt.gca().invert_xaxis()
plt.plot (df. Close)
st.pyplot(fig)

