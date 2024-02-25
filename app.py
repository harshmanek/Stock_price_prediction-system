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


#splitting data into training and testing

data_training  = pd.DataFrame(df['Close'][0:int(len(df)*0.7)])
data_testing = pd.DataFrame(df['Close'][int(len(df)*0.7):int(len(df))])

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))

data_training_array = scaler.fit_transform(data_training)

#loading model
model = load_model('keras_model2.h5')

#testing
past_100_days = data_training.tail(100)
past_100_days = pd.DataFrame(past_100_days)

final_df = pd.concat([past_100_days,data_testing],axis=0)

input_data = scaler.fit_transform(final_df)

x_test = []
y_test = []

for i in range(100,input_data.shape[0]):
  x_test.append(input_data[i-100:i])
  y_test.append(input_data[i,0])

x_test, y_test = np.array(x_test), np.array(y_test)

# predictions

y_predicted = model.predict(x_test)
scalr = scaler.scale_
y_predicted = y_predicted * (1/scalr)
y_test= y_test* (1/scalr)

#predicted graph
st.subheader("Trend Prediction")
fig = plt.figure(figsize=(12,6))
plt.plot(y_test,'b',label='Original Price')
plt.plot(y_predicted,'r',label='Predicted')
plt.xlabel('time')
plt.ylabel('price')

plt.legend()
st.pyplot(fig)